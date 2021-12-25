import re

def is_valid_backlink(curr_backlink):
    red_flag_phrases=["Wikipedia","talk","Archive","File","User","Wikipedia"]
    for curr_phrase in red_flag_phrases:
        if curr_phrase in curr_backlink:
            return False 
    return True

def purify_backlinks(backlinks_arr):
    # print(backlinks_arr)
    final_arr=list(filter(lambda x:is_valid_backlink(x),backlinks_arr))
    return final_arr

def purify_categories(cat_arr):
    return [x.replace("Category:","") for x in cat_arr]

def rem_wikidata_page_id(q_str):
    if type(q_str)==list:
        return list_rem_wikidata_page_id(q_str)
    if q_str==None:
        return None
    #print("q_str is ",q_str)
    q_str=re.sub(r'\(Q.*\)', '', q_str)
    q_str=re.sub(r'\(P.*\)', '', q_str)
    return q_str.rstrip().lstrip()

def purify_gender(p_gender):
    assert(type(p_gender)!=list)
    return rem_wikidata_page_id(p_gender)

def list_rem_wikidata_page_id(occ_list):
    if type(occ_list)!=list:
        return rem_wikidata_page_id(occ_list)
    return [rem_wikidata_page_id(x) for x in occ_list]

def purify_date_of_birth(dob):
    if type(dob)==list:
        dob=dob[0]
    curr_str=""
    for curr_ch in dob[1:]:
        if curr_ch=='T':
            break
        curr_str+=curr_ch
    # print("mod str is ", curr_str)
    # "sample": "+1947-05-01T00:00:00Z",
    dob_dict={}
    dob_dict['year']=None
    dob_dict['month']=None
    dob_dict['day']=None  

    dob=curr_str
    try:
        # print(dob.split("-"))
        tokens=[int(x) for x in dob.split("-")]
        # print("toks are ", tokens)
        assert(len(tokens)==3)
        dob_dict['year']=tokens[0]
        dob_dict['month']=tokens[1]
        dob_dict['day']=tokens[2]   
    except:
        pass
    
    return dob_dict

def get_univs_from_alma_mater(curr_str):
    if "{" in curr_str:
        arr=re.findall('\[\[.*\]\]', curr_str)
    else:
        arr = re.compile("<.*?br.*?/?>").split(curr_str)
  
    # print(arr)
    arr=[x.replace("[","") for x in arr]
    arr=[x.replace("]","") for x in arr]
    arr=list(filter(lambda x:x!="", arr))
    return arr

def fetch_nums_from_str(curr_str):
    curr_str=curr_str.replace("."," ")
    rr = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", curr_str)
    return [int(x) for x in rr]

def purify_birth_date(b_str):
    b_str=b_str.lower()
    # "sample": "{{Birth date|1917|3|7}}",
    # "birth_date": "{{birth date and age|df|=|yes|1959|7|28}}",
    # "birth_date": "{{birth year and age|1980}}",
    # "birth_date": "January 8, 1917",
    # "birth_date": "1975",
    # "birth_date": "{{b-da|October 23, 1960}}",
    # "birth_date": "{{bya|1950}}",
    # "birth_date": "May 1967",




    dob_dict={}
    dob_dict['year']=None
    dob_dict['month']=None
    dob_dict['day']=None
    if "year" in b_str:
        tokens=fetch_nums_from_str(b_str)
        assert(len(tokens)>=1)
        dob_dict['year']=tokens[0]
    elif "date" in b_str:
        tokens=fetch_nums_from_str(b_str)
        if len(tokens)<3:
            dob_dict['year']=tokens[0]

            # print(tokens)
            # print(b_str)
        else:
            assert(len(tokens)>=3)
            dob_dict['year']=tokens[0]
            dob_dict['month']=tokens[1]
            dob_dict['day']=tokens[2]
    else:
        months_list=['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
        months_list=[x.lower() for x in months_list]
        for idx, curr_month in enumerate(months_list):
            if curr_month in b_str:
                dob_dict['month']=idx+1
                break
        tokens=fetch_nums_from_str(b_str)
        for curr_token in tokens:
            if curr_token>=1500 and curr_token<=2100:
                dob_dict['year']=curr_token
                break

        for curr_token in tokens:
            if curr_token>=1 and curr_token<=31:
                dob_dict['day']=curr_token
                break
    return dob_dict

def purify_birth_place(place_str):
    # "[[Repino, Saint Petersburg|Kuokkala]], [[Grand Duchy of Finland]], [[Russian Empire]]"
    # "[[Pittsburgh]], [[Pennsylvania]], U.S."
    in_cnt=0
    pipe_found=False
    ans_str=""
    for ch in place_str:
        if ch=="[":
            in_cnt+=1
            if in_cnt==2:
                pipe_found=False
        elif ch=="]":
            in_cnt-=1
            if in_cnt==0:
                pipe_found=False
        elif ch=="|":
            pipe_found=True
        else:
            if not pipe_found:
                ans_str+=ch
    return ans_str

def purify_profile_image(img):
    if type(img)!=list:
        return []
    else:
        return img
    
def purify_known_for(k_str,comma_split=False):
    # "[[database systems]]<br>[[operating systems]]"
    # "[[Artificial Intelligence]] <br />Autonomy<br />[[Multi-Agent System]]s <br />[[Automated planning and scheduling]] <br />Personalization Technologies<br />Mixed-Initiative Problem Solving"
    # "{{Plainlist|\n* [[RC 4000 multiprogramming system]]\n* [[Operating system]]s [[Kernel (operating system)|kernels]], [[microkernel]]s\n* [[Monitor (synchronization)|Monitors]]\n* [[Concurrent programming]]\n* [[Concurrent Pascal]]\n* Distributed Processes\n* [[Parallel computing]]\n* [[Distributed computing]]}}
    # "[[visual culture]], [[design]], [[information visualization]], [[graph drawing]], [[tree structure]]."
    # "[[Biogeography]], ''[[Kosmos (Humboldt)|Kosmos]]'' (1845\u20131862), [[Humboldt Current]], [[magnetic storm]], [[Humboldtian science]], [[Berlin Romanticism]]"
    # "{{ublist|''[[The Art of Computer Programming]]''|[[TeX]], [[METAFONT]], [[Computer Modern]]|[[Knuth's up-arrow notation]]|[[Knuth\u2013Morris\u2013Pratt algorithm]]|[[Knuth\u2013Bendix completion algorithm]]|[[MMIX]]|[[Robinson\u2013Schensted\u2013Knuth correspondence]]|[[LR parser]]|[[Literate programming]]}}"
    # "[[Classification and regression tree|CART]], [[Bootstrap aggregating|Bagging]], [[Random forest]]"
    # "[[Optimal Control]], [[Decision Making]], [[Deep Learning]], [[AlphaGo]], [[AlphaZero]]"
    # "The eponymous [[Paris Kanellakis Award|award]] given annually by the [[Association for Computing Machinery|ACM]]."

    if "{" in k_str:
        # just extract inside [] in a sep list
        arr=[]
        in_cnt=0
        curr_str=""
        pipe_pres=False
        for ch in k_str:
            if ch=='[':
                in_cnt+=1
                if in_cnt==2:
                    pipe_pres=False
            elif ch==']':
                in_cnt-=1
                if in_cnt==0:
                    pipe_found=False
                if curr_str!="":
                    arr.append(curr_str)
                    curr_str=""
            elif ch=='|':
                pipe_pres=True
            else:
                if in_cnt==2 and (not pipe_pres):
                    curr_str+=ch
        if curr_str!="":
            arr.append(curr_str)
            curr_str=""
    else:
        # separate by new line , br, ","
        if type(k_str)==str:
            arr=k_str.split("\n")
        else:
            arr=[]
            for curr_elem in k_str:
                arr.extend(curr_elem.split("\n"))
        ######################################
        # split by BR
        mod_arr = [re.compile("<.*?br.*?/?>").split(x) for x in arr]
     
        arr=[]
        for curr_elem in mod_arr:
            arr.extend(curr_elem)
        #############################
        if comma_split:
            mod_arr = [re.compile(",").split(x) for x in arr]
     
            arr=[]
            for curr_elem in mod_arr:
                arr.extend(curr_elem)

       
        arr=[purify_birth_place(x) for x in arr]
        # arr=[x.replace("]","") for x in arr]
    arr= [ x.lstrip().rstrip() for x in arr]
    arr=list(filter(lambda x:x!="", arr))
    return arr



def purify_doctoral_advisor(curr_str):
    #  "doctoral_advisor": "[[David Patterson (computer scientist)|David A. Patterson]]",
    #  "[[Erik Demaine]] <br /> [[F. Thomson Leighton]]"
    curr_str = re.sub(r"<.*?br.*?/?>", ", ", curr_str)
    return purify_birth_place(curr_str)

def purify_nationality(curr_str):
    # "nationality": "American <br> Israeli",
    # "nationality": "[[Germans|German]]",
    # "nationality": "[[Greece|Greek]]-[[United States|American]]",
    # "nationality": "American <br> Israeli",
    # "nationality": "[[Image:Flag of the United States.svg|20px|]] [[United States]]",
    # {{Flagicon|Netherlands}} Dutch -> {{Flagicon
    curr_str = re.sub(r"\{\{.*?\}\}", "", curr_str)

    curr_str = re.sub(r"<.*?br.*?/?>", ", ", curr_str)
    return purify_birth_place(curr_str)

def purify_workplaces(curr_str):
    # "workplaces": "Thrive Financial, Inc.<br>[[Twitter Inc.]]<br>ZunaVision Inc.
    # "workplaces": "{{Unbulleted list |[[Carnegie Mellon University]] |[[Tartan Laboratories]] |[[Thinking Machines]] |[[Sun Microsystems]] |[[Oracle Corporation]]}}",",
    # "workplaces": "[[Hungarian Academy of Sciences]]<br>\n[[University of Rochester]] <br> [[Boston University]]",
    return purify_known_for(curr_str)



def purify_spouses(curr_str):
    if "{" in curr_str:
        ans=[]
        potential=curr_str.split("|")
        prev_token=None
        for curr_token in potential:
            if "marriage" in prev_token.lower():
                ans.append(purify_known_for(curr_token))
            prev_token=curr_token
        return ans          
    else:
        return purify_known_for(curr_str)


def purify_split_by_comma(arr):
    return [ x.lstrip().rstrip() for x in purify_known_for(arr, True)]

def purify_notable_students(arr):
    arr=purify_known_for(arr)
    arr=list(filter(lambda x:"researcher" not in x.lower(), arr))
    return arr


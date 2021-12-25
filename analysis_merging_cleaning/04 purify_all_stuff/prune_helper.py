import re
import json
import os
import sys
from copy import deepcopy
from test_names import *

def remove_url_and_crossref_dblp(whole_obj):

    '''! Removes url and crossref and updates ee to a more meaningful name
    '''

    # "ee": "https://doi.org/10.1145/3484266.3487389",
    #  "crossref": "conf/hotnets/2021",
    #   "url": "db/conf/hotnets/hotnets2021.html#BittmanSMSMBSA21"
    rem_arr=["url","crossref",'cite','cdrom']
    for curr_work in whole_obj['data']:

        for unlucky_attr in rem_arr:
            if unlucky_attr in curr_work:
                del curr_work[unlucky_attr]
        if "ee" in curr_work:
            curr_work['link_to_work']=deepcopy(curr_work['ee'])
            del curr_work['ee']
    return whole_obj

def handle_person_dob(whole_obj):
    '''! Takes the entire value corredponding to DOB
    It then checks for consistency.
    If consensus is reached, then it marks the attribute as reliable;
    else marks it as unreliable

    '''
    #  "data": [
    #                 {
    #                     "year": 1947,
    #                     "month": 5,
    #                     "day": 1
    #                 },
    #                 {
    #                     "year": 1943,
    #                     "month": 2,
    #                     "day": 5
    #                 },
    #                 {
    #                     "year": 1930,
    #                     "month": 8,
    #                     "day": 18
    #                 },
    #                 {
    #                     "year": 1936,
    #                     "month": 2,
    #                     "day": 10
    #                 },
    #                 {
    #                     "year": 1957,
    #                     "month": 6,
    #                     "day": 27
    #                 },
    #                 {
    #                     "year": 1994,
    #                     "month": 1,
    #                     "day": 31
    #                 },
    #                 {
    #                     "year": 1981,
    #                     "month": 5,
    #                     "day": 22
    #                 },
    #                 {
    #                     "year": 1984,
    #                     "month": 10,
    #                     "day": 17
    #                 }
    #             ],
    if type(whole_obj['data'])!=list:
        # only one source
        whole_obj["is_reliable"]=True
        return whole_obj
    is_reliable=True
    # multiple sources/attributes detectee

    sub_attrs=['year','month','day']
    ideal_obj={
        "year":None,
        "month":None,
        "day":None
    }

    # we know its a list
    for curr_obj in whole_obj['data']:
        for sub_part in sub_attrs:
            # no chance of opposing
            if curr_obj[sub_part]==None:
                continue
            else:
                if ideal_obj[sub_part]==None:
                    # blindly set
                    ideal_obj[sub_part]=curr_obj[sub_part]
                else:
                    if ideal_obj[sub_part]==curr_obj[sub_part]:
                        # all is consistent
                        pass
                    else:
                        # contradiction reached. Keep priority to earlier stored (FCFS)
                        is_reliable=False

    whole_obj['data']=deepcopy(ideal_obj)
    whole_obj['is_reliable']=is_reliable
    return whole_obj

def make_websites_consistent(entire_obj):
   
    num_sources=0
    arr1=[]
    arr2=[]
    if "associated_website" in entire_obj:
        if type(entire_obj["associated_website"]['data'])!=list:
            entire_obj["associated_website"]['data']=[entire_obj["associated_website"]['data']]
        arr1=deepcopy(entire_obj["associated_website"]['data'])
        del entire_obj["associated_website"]
        num_sources+=1

    if "gs_website" in entire_obj:
        if 'url' in entire_obj["gs_website"]['data']:
            if type(entire_obj["gs_website"]['data']['url'])!=list:
                entire_obj["gs_website"]['data']['url']=[entire_obj["gs_website"]['data']['url']]
            arr2=deepcopy(entire_obj["gs_website"]['data']['url'])
        del entire_obj["gs_website"]
        num_sources+=1
  
    
    final_arr=[]
    final_arr.extend(arr1)
    final_arr.extend(arr2)


    final_arr=[x.replace("{","") for x in final_arr]
    final_arr=[x.replace("}","") for x in final_arr]
    final_arr=[extract_urls(x) for x in final_arr]
    final_arr=[x.replace("http://","") for x in final_arr]
    final_arr=[x.replace("https://","") for x in final_arr]
    final_arr=list(set(final_arr))

    final_arr=list(filter(lambda x:x!="",final_arr))


    ####################
    # remove substrings

    # {'data': ['https://www.stephenwolfram.com/', 'http://www.stephenwolfram.com', 'http://www.stephenwolfram.com/'], 'num_sources': 1}
    now_arr=final_arr[:]
    final_arr=[]
    now_arr.sort(reverse=True)
    for curr_url in now_arr:
        found_else=False
        for other_url in final_arr:
            if curr_url in other_url:
                found_else=True
        if not found_else:
            final_arr.append(curr_url)


    ######################
    if num_sources!=0 and len(final_arr)>0:
        entire_obj["associated_website"]={'data':final_arr,'num_sources':num_sources}
    return entire_obj

def extract_urls(url):
    r = re.search(r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})",url)
    result = r.group(0) if r else ""
    return result

def make_awards_consistent(entire_obj):
    arr1=[]
    arr2=[]
    num_sources=0
    if "awards_received" in entire_obj:
        arr1=deepcopy(entire_obj['awards_received']['data'])
        del entire_obj['awards_received']
        num_sources+=1
    if "awards_as_per_research_com" in entire_obj:
        arr2=deepcopy(entire_obj["awards_as_per_research_com"]['data'])
        del entire_obj["awards_as_per_research_com"]
        num_sources+=1
    
    final_arr=[]
    final_arr.extend(arr1)
    final_arr.extend(arr2)

    final_arr=list(set(final_arr))
    if num_sources!=0 and len(final_arr)>0:
        entire_obj['awards_won_by_person']={'data':final_arr,'num_sources':num_sources}
    return entire_obj

def clean_mgp_data(curr_obj):
    bad_attrs=["descendants","id"]
    if 'students' in curr_obj:
        for curr_stu in curr_obj['students']:
            for unlucky_attr in bad_attrs:
                del curr_stu[unlucky_attr]
    return curr_obj

def proper_setup_employer_orgs(whole_obj):
    master_keys=["employer_orgs","affiliation (P1416)",
    "person_workplaces"
    ]

    final_arr=[]
    num_sources=0
    for curr_key in master_keys:
        if curr_key in whole_obj:
            num_sources+=1
            the_val=whole_obj[curr_key]['data']
            if type(the_val)!=list:
                the_val=[the_val]
            final_arr.extend(the_val)
            del whole_obj[curr_key]
    if final_arr==[]:
        return whole_obj
    # print(type(whole_obj))
    whole_obj['employer_orgs']={'data':deepcopy(final_arr),'num_sources':num_sources}
    return whole_obj


def prune_employer_orgs(arr,THRESHOLD=3):

    #     {'data': ['Allen Institute for Artificial Intelligence', 'University of Washington', 'Allen Institute for AI, United States'], 'num_sources': 2}
    # {'data': ['University of Texas at Austin', 'University of Texas at Austin, United States'], 'num_sources': 2}
    if type(arr)!=list:
        arr=[arr]

    # backup_arr=arr[:]
    # assume you got an array
    init_len=len(arr)
    arr=list(filter(lambda x:len(x)>1,arr))

    surely_done=[]

    for idx, curr_place in enumerate(arr):
        best_score=-1
        best_idx=-1
        for idx_find, master_place in enumerate(surely_done):
            their_score=fetch_num_tokens_matched(curr_place, master_place)
            if their_score>best_score:
                best_score=their_score
                best_idx=idx_find
        # decide whether to include or not
        if best_score>=THRESHOLD:
            master_place=surely_done[best_idx]
            # surely decide, not decide which of the 2 to keep
            # print(f"{curr_place} : {master_place} found same")
            if len(master_place)<len(curr_place):
                surely_done[best_idx]=curr_place
        else:
            surely_done.append(curr_place)

    surely_done=list(filter(lambda x:len(x)>1,surely_done))
    # if init_len!=0 and len(surely_done)==0:
    #     print("Backup is ", backup_arr)
    #     print("Sure is ", surely_done)

    return surely_done




def expose_mgp_data(whole_obj):

    # delete entire mgp thing
    if "mgp_data" not in whole_obj:
        return whole_obj

    master_val=deepcopy(whole_obj['mgp_data']['data'])

    master_dict={}

    if "dissertation" in master_val:
        master_dict['mgp_dissertation']=master_val['dissertation']
    
    if "students" in master_val:
        master_dict['mgp_students']=master_val['students']

    if "advisor" in master_val:
        master_dict['mgp_advisor']=master_val['advisor']['name']

    del whole_obj['mgp_data']
    for curr_key, curr_val in master_dict.items():
        whole_obj[curr_key]={'data':curr_val, 'num_sources':1}
    return whole_obj

def map_advisor(whole_obj):
    master_keys=["doctoral advisor(s)","mgp_advisor"]

    final_arr=[]
    num_sources=0
    for curr_key in master_keys:
        if curr_key in whole_obj:
            num_sources+=1
            the_val=whole_obj[curr_key]['data']
            if type(the_val)!=list:
                the_val=[the_val]
            final_arr.extend(the_val)
            del whole_obj[curr_key]
    if final_arr==[]:
        return whole_obj
    # print(type(whole_obj))

    final_arr=prune_employer_orgs(final_arr,THRESHOLD=2)
    whole_obj["doctoral advisor(s)"]={'data':deepcopy(final_arr),'num_sources':num_sources}
    return whole_obj

def map_students(whole_obj):
    if "mgp_students" not in whole_obj:
        return whole_obj

    final_arr=[]
    num_src=1
    final_arr=deepcopy(whole_obj['mgp_students']['data'])
    done_names=[x['name'] for x in final_arr]
    # print('done names is ', done_names)
    add_arr=[]
    if "person_doctoral_students" in whole_obj:
        num_src+=1
        if type(whole_obj["person_doctoral_students"]['data'])!=list:
            whole_obj["person_doctoral_students"]['data']=[whole_obj["person_doctoral_students"]['data']]
        for curr_p in whole_obj["person_doctoral_students"]['data']:
            # print("curr is ", curr_p)
            if curr_p==None or len(curr_p)<=2:
                continue
            best_score=-1
            for the_name in done_names:
                the_score=fetch_num_tokens_matched(curr_p, the_name)
                if the_score>best_score:
                    best_score=the_score
            if best_score<2:
                add_arr.append(curr_p)

    final_arr.extend(add_arr)
    whole_obj["person_doctoral_students"]={'data':final_arr,"num_sources":num_src}

    del whole_obj['mgp_students']

    return whole_obj


    

def map_spouse(whole_obj):
    key_name="person_spouse(s)"
    if key_name not in whole_obj:
        return whole_obj
    if type(whole_obj[key_name]['data'])!=list or len(whole_obj[key_name]['data'])==0:
        del whole_obj[key_name]
    return whole_obj

def merge_cats(master_keys_list, whole_obj):
    final_arr=[]
    main_key=master_keys_list[0]
    num_src=0
    for curr_key in master_keys_list:
        if curr_key in whole_obj:
            num_src+=1
            the_val=whole_obj[curr_key]['data']
            if type(the_val)!=list:
                the_val=[the_val]
            final_arr.extend(the_val)
            del whole_obj[curr_key]

    final_arr=prune_employer_orgs(final_arr)
    if main_key=="person_birth_place" and len(final_arr)>0:
        final_arr=[final_arr[0]]
    
    if len(final_arr)>0:
        whole_obj[main_key]={'data':final_arr, 'num_sources':num_src}
    return whole_obj

    
    

import os
import re
import sys

def purify_name(init_name):
    person_name=init_name[:]
    # person_name = re.sub('[^a-zA-Z.\d\s]', '', person_name)
    person_name=re.sub(r'[^a-zA-Z ]+', '', person_name)
    person_name=person_name.lower()
    person_name=person_name.rstrip()
    person_name=person_name.lstrip()
    return person_name

def fetch_tokens(init_name):
    # print(f"{purify_name(init_name)}:{init_name}")
    # print(f"{len(purify_name(init_name))}:{len(init_name)}")
    assert(purify_name(init_name)==init_name)
    tokens=init_name.split(" ")
    tokens=list(set(list(filter(lambda x:x!="", tokens))))

    # print(f"Returning for {init_name} as {tokens}")
    return tokens

def fetch_lst_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def fetch_num_tokens_matched(name_1, name_2):

    # print(f"names are {name_1} AND {name_2}")
    name_1=purify_name(name_1)
    name_2=purify_name(name_2)

    arr_1=fetch_tokens(name_1)
    arr_2=fetch_tokens(name_2)

    inter_arr=fetch_lst_intersection(arr_1, arr_2)

    num_common_tokens=len(inter_arr)

    # print("num common tokens is ", num_common_tokens)
    
    if ((num_common_tokens==len(arr_1)) or (num_common_tokens==len(arr_2))) and (num_common_tokens!=0):
        # print("inside")
        num_common_tokens=1000
        # sys.exit()

    # print("len is ", len(arr_1))
    # print("len is ", len(arr_2))
    # print("##############")
    return num_common_tokens

def fetch_best_score_of_name_with_arr(arr, name):
    all_scores=[fetch_num_tokens_matched(x, name) for x in arr]
    best_score=max(all_scores)
    return best_score


    
        


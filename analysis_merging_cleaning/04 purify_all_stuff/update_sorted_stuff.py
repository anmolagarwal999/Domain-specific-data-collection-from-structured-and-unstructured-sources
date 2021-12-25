#!/usr/bin/env python
# coding: utf-8

# ### The purpose of this notebook is to generate a sorted list of attributes to decide on final merging steps

# In[1]:


import json
import os
import sys
from copy import deepcopy


# In[3]:
def sort_stuff():

    FILE_PATH="./CNT_gs_viaf_dblp_wc_mgp_wikiquote_influ_semantic_research.json"
    with open(FILE_PATH, 'r') as fd:
        df=json.load(fd)


    # ### For each attribute, store a sample value also for analysis. Also, maintain a freq dict

    # In[4]:


    attr_freq=dict()
    sample_vals=dict()
    for curr_elem in df:
        
        for curr_key, curr_val in curr_elem.items():
            # if curr_key=="ire_wiki_id":
            #     print("yp")
            if curr_key in attr_freq:
                attr_freq[curr_key]+=1
                try:
                    if curr_val['num_sources']>sample_vals[curr_key]['num_sources']:
                        curr_val['num_sources']=sample_vals[curr_key]['num_sources']
                except:
                    # print(curr_key)
                    # print(curr_val)
                    # return
                    pass
            else:
                # print("Error is ", e)
                attr_freq[curr_key]=1
                sample_vals[curr_key]=deepcopy(curr_val)


    # In[5]:


    freq_arr=list(attr_freq.items())
    sorted_freq_arr=list(sorted(freq_arr, key=lambda x:-x[1]))
    # print(attr_freq)

    # In[6]:


    final_arr=[]
    for curr_elem in sorted_freq_arr:
        curr_dict={"attr_name":curr_elem[0], 'f':curr_elem[1], "sample_val":sample_vals[curr_elem[0]]}
        final_arr.append(deepcopy(curr_dict))


    # In[7]:


    with open("sample_and_freqs_for_attributes.json", 'w') as fd:
        json.dump(final_arr, fd, indent=4)


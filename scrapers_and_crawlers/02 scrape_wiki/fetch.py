#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import json
import wptools
from copy import deepcopy


# In[2]:





# In[3]:


with open("../EXTRA_NAMES_LIST.json",'r') as fd:
    curr_lines=json.load(fd)['extra_names']


# In[4]:





# In[5]:


df=[]
error_list=[]


# In[6]:


tot_elem=0
failure_cnt=0
inner_freq=dict()
newness=0

# going through all names scraped
for curr_name in curr_lines:
    tot_elem+=1
    
    # try to find a page for the "name"
    page = wptools.page(curr_name)
    #print(page)
    try:
        # fetch all keys
        ####################################
        page.get()
        curr_dict=deepcopy(page.data)
        #########################################
        ####################################
        page.get_more()
        for curr_key in page.data:
            if curr_key not in curr_dict:
                curr_dict[curr_key]=page.data[curr_key]
                #print("New key is ", curr_key)
                newness+=1
        #########################################
        for curr_key in curr_dict:
            if curr_key in inner_freq:
                inner_freq[curr_key]+=1
            else:
                inner_freq[curr_key]=1 
        curr_dict['ire_person_name']=curr_name
        df.append(deepcopy(curr_dict))
        
    except Exception as E:
        failure_cnt+=1
        error_list.append((curr_name, E))
        print("Exception is ",E)
        print("SOme error occured while finding ",curr_name)
    
    #take data backup at regular intervals
    if tot_elem%100==0:
        print("tot elem is ", tot_elem)
        with open("extra_wiki_all_data.json",'w') as fd:
            json.dump({'done_cnt':tot_elem, 'error_list':error_list,"failure_cnt":failure_cnt,'attr_freq':inner_freq,'data':df}, fd, indent=4)


# In[ ]:


tot_elem


# In[ ]:


with open("extra_wiki_all_data.json",'w') as fd:
            json.dump({'done_cnt':tot_elem, 'error_list':error_list,"failure_cnt":failure_cnt,'attr_freq':inner_freq,'data':df}, fd, indent=4)


# In[ ]:





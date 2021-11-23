#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.



#﻿Sample String : 'The quick Brow Fox'


# In[34]:


def sam_str(x):
    a={'UPPER_C':0,'LOWER_C':0}
    for i in x:
        if i.isupper():
            a['UPPER_C']+=1
        elif i.islower():
            a["LOWER_C"]+=1
        else:
            pass
    print ("No. of Upper case characters : ", a["UPPER_C"])
    print ("No. of Lower case Characters : ", a["LOWER_C"])
sam_str('The quick Brow Fox')
    


# In[ ]:





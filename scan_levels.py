#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import json
import re
import google_auth_write

Mission=[]
Level= set()

def construct(path, meta):
    #print(path, meta[:20])
    try:
        j = json.loads(meta)        
    except:
        print("json error: ", meta)
        return
    
    if 'type' in j:
        if j["type"] == "mission":
            extract = re.findall('\d+', path)
            if len(extract)>1:
                #print(extract[0])
                j["level"]=extract[0]
                Mission.append(j)
                Level.add(extract[0])                        
    
def scan_readme(file):
    #print('1', file)
    with open(file, encoding="utf-8") as f: lines = f.read()
    #print('2', lines[:50].replace('\n', '\\n'))
    extract = re.findall(r"\{.*\}", lines)
    if len(extract)>0:
        #print('3', "extract", type(extract[0]), len(extract), extract[0])
        construct(file, extract[0])   

def listdir(basepath):
    #print('a', basepath)
    with os.scandir(basepath) as entries:
        for entry in entries:
            fname = basepath+'/'+entry.name
            #print('b', fname)
            if entry.is_dir():
                if "Levels" in fname:
                    listdir(fname)
            elif str(entry.name).lower() == "readme.md":
                scan_readme(fname)
                
# List all subdirectories using scandir()
basepath = '.'
listdir(basepath)
#print(Level)
#print(Mission)

keys = set()
for le in Level:
    #print("Level:", le)
    for m in Mission:
        #if m["level"] == le: print(m)
        keys.update(m.keys())

keys = list(keys)
print(keys)
keys = ['level','type', 'id', 'description', 'target']
val = [keys]
for le in Level:
    for m in Mission:
        val2 = []
        if m["level"]==le:
            for i in range(len(keys)):
                val2.append(m.get(keys[i],""))
            val.append(val2)
google_auth_write.write_playbook(val)


# In[24]:


get_ipython().system('dir')


# In[8]:


Mission


# In[89]:


b


# In[ ]:





# In[6]:


print(basepath)


# In[ ]:





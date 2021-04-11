#!/usr/bin/env python
# coding: utf-8

import os
import json
import re
import google_auth_write

Mission=[]
Level= set()

def construct(path, meta):
    global Level, Mission
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
    global Level, Mission
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
                
def scanit():
    global Level, Mission
    Mission=[]
    Level= set()
    # List all subdirectories using scandir()
    basepath = '.'
    listdir(basepath)
    #print(Level)
    #print(Mission)

    allkeys = set()
    for le in Level:
        #print("Level:", le)
        for m in Mission:
            #if m["level"] == le: print(m)
            allkeys.update(m.keys())

    keys = ['order', 'type','level', 'id', 'description', 'target']
    print('before', allkeys)
    allkeys -= set(keys)
    print('after', allkeys)
    for x in allkeys: keys.append(x)
    val = []
    for le in Level:
        for m in Mission:
            val2 = []
            if m["level"]==le:
                for i in range(1,len(keys)):
                    val2.append(m.get(keys[i],""))
                #print(m.get(keys[2]), m.get(keys[3]))
                val2.insert(0, "%03d.%02d"%(int(m.get(keys[2])),int(m.get(keys[3]))))
                val.append(val2)
    val.sort()
    val.insert(0, keys)
    for x in val: del x[0]
    #print(val)
    return val

if __name__ == '__main__':
    val = scanit()
    google_auth_write.write_playbook(val)

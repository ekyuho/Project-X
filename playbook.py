#!/usr/bin/env python
# coding: utf-8

from flask import Flask, request
import re
import google_auth
import google_auth_write
import scan_levels
import sys
import json
app = Flask(__name__, static_url_path='')

import numpy as np
book={}

def read_playbook():
    global df, book
    
    table = google_auth.fetch_playbook()
    index = 0
    for items in table:
        # skip commented line
        if len(items)==0 or items[0]=='#' or (len(items)>2 and items[0]+items[1])=="": continue
        # confirm that it has right header line
        if index==0:
            if items[0]=='id' and items[1]=='subid' and items[2]=='description' and items[3]=='key' and items[4]=='value':
                index += 1
                continue
            else:
                print("playbook format broken")
                print(items)
                sys.exit()
        index += 1

        #print(items)
        if items[0] != "": id=items[0]
        if not id.isnumeric():
            print("id is not numeric: id={}".format(id))
            print("playbook format broken")
            sys.exit()
        subid=items[1]
        if not subid.isnumeric():
            print("subid is not numeric: id={}".format(id))
            print("playbook format broken")
            sys.exit()               

        #print("{} {}".format(id,subid), flush=True)
        if not id in book: book[id] = {}
        if not "description" in book[id]:
            book[id]["description"] = items[2] if len(items)>3 else ""
            book[id]["process"] = {}
        if len(items)>4: book[id]["process"][subid] = {"key":items[3], "value":items[4]}
        elif len(items)>3:  book[id]["process"][subid] = {"key":items[3]}

def mission2level(id, s):
    #some mapping algoritym
    return "2"

def account2mission(s):
    #system knows current mission in progress
    return "이미지 cropping"

def render(id, s):
    if s!=s: return s
    if "ACCOUNT" in s: return "이정인"
    elif "LEVEL" in s: return mission2level(id, s)
    elif "MISSION" in s: return account2mission(s)

    if "{INPUT:user_typing}" in s: s = s.replace("{INPUT:user_typing}","입력해주세요: <input type=text name=i1>")
    if "{SELECTION:INTEGER}" in s: s = s.replace("{SELECTION:INTEGER}", "숫자를 입력해 주세요 <input type=text name=i2>")
    elif "{SELECTION:make_selection_list_from_context}" in s: s = s.replace("{SELECTION:make_selection_list_from_context}", "System wil make a list: ")
    elif "SELECTION" in s: 
        extract = re.findall(r'\{SELECTION:"(.*)"\}', s)
        print("EXTRACT", extract)
        if len(extract)>0:
            s1 = ""
            for select in extract[0].split(','):
                s1 += "<input type=radio name='r1' value=%s>%s</option>"%(select, select)
        s = s1

    return s


def show(id):
    global book
    read_playbook()
    if id == "": 
        with open("playbook.html", encoding='utf-8') as f: s = f.read()
        return s

    s = '<H3>process {} {}</H3>'.format(id, book[id]["description"])
    for proc in book[id]["process"]:
        #print(id, book[id]['process'], proc, flush=True)
        b = book[id]["process"][proc]
        s += '<p> {} {}: {}'.format(proc, b.get("key",""), render(id, b.get("value","")))
        print(b, flush=True)
    s += "<p><input type=submit value='제출하기'>"
    print(s, flush=True)
    return(s)

#read_playbook()
#print(book, flush=True)

@app.route('/')
def hello1():
    return "hello"

@app.route('/scan')
def scan():
    val = scan_levels.scanit()
    google_auth_write.write_playbook(val)
    resp = ""
    for x in val:
        resp += "%s<br>"%(json.dumps(x, ensure_ascii=False))
    #print(resp)
    return resp

@app.route('/show')
def showit():
    id = request.args.get('id', "")
    print('id=', id, flush=True )
    return show(id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

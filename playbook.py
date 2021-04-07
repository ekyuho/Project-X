from flask import Flask
from flask import request
import re
app = Flask(__name__, static_url_path='')

import pandas as pd
import numpy as np
book={}

def read_playbook():
    global df, book
    book={}
    df = pd.read_csv('playbook.csv')
    print('read playbook', flush=True)
    for no,s in df.iterrows():
        if not np.isnan(s["id"]):
            id=str(int(s["id"]))
            subid=str(int(s["subid"]))
            print("{} {}".format(id,subid), flush=True)
            if not id in book: book[id] = {}
            if not "description" in book[id]:
                book[id]["description"] = s["description"]
                book[id]["process"] = {}
            book[id]["process"][subid] = {"key":s["key"], "value":s["value"]}

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
        with open("playbook.html") as f: s = f.read()
        return s

    s = '<H3>process {} {}</H3>'.format(id, book[id]["description"])
    for proc in book[id]["process"]:
        #print(id, book[id]['process'], proc, flush=True)
        b = book[id]["process"][proc]
        s += '<p> {} {}: {}'.format(proc, b["key"], render(id, b["value"]))
        print(b, flush=True)
    s += "<p><input type=submit value='제출하기'>"
    print(s, flush=True)
    return(s)

read_playbook()
print(book, flush=True)


@app.route('/')
def hello1():
    return "hello"

@app.route('/show')
def showit():
    id = request.args.get('id', "")
    print('id=', id, flush=True )
    return show(id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

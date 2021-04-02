from flask import Flask
from flask import request
app = Flask(__name__)

import pandas as pd
import numpy as np
df = pd.read_csv('playbook.csv')

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

    if "{INPUT:user_typing}" in s: s = s.replace("{INPUT:user_typing}", "please type input?(HTML input form) ")
    if "{SELECTION:INTEGER}" in s: s = s.replace("{SELECTION:INTEGER}", "please type integer?(HTML input form) ")
    elif "{SELECTION:make_selection_list_from_context}" in s: s = s.replace("{SELECTION:make_selection_list_from_context}", "System wil make a list: ")
    elif "SELECTION" in s: s = s.replace("SELECTION:", "하나를 고르세요 ")

    return s

book={}
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
print(book)

def show(id):
    s = ""
    if id == "":
        s += "<H2>평가 양식 메뉴M</H2>"
        s += "<UL>"
        for m in book:
            s += "<li><a href=./show?id={}>{}</a>".format(m, book[m]["description"])
        s += "</UL>"
        return s

    t = 'process {} {}'.format(id, book[id]["description"])
    print(t, flush=True)
    s += t
    for proc in book[id]["process"]:
        #print(id, book[id]['process'], proc, flush=True)
        b = book[id]["process"][proc]
        print(b, flush=True)
        t = '<p> {} {}: {}'.format(proc, b["key"], render(id, b["value"]))
        print(t, flush=True)
        s += t
    return(s)


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

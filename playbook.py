from flask import Flask
from flask import request
import re
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
    if id == "":
        s = '''
<H2>이노베이션 아카데미 평가 절차와 양식</H2>
<H3>미션수행완료에 따라 Evaluation 절차 진행</H3>
<a href=./show?id=10>1. 제일먼저 스스로 평가(self-postmortem)진행</a>
<p>
자기 평가를 마치면 자동으로 (시스템상 미리 설정되었거나 아니면 pop-up하여 입력하도록 한후) peer-reviewer(동료평가자)를 수신자로, 멘토를 Cc로 해서 통지가 전달된다.
<p>
<H4><a href=./show?id=11>2. 자기평가후 peer reviewer 들이 받아보는 양식</a></H4>
<p>
동료평가자들은 이러한 양식을 받고 평가헤 참여하거나 다른 평가자를 추천한다.
<p>
<H4><a href=./show?id=12>3. 자료를 기반으로 1차 평가를 실시 및 평가참여 수락</a></H4>
<p>
자료 기반으로 간단한 1차 평가를 하고나면 평가 수락이 된다.
<p>
멘토는 참관만 하고 Peer Review에 개입 하지는 않는다.
<p>
<p>
<i>Peer Review 진행(오프라인으로 모여서 세션 진행) </i>
<p>
<p>
<H4><a href=./show?id=21>11. Peer Review 세션 후 피평가자가 입력하는 양식</a></H4>
<p>
<H4><a href=./show?id=22>12. Peer Review 세션 후 Peer Reviewer가 입력하는 양식</a></H4>
<p>
미션들은 사전에 반드시 Peer Reviewer를 해야하는지, 몇개를 묶어서 해도 되는지 정해져 있어서 피평가자 본인이 선택할 수 있는 범위가 있다
<p>
마지막 미션은 사실은 레벨 평가를 위한 단계이다.
<p>
<H4><a href=./show?id=16>21. 래벨평가를 위한 스스로평가 (self-postmortem)</a></H4>
<p>
<H4><a href=./show?id=17>22. 래벨평가를 참여요청양식 </a></H4>
<p>
<H4><a href=./show?id=18>22. 래벨평가를 참여수락 양식 </a></H4>
<p>
<H4><a href=./show?id=18>26. 래벨평가 피평가자 작성양식 </a></H4>
<p>
<H4><a href=./show?id=18>27. 래벨평가 평가자 작성양식 </a></H4>
<p>
<H4><a href=./show?id=12>3. 자료를 기반으로 1차 평가를 실시 및 평가참여 수락</a></H4>
<p>
<H4><a href=./show?id=18>29. 래벨평가 멘토 작성양식 </a></H4>
<p>
<H4><a href=./show?id=101>101. 개인별 Dash Board </a></H4>

<p>
<br><a href=https://docs.google.com/spreadsheets/d/1HRpjR7VKiyH5NrL4f50IM1im6WrFGbs5g-i7tu1fJk0/edit#gid=0>Playbook 수정하기 </a>(실시간 수정은 아직 안됩니다)
<br><a href=https://github.com/ekyuho/Project-X/blob/main/playbook.py>Playbook Parsing 프로그램 보기 </a>
<br><a href=https://github.com/ekyuho/Project-X/blob/main/playbook.csv>현재 Active한 Playbook Metafile 보기</a>
        '''
        return s

    t = '<H3>process {} {}</H3>'.format(id, book[id]["description"])
    print(t, flush=True)
    s = t
    for proc in book[id]["process"]:
        #print(id, book[id]['process'], proc, flush=True)
        b = book[id]["process"][proc]
        print(b, flush=True)
        t = '<p> {} {}: {}'.format(proc, b["key"], render(id, b["value"]))
        print(t, flush=True)
        s += t
    s += "<p><input type=submit value='제출하기'>"
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

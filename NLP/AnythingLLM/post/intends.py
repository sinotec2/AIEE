#kuang@node01 /nas2/kuang/MyPrograms/query_anything
# cat intends.py
import json
import os,sys
import numpy as np
from pandas import *
from datetime import datetime, timedelta

def summ_eng06(summ):
    import json,subprocess
    if len(summ)>20000:summ=summ[:20000]
    cmd="curl -s -X POST http://eng06.sinotech-eng.com:3012/api/v1/workspace/intentions/chat \
    -H 'accept: application/json' -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer 89GQ4GY-Q7JMYQT-NPA87MX-56HF5KZ' JSON"
    prompt= f"以下是提問及答案的文字: {summ}"
    data = json.dumps({"message": prompt, "mode": "chat"})
    JSON = f" -d '{data}'"
    a=cmd.replace('JSON',JSON)
    result=subprocess.check_output(a,shell=True).decode('utf8')
    chats = json.loads(result)
    return chats['textResponse']

APIK="89GQ4GY-Q7JMYQT-NPA87MX-56HF5KZ"
msg="/nas2/kuang/MyPrograms/query_anything/msg.txt"
cmd="curl -s -X DIR  http://eng06.sinotech-eng.com:PORT/PATH \
-H 'accept: application/json' -H 'Content-Type: application/json' \
-H 'Authorization: Bearer APIK' JSON -o MSG"
chats_all=[]
for i in range(1,15):
    if i==12:continue
    port='30{:02d}'.format(i)
    PATH='api/v1/admin/workspace-chats'
    DIR="POST"
    cmd1=cmd.replace('PORT',port).replace('PATH',PATH).replace('APIK',APIK).replace('DIR',DIR).replace('MSG',msg)
    p=0
    result=0
    while True:
        JSON="-d \'{\"offset\": PAGE}\'".replace('PAGE',str(p))
        a=cmd1.replace('JSON',JSON)
        result=os.system(a)
        if result !=0: break
        with open(msg,'r') as f:
            chats = json.loads([i.strip('\n') for i in f][0])
        cts=chats['chats']
        if len(cts)==0:break
        cc=[]
        for c in cts:
            if 'kuang' in c['user']['username']:continue
            cc.append(c)
        chats_all+=cc
        p+=1
df=DataFrame({'prompt':[i['prompt'] for i in chats_all],'response':[json.loads(i['response'])['text'] for i in chats_all]})
num=[str(i) for i in range(10)]


ints=[]
for i in range(len(df)):
    a=str((df.prompt[i],df.response[i])).replace("'","").replace('\n','').replace('|','')
    ints.append(summ_eng06(a))
df['ints']=ints
for i in range(len(df)):
    s=df.ints[i]
    s2=s.replace(',',' ').replace('\n',' ').replace('.','')
    ss=[i for i in s2.split() if i in num]
    s=''.join(ss)
    df.loc[i,'ints']=s

a=df.loc[df.ints.map(lambda x: len(x)==0)]
for i in a.index:
    b=str((df.prompt[i],df.response[i]))
    if '計算' in b:
        df.loc[i,'ints']='5'+df.loc[i,'ints']
a=df.loc[df.ints.map(lambda x: len(x)==0)]
for i in a.index:
    b=str((df.prompt[i],df.response[i]))
    if '表格' in b or '|' in b:
        df.loc[i,'ints']='3'+df.loc[i,'ints']
a=df.loc[df.ints.map(lambda x: len(x)==0)]
for i in a.index:
    b=str((df.prompt[i],df.response[i]))
    if "噸/▒" in b:
        df.loc[i,'ints']='5'+df.loc[i,'ints']
    else:
        df.loc[i,'ints']='4'+df.loc[i,'ints']

a=df.loc[df.ints.map(lambda x: '3' != x[0])]
b=a.loc[a.prompt.map(lambda x: '表格' in x)]
for i in a.index:
    df.loc[i,'ints']='3'+df.loc[i,'ints']

ittn={
 '尋求幫助/支援(例如請求技術支援、客服協助等)': 0,
 '投訴反饋(例如反映問題、提出意見等)': 1,
 '推薦建議(例如尋求產品或服務推薦)': 2,
 '整理表格(例如歸納欄位與各列的標題、段落改成條列)': 3,
 '翻譯修正文章(例如將文章從一種語言翻譯到另一種語言,或修改文章內容. 處理公文、函文、心得報告等等)': 4,
 '計算換算(例如幫我算出...、找最大最小或平均值、進行單位換算等)': 5,
 '摘要重點(例如整理結論、給出標題等)': 6,
 '訪問網站(例如購買商品、閱讀網頁、查詢天氣、交通、營業時間等)': 7,
 '定義介紹(是甚麼?是誰?指出現名詞卻無任何其他指示)': 8,
 '法律徵詢見解(關鍵詞包括法律、法規、辦法、規範、標準、準則、細則等)': 9}
s=''
for j in range(len(df)):
    # 取得當前的字符序列
    chars = list(df.ints[j])
    # 根據字符的序位加權計數
    if len(chars) > 0:
        s += chars[0] * 3  # 第一個字符加權 3 次
    if len(chars) > 1:
        s += chars[1] * 2  # 第二個字符加權 2 次
    if len(chars) > 2:
        s += ''.join(chars[2:])  # 其餘字符原樣添加
for n in num:
    if n in itt2:
        print(n,s.count(str(n)),itt2[n])
dfr=DataFrame({'num':num,'itt':[itt2[n] for n in num],'count':[s.count(str(n)) for n in num ]})
dfr=dfr.sort_values('count',ascending=False)
dfr.to_csv('intents.csv',index=False)

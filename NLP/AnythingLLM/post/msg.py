#!/opt/anaconda3/bin/python
import json
import os,sys
import numpy as np
from pandas import *


def get_total_token_count(data):
    len_itm=len(data["localFiles"]["items"])
    return sum([sum(item['token_count_estimate'] for item in data["localFiles"]["items"][i]["items"]) for i in range(len_itm)])
def cmm(number):
    return '{:,}'.format(number)

def outp():
    with open('/nas2/kuang/MyPrograms/query_anything/grpsvr.json','r',encoding='utf8') as f:
        grps = json.load(f)
    ss=DataFrame({'grp':[i for i in grps],'num':[grps[i] for i in grps]})
    sgrp={int(i)-3000:j for i,j in zip(list(ss['num']),list(ss.grp))}
    sgrp.update({14:"小幫手"})
    ss=ss.sort_values('num')
    n=len(df)
    df['分組']=[sgrp[i] for i in list(df['分組'])]
    df.loc[n]=['合計']+list(df.sum().values)[1:]
    for c in col[1:]:
        df[c]=[cmm(i) for i in df[c]]
    print(df)
    df.to_csv('/nas2/VuePressDist/ICT/file.csv')

APIK="..."
msg="/nas2/kuang/MyPrograms/query_anything/msg.txt"
cmd="curl -s -X DIR  http://eng06.sinotech-eng.com:PORT/PATH \
-H 'accept: application/json' -H 'Content-Type: application/json' \
-H 'Authorization: Bearer APIK' JSON -o MSG"
col=['分組','對話次數','參與人數','文件詞組']
df=DataFrame({i:[] for i in col})
data=[]
for i in range(1,15):
    port='30{:02d}'.format(i)
    PATH='api/v1/admin/workspace-chats'
    DIR="POST"
    cmd1=cmd.replace('PORT',port).replace('PATH',PATH).replace('APIK',APIK).replace('DIR',DIR).replace('MSG',msg)
    p=0
    chats_all=[]
    result=0
    while True:
        JSON="-d \'{\"offset\": PAGE}\'".replace('PAGE',str(p))
        a=cmd1.replace('JSON',JSON)
        result=os.system(a)
        if result !=0: break
        with open(msg,'r') as f:
            chats = json.loads([i.strip('\n') for i in f][0])
        if len(chats['chats'])==0:break
        chats_all+=chats['chats']
        p+=1
    if result !=0: continue

    PATH='api/v1/documents'
    DIR="GET"
    JSON=''
    a=cmd.replace('PORT',port).replace('PATH',PATH).replace('APIK',APIK).replace('JSON',JSON).replace('DIR',DIR).replace('MSG',msg)
    result=os.system(a)
    with open(msg,'r') as f:
        docs = json.loads([i.strip('\n') for i in f][0])
    ntoken=0
    if len(docs)!=0:ntoken=get_total_token_count(docs)
    result=os.system(a)
    n=len(df)
    df.loc[n]=[i,len(chats_all),len(set([c['user']['username'] for c in chats_all])),ntoken]
if len(df)==0: sys.exit()
result=outp()

#kuang@node01 /nas2/kuang/MyPrograms/query_anything
# cat wc_usr.py
#!/opt/anaconda3/bin/python
import json
import os,sys,re
import numpy as np
from pandas import *
from datetime import datetime, timedelta


def get_total_token_count(data):
    len_itm=len(data["localFiles"]["items"])
    return sum([sum(item['token_count_estimate'] for item in data["localFiles"]["items"][i]["items"]) for i in range(len_itm)])
def cmm(number):
    return '{:,}'.format(number)

def count_mixed_characters(text):
    # 使用正則表達式匹配中文和英文字符
    chinese_pattern = re.compile(r'[\u4e00-\u9fa5]')  # 中文字符範圍
    english_words = re.findall(r'\b[a-zA-Z]+\b', text)  # 匹配完整的英文單詞

    # 初始化計數器
    chinese_count = len(re.findall(chinese_pattern, text))
    english_count = len(english_words)

    return chinese_count+english_count
def count_chinese_characters(text):
    # 使用正則表達式匹配中文和英文字符
    chinese_pattern = re.compile(r'[\u4e00-\u9fa5]')  # 中文字符範圍
    english_words = re.findall(r'\b[a-zA-Z]+\b', text)  # 匹配完整的英文單詞

    # 初始化計數器
    chinese_count = len(re.findall(chinese_pattern, text))
    english_count = len(english_words)

    return chinese_count


aln=read_csv('allname.csv')

em_nm={i:j for i,j in zip([k.split('@')[0] for k in aln.Email],list(aln.EmpName))}
em_nm.update({'kuang':"曠永銓"})
em_nm.update({'unknown user':"曠永銓"})
em_nm.update({'jyhua':"花建佑"})
em_nm.update({'sunshaopo':"孫紹博"})

em_dp={i:j for i,j in zip([k.split('@')[0] for k in aln.Email],list(aln.DeptName))}
em_dp.update({'kuang':"研發及資訊部"})
em_dp.update({'unknown user':"研發及資訊部"})
em_dp.update({'jyhua':"能資源設施部"})
em_dp.update({'sunshaopo':"環境規劃一部"})

APIK="89GQ4GY-Q7JMYQT-NPA87MX-56HF5KZ"
msg="/nas2/kuang/MyPrograms/query_anything/msg.txt"
cmd="curl -s -X DIR  http://eng06.sinotech-eng.com:PORT/PATH \
-H 'accept: application/json' -H 'Content-Type: application/json' \
-H 'Authorization: Bearer APIK' JSON -o MSG"
col=['分組','對話次數','參與人數','文件詞組']
df=DataFrame({i:[] for i in col})
chats_all=[]
for i in range(1,15):
    port='30{:02d}'.format(i)
    PATH='api/v1/admin/workspace-chats'
    DIR="POST"
    cmd1=cmd.replace('PORT',port).replace('PATH',PATH).replace('APIK',APIK).replace('DIR',DIR).replace('MSG',msg)
    p=0
    result=0
    chats_p=[]
    while True:
        JSON="-d \'{\"offset\": PAGE}\'".replace('PAGE',str(p))
        a=cmd1.replace('JSON',JSON)
        result=os.system(a)
        if result !=0: break
        with open(msg,'r') as f:
            chats = json.loads([i.strip('\n') for i in f][0])
        if len(chats['chats'])==0:break
        chats_p+=chats['chats']
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
    chats_all+=chats_p
users=list(set([c['user']['username'] for c in chats_all]))
wc=[np.mean([count_mixed_characters(c['prompt']) for  c in chats_all if c['user']['username']==u]) for u in users]
df=DataFrame({'wc':wc,'user':users})

df['EmpName']=df.user
a=list(df.loc[df.user.map(lambda x:count_chinese_characters(x)==0),'user'])
df.loc[df.user.map(lambda x:count_chinese_characters(x)==0),'EmpName']=[em_nm[i] for i in a]

df['DeptName']='水務部'
a=list(df.loc[df.user.map(lambda x:count_chinese_characters(x)==0),'user'])
df.loc[df.user.map(lambda x:count_chinese_characters(x)==0),'DeptName']=[em_dp[i] for i in a]
df.set_index('wc').to_csv('wc.csv')

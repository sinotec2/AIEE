 ---

layout: default
title: add_user.py
parent: Anything LLM
grand_parent: 自然語言處理
nav_order: 99
date: 2024-05-03
last_modified_date: 2024-05-07 11:58:34
tags: AI chat
---

# add_user.py程式說明
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>
---

## 背景

- 這裡討論的是批次新增AnythingLLM使用者。但要增加的是怎麼樣等級的使用者？
  - 內設一般只能對話諮詢的使用者：似乎與免費版的OpenAI沒有什麼差別，比免費版的Claud2還差，似乎對推廣GPT的使用沒有什麼幫助。
  - [經理](AnyChat_mng.md)等級的使用者：每個人都可以修改使用者的名稱權限、重複開設工作區、重複讀取檔案、API資源大幅消耗，這似乎是推廣必然的代價。
  - [管理者](AnyChat_adm.md)：（似乎沒有普設[管理者](AnyChat_adm.md)這個選項）
- 伺服器的考量
  - 基本上是個知識領域以及隱私權的分際
  - AnythingLLM並沒有單一伺服器服務人數的上限。
  - 同一個檔案轉檔的次數應該有個最佳h
- 要將每一個技術分組的使用者，分配到自己的GPT伺服器上，除了手動個別新增、以邀請連結新增、也可以使用API在後端以python程式輪番新增。
  - 手動新增：(不予評論)
  - 邀請連結：只能新增內定之無權限使用者，還需要手動將其身分提升至[經理](AnyChat_mng.md)等級，才能使用檔案及網頁的連結功能。
  - API程式：新增使用者，除了帳號、密碼之外，也可以指定身分(role)，一經給定，不必再手動修改。
- 帳密之考量
  - 帳號：使用email @左方的名稱，數字仍予以保留。帳號長度大於8碼者約35人，並不是很多，如果同仁想要修改可以自行修改。(仍會有IP追蹤)
  - 密碼：至少為8碼，此處以員編重複2次作為初設值
- 部門、技術組與伺服器的對應關係

### 對應關係表

|部門|技術組|英文簡稱|伺服器
-|-|-|-
環境規劃一部|環評組|EIA|[3001](http://eng06.sinotech-eng.com:3001)
環境規劃一部|風機組|Wind|[3002](http://eng06.sinotech-eng.com:3002)
環境規劃一部|空品組|Air|[3003](http://eng06.sinotech-eng.com:3003)
環境規劃一部|減碳組|Carbon|[3004](http://eng06.sinotech-eng.com:3004)
水務工程部|管線組|Pipeline|[3005](http://eng06.sinotech-eng.com:3005)
水務工程部|廠站組|Water|[3006](http://eng06.sinotech-eng.com:3006)
環境規劃二部|廢棄物組|Waste|[3007](http://eng06.sinotech-eng.com:3007)
環境規劃二部|土水組|Soil|[3008](http://eng06.sinotech-eng.com:3008)
能資源設施部|興建組|Construction|[3009](http://eng06.sinotech-eng.com:3009)
能資源設施部|營管組|Operation|[3010](http://eng06.sinotech-eng.com:3010)
能資源設施部|產業輔導組|Counseling|[3011](http://eng06.sinotech-eng.com:3011)
研發及資訊部|研資部|ICT|[3012](http://eng06.sinotech-eng.com:3012)
行政及支援部|行政部|Admin|[3013](http://eng06.sinotech-eng.com:3013)

## 程式說明

### 準備

- 將模板複製到每一個image的所屬目錄下
  - 以保持每一個image的API token都一致，這樣才能允許curl -XPOST造訪
  - 每個image都已經有既設的工作區與對應的GPT API keys
  - 每個image都必須在運轉的狀態，才會對API有所回應。
- 資料確認
  - 員編與Email的對應關係、可以參考公司員工分機網頁，更新到最新。
  - 員編與分組對應關係：洽分組技經確認，包括新進與離職的最新動態。
  - 無Email員工：不予啟用。

### 輸入檔

程式會讀取兩個 CSV 檔案與一個json檔案:

- allname.csv: 包含員工編號(EmpNo)和電子郵件名稱(EmailName)的對應關係。
- group.csv: 員工編號與群組名稱(組別名稱)的對照關係
- grpsvr.json：包含各個群組名稱(組別名稱)和對應的群組伺服器 Port 號。

### 大要

- 此程式的目的是自動建立新使用者帳號,並將使用者分配到對應的群組伺服器上。
- 使用pandas將csv讀進來
- 程式會遍歷每個群組,並為該群組中的每個員工建立新的使用者帳號。使用者名稱為電子郵件名稱,密碼為員工編號。
- 使用 curl 命令向 http://eng06.sinotech-eng.com:PORT/api/v1/admin/users/new 發送 POST 請求,建立新的使用者帳號。其中 PORT 會被替換為對應群組的伺服器 Port 號。
- 程式會將每個員工所屬的群組(grp)和群組伺服器(svr)資訊更新到 df 資料框中。
- 最後,程式會將包含員工編號(EmpNo)、員工名稱(EmpName)、部門名稱(DeptName)、電子郵件(Email)、所屬群組(grp)和群組伺服器(svr)的資訊,輸出到 grp_svr.csv 檔案中。

### cURL指令

- 指令
  - `POST`：因為是新增使用者，所有指令將會送到(`/admin/users/new`)，不必指定使用者id，系統會按照次序自行給定id值。
  - `-H`檔頭：需指定格式及金鑰
  - API金鑰：由[管理者](AnyChat_adm.md)產生，詳見[API Keys](./AnyChat_adm.md#api-keys)。為使程式設計方便，所有端口的API金鑰均保持一致。(先在某伺服器環境中產生，再複製到其他伺服器。)
- 網址
  - 固定部分：主機、網域及路徑，
  - 變數部分：各技術組分配之伺服器端口，由`3001`~`3013`(見[上表](#對應關係表))。
- 使用者設定json內容
  - 固定部分：角色(`role`)全設定為[經理](AnyChat_mng.md)。
  - 變數部分：名稱設為email名稱、密碼初設為員編2遍共8碼。
  
```bash
cmd="curl -X 'POST' \
   'http://eng06.sinotech-eng.com:PORT/api/v1/admin/users/new' \
   -H 'accept: application/json' \
   -H 'Authorization: Bearer ***' \
   -H 'Content-Type: application/json' \
   -d '{  \"username\":\"NAME\",\"password\":\"PASSWORD\",\"role\":\"manager\" }'"
```

- 注意
  - 指令中的雙引號需特別指定，不可忽略。
  - 變數部分：以字串之替代方式，在迴圈中進行疊代(`cmd.replace(...)`)。

### 迴圈

設計2層的迴圈
1. 各技術分組
2. 隸屬該技術組的成員

```python
eg={}
for g in grpsvr:
    dfi=dfg.loc[dfg['組別名稱']==g]
    for e in list(dfi.EmpNo):
        if int(e) not in EmpNo2EmailName:continue
        name=EmpNo2EmailName[int(e)]
        passwd=str(int(e))+str(int(e))
        a=cmd.replace('PORT',grpsvr[g]).replace("NAME",name).replace("PASSWORD",passwd)
        os.system(a)
        eg.update({int(e):g})
    print(g)
```

## 程式碼下載

{% include download.html content="將使用者分配到對應的群組伺服器` [add_user.py](./add_user.py)" %}
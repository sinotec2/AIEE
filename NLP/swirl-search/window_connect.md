---
layout: default
title: MS Window AD Connection
parent: swirl搜尋引擎
grand_parent: 自然語言處理
nav_order: 99
date: 2023-11-13
last_modified_date: 2023-11-13 19:18:56
has_children: true
tags: AI chat report
---

# MS Window AD Connection
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

## 遠端Linux上的swirl django 伺服器如何取得使用者AD訊息。

### Answer from GPT 3.5

  在遠端的 Linux 環境中，如果你的 Django 伺服器需要取得使用者 Active Directory（AD）訊息，你可以使用 LDAP（Lightweight Directory Access Protocol）協議與 AD 進行通信。這裡提供一個簡單的步驟：

1. **安裝 LDAP 相關套件：**
   確保你的 Django 環境中安裝了支援 LDAP 的相關套件，例如 `django-auth-ldap`。你可以使用 pip 安裝：

   ```bash
   pip install django-auth-ldap
   ```

2. **設定 Django settings：**
   在 Django 專案的 settings.py 中，加入 LDAP 相關的配置。請根據你的 AD 設定調整以下範例：

   ```python
   import ldap
   from django_auth_ldap.config import LDAPSearch, NestedActiveDirectoryGroupType

   AUTH_LDAP_SERVER_URI = "ldap://your-ad-server"
   AUTH_LDAP_BIND_DN = "CN=bind_user,CN=Users,DC=example,DC=com"
   AUTH_LDAP_BIND_PASSWORD = "your_bind_password"

   AUTH_LDAP_USER_SEARCH = LDAPSearch(
       "CN=Users,DC=example,DC=com",
       ldap.SCOPE_SUBTREE,
       "(sAMAccountName=%(user)s)"
   )

   AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
       "CN=Users,DC=example,DC=com",
       ldap.SCOPE_SUBTREE,
       "(objectClass=group)"
   )

   AUTH_LDAP_GROUP_TYPE = NestedActiveDirectoryGroupType(name_attr="cn")

   AUTH_LDAP_MIRROR_GROUPS = True
   ```

   注意：請替換示例中的 AD 伺服器 URI、綁定用戶 DN、綁定用戶密碼和搜索基礎等參數，以符合你的 AD 環境。

3. **同步資料庫：**
   在設定完 LDAP 相關配置後，執行 Django 的資料庫遷移命令以同步資料庫：

   ```bash
   python manage.py migrate
   ```

4. **測試連接：**
   使用 Django 的 shell 來測試 LDAP 連接是否正常：

   ```bash
   python manage.py shell
   ```

   在 shell 中執行以下命令：

   ```python
   from django_auth_ldap.backend import LDAPBackend
   ldap = LDAPBackend()
   user = ldap.populate_user("your_username")
   print(user)
   ```

   請替換 `"your_username"` 為實際的 AD 使用者名稱。

這樣配置後，Django 將能夠使用 LDAP 協議從 AD 中檢索使用者信息。確保網路連接到 AD 伺服器是正常的，並檢查你的 AD 網域和用戶搜尋基礎等參數是否正確。

### Answer  from  GpT4

您好！要在遠端Linux上的swirl django伺服器中取得使用者AD訊息，您需要使用Python的LDAP模塊。LDAP是一種協議，用於訪問和維護分散式目錄信息。您可以使用LDAP模塊來連接到Active Directory（AD）並檢索用戶信息。以下是一些參考資料，可以幫助您開始：

1. **Python LDAP**：這是一個Python LDAP客戶端庫，可以用於連接到LDAP目錄服務器，包括AD ¹.
2. **Python LDAP3**：這是另一個Python LDAP客戶端庫，支持Python 2和3，可以用於連接到LDAP目錄服務器，包括AD ².
3. **Python Active Directory**：這是一個Python庫，可以用於執行各種AD操作，例如驗證用戶，查找用戶，更改密碼等 ³.

希望這些資訊能對您有所幫助！

來源: 與 Bing 的交談， 2024/1/17
(1) Django 介紹 - 學習該如何開發 Web | MDN - MDN Web Docs. https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/Introduction.
(2) Visual Studio 中的了解 Django 教學課程步驟 1，Django 基本知識. https://learn.microsoft.com/zh-tw/visualstudio/python/learn-django-in-visual-studio-step-01-project-and-solution?view=vs-2022.
(3) 架設 Django 開發環境 - 學習該如何開發 Web | MDN. https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/development_environment.

### Answer from Claude2

 要在遠端Linux上的swirl django伺服器獲取使用者的AD(Active Directory)信息,可以採取以下方法:

1. 在django應用中安裝python-ldap套件,通過該套件與AD進行交互。

2. 配置LDAP認證後端:在settings.py中配置如下內容,指定AD server、基礎DN等信息。

```python
import ldap
from django_auth_ldap.config import LDAPSearch

AUTH_LDAP_SERVER_URI = "ldap://ad.example.com"
AUTH_LDAP_BIND_DN = "cn=django-agent,dc=example,dc=com" 
AUTH_LDAP_BIND_PASSWORD = "password"
AUTH_LDAP_USER_SEARCH = LDAPSearch("dc=example,dc=com", ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
```

3. 在views和模板中通過request.user來取得AD用户信息,如displayName、mail等。可以自定义django user模型來儲存更多属性。

4. 也可以考慮使用django-auth-adfs等專用於AD集成的第三方應用。

這樣django應用就可以方便地與AD集成,通過LDAP協議查詢和驗證用戶信息。



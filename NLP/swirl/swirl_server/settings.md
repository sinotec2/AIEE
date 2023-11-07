---
layout: default
title: setings.py
nav_order: 99
layout: default
grand_parent: swirl搜尋引擎
parent: swirl_server
date: 2023-11-04
last_modified_date: 2023-11-04 20:37:49
tags: AI chat report
---


# setings.py

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

- *setings.py有些內容是讀取環境變數、有些在程式內設定。*
```bash
$ cat .env
SECRET_KEY='...'
ALLOWED_HOSTS=devp,localhost,host.docker.internal,200.200.32.195
PROTOCOL=http
SWIRL_EXPLAIN=True
SQL_ENGINE=django.db.backends.sqlite3
SQL_DATABASE=db.sqlite3
SQL_USER=user
SQL_PASSWORD=password
SQL_HOST=localhost
SQL_PORT=5432
MICROSOFT_CLIENT_ID=''
MICROSOFT_CLIENT_SECRET=''
MICROSOFT_REDIRECT_URI=''
OPENAI_API_KEY='...'
```

- `ALLOWED_HOSTS`*的第一個名稱將會被令為*`HOSTNAME`

## 程式說明

這[程式](./settings.py)是一個 Django 設置文件，用於配置 Django Web 應用程序的各個方面。以下是文件中定義的一些重要設置及其用途：

### 基本路徑和環境變量

- **BASE_DIR**：項目的基礎目錄。
- **env**：環境變量幫助類的實例，用於從 `.env` 文件中獲取設置。

### 安全性和執行模式：

- **SECRET_KEY**：Django 的密鑰，用於加密。
- **DEBUG**：是否開啟調試模式。生產環境應該設為 `False`。
- **ALLOWED_HOSTS**：允許服務的主機名單。

### 應用程序和中間件設定：

- **INSTALLED_APPS**：安裝的應用程序列表。
- **MIDDLEWARE**：中間件列表，負責請求/響應處理流程中的各個階段。

### 資料庫配置：

- **DATABASES**：資料庫配置，包括引擎、名稱、用戶等。

### 國際化設定：

- **LANGUAGE_CODE** 和 **TIME_ZONE**：應用程序使用的語言和時區。

### 靜態文件設定：

- **STATIC_URL** 和 **STATIC_ROOT**：用於服務靜態文件（如 CSS、JavaScript、圖片等）。

### Celery 配置：
- **CELERY_BROKER_URL** 和 **CELERY_RESULT_BACKEND**：Celery 任務佇列的配置。
- **CELERY_BEAT_SCHEDULE**：周期性任務的計劃。

### 郵件設置：

- **EMAIL_BACKEND** 和相關設置：用於發送郵件的配置。

### Swirl 特定配置：

- **SWIRL_TIMEOUT**：Swirl 操作的超時設置。
- **SWIRL_SEARCH_FORM_URL**：Swirl 搜索表單的 URL 路徑。
- **OPENAI_API_KEY**：OpenAI API 的密鑰。

### 其他重要設置：
- **TEMPLATES**：Django 模板的配置。
- **WSGI_APPLICATION** 和 **ASGI_APPLICATION**：WSGI 和 ASGI 應用程序的路徑，用於同步和異步 Web 服務。
- **STATICFILES_DIRS** 和 **STATICFILES_FINDERS**：額外的靜態文件目錄和搜索器。
- **DEFAULT_AUTO_FIELD**：Django ORM 默認的主鍵字段類型。
- **CSRF_TRUSTED_ORIGINS**：CSRF 信任的原始域名單。

這份文件是根據生產環境的標準和最佳實踐來配置的。開發人員應該根據他們的需求和基礎設施進行調整。
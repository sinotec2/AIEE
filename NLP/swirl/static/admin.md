---
layout: default
title: admin
nav_order: 99
layout: default
grand_parent: swirl搜尋引擎
parent: static
date: 2023-11-04
last_modified_date: 2023-11-04 20:37:49
tags: AI chat report
---


# static/admin

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

*這個目錄下的檔案控制著admin界面的畫面與程式*

```bash
admin
├── css
│   ├── autocomplete.css
│   ├── base.css
│   ├── changelists.css
│   ├── dark_mode.css
│   ├── dashboard.css
│   ├── forms.css
│   ├── login.css
│   ├── nav_sidebar.css
│   ├── responsive.css
│   ├── responsive_rtl.css
│   ├── rtl.css
│   ├── vendor
│   │   └── select2
│   │       ├── LICENSE-SELECT2.md
│   │       ├── select2.css
│   │       └── select2.min.css
│   └── widgets.css
├── img
│   ├── calendar-icons.svg
│   ├── gis
│   │   ├── move_vertex_off.svg
│   │   └── move_vertex_on.svg
│   ├── icon-addlink.svg
│   ├── icon-alert.svg
│   ├── icon-calendar.svg
│   ├── icon-changelink.svg
│   ├── icon-clock.svg
│   ├── icon-deletelink.svg
│   ├── icon-no.svg
│   ├── icon-unknown-alt.svg
│   ├── icon-unknown.svg
│   ├── icon-viewlink.svg
│   ├── icon-yes.svg
│   ├── inline-delete.svg
│   ├── LICENSE
│   ├── README.txt
│   ├── search.svg
│   ├── selector-icons.svg
│   ├── sorting-icons.svg
│   ├── tooltag-add.svg
│   └── tooltag-arrowright.svg
└── js
    ├── actions.js
    ├── admin
    │   ├── DateTimeShortcuts.js
    │   └── RelatedObjectLookups.js
    ├── autocomplete.js
    ├── calendar.js
    ├── cancel.js
    ├── change_form.js
    ├── collapse.js
    ├── core.js
    ├── filters.js
    ├── inlines.js
    ├── jquery.init.js
    ├── nav_sidebar.js
    ├── popup_response.js
    ├── prepopulate_init.js
    ├── prepopulate.js
    ├── SelectBox.js
    ├── SelectFilter2.js
    ├── theme.js
    ├── urlify.js
    └── vendor
        ├── jquery
        │   ├── jquery.js
        │   ├── jquery.min.js
        │   └── LICENSE.txt
        ├── select2
        │   ├── i18n
        │   │   ├── af.js
        │   │   ├── ar.js
        │   │   ├── az.js
        │   │   ├── bg.js
        │   │   ├── bn.js
        │   │   ├── bs.js
        │   │   ├── ca.js
        │   │   ├── cs.js
        │   │   ├── da.js
        │   │   ├── de.js
        │   │   ├── dsb.js
        │   │   ├── el.js
        │   │   ├── en.js
        │   │   ├── es.js
        │   │   ├── et.js
        │   │   ├── eu.js
        │   │   ├── fa.js
        │   │   ├── fi.js
        │   │   ├── fr.js
        │   │   ├── gl.js
        │   │   ├── he.js
        │   │   ├── hi.js
        │   │   ├── hr.js
        │   │   ├── hsb.js
        │   │   ├── hu.js
        │   │   ├── hy.js
        │   │   ├── id.js
        │   │   ├── is.js
        │   │   ├── it.js
        │   │   ├── ja.js
        │   │   ├── ka.js
        │   │   ├── km.js
        │   │   ├── ko.js
        │   │   ├── lt.js
        │   │   ├── lv.js
        │   │   ├── mk.js
        │   │   ├── ms.js
        │   │   ├── nb.js
        │   │   ├── ne.js
        │   │   ├── nl.js
        │   │   ├── pl.js
        │   │   ├── ps.js
        │   │   ├── pt-BR.js
        │   │   ├── pt.js
        │   │   ├── ro.js
        │   │   ├── ru.js
        │   │   ├── sk.js
        │   │   ├── sl.js
        │   │   ├── sq.js
        │   │   ├── sr-Cyrl.js
        │   │   ├── sr.js
        │   │   ├── sv.js
        │   │   ├── th.js
        │   │   ├── tk.js
        │   │   ├── tr.js
        │   │   ├── uk.js
        │   │   ├── vi.js
        │   │   ├── zh-CN.js
        │   │   └── zh-TW.js
        │   ├── LICENSE.md
        │   ├── select2.full.js
        │   └── select2.full.min.js
        └── xregexp
            ├── LICENSE.txt
            ├── xregexp.js
            └── xregexp.min.js
```
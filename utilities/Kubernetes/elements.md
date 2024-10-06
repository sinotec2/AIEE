---
layout: default
title: Kubernetes之執行
parent: Kubernetes
grand_parent: Utilities
nav_order: 99
date: 2023-11-16
last_modified_date: 2023-11-16 04:50:52
tags: AI Kubernetes
---

# Kubernetes之執行
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


Kubernetes（通常簡稱為K8s）是一個用於自動部署、擴展和管理容器化應用程式的開源平台。 Kubernetes本身不處理檔案，而是專注於容器編排和應用程式的管理。 然而，Kubernetes可以與儲存系統集成，以處理應用程式的資料和檔案。

以下是Kubernetes中處理檔案的一些關鍵元件和方式：

1. **磁碟區（Volumes）**: Kubernetes支援磁碟區的概念，它可以將持久性儲存附加到Pod中。 這些磁碟區可以是雲端儲存、網路儲存（NFS、[Ceph](#ceph)等）或本機儲存。 卷可用於在Pod之間共用文件，儲存設定檔或將資料持久化到外部儲存中。

2. **ConfigMaps和Secrets**: ConfigMaps和Secrets是Kubernetes資源，用於儲存配置資訊和敏感數據，如API金鑰、密碼等。 它們可以在容器中掛載為檔案或環境變量，以供應用程式使用。

3. **持久性卷聲明（Persistent Volume Claims）**: 應用程式通常需要持久性存儲，如資料庫資料。 Kubernetes透過Persistent Volume Claims（PVCs）允許應用程式聲明對持久性儲存的需求。 管理員可以配置持久卷（PV）來滿足這些需求。

4. **StatefulSets**: 對於需要穩定的網路標識和持久性儲存的應用程序，可以使用StatefulSets。 它們確保Pod有穩定的主機名稱和有序的部署，對於分散式系統和資料庫等應用程式非常有用。

5. **儲存類別（StorageClass）**: 儲存類別是Kubernetes中用來動態分配持久卷的抽象。 它允許管理員定義不同類型的存儲，以供應用程式使用。

總而言之，Kubernetes提供了豐富的選項來處理應用程式的資料和文件，讓您可以靈活地滿足不同應用程式的需求。 這些功能使Kubernetes成為容器化應用程式管理的強大平台。

## 名詞解釋

### Ceph

[Ceph](https://ceph.io/en/)（又稱 Ceph Storage）是一個開源的分散式儲存系統，旨在提供高度可擴展性、高性能和高可用性的儲存解決方案。Ceph 最初由 Sage Weil 開發，現在是一個廣泛使用的項目，並由許多組織和企業支持和採用。以下是 Ceph 的一些主要特點和概念：

1. **分散式儲存：** Ceph 設計為分散式儲存系統，可以將數據分佈在多個節點上。這提高了可用性，因為數據冗余存儲在多個地方，並且可以容忍硬件故障。

2. **對象儲存：** Ceph 提供對象儲存功能，稱為 RADOS（Reliable Autonomic Distributed Object Store），它使用分散式架構來存儲和檢索對象。這使得 Ceph 適用於需要大規模和可擴展對象儲存的應用程序，如雲端儲存。

3. **區塊儲存和檔案儲存：** 除了對象儲存，Ceph 還提供區塊儲存（RBD）和檔案儲存（CephFS）功能。這使得 Ceph 適用於虛擬機器（VM）、容器、檔案共享等各種用途。

4. **自我修復和自動平衡：** Ceph 具有自動修復和平衡功能，當節點故障或新增節點時，它可以自動重新分配數據，以確保高可用性和性能。

5. **可擴展性：** Ceph 可以根據需要輕鬆擴展，並且可以在小型集群和大型數據中心之間實現一致的儲存管理。

6. **開源和社區支持：** Ceph 是一個開源項目，具有強大的社區支持和活躍的開發者生態系統。這意味著它持續發展，並且有許多支援工具和插件可供使用。

- 一次搞懂Ceph儲存架構與應用形式[(李宗翰2015-09-29發表)](https://www.ithome.com.tw/tech/98860)
- All-In-One Ceph by [Dennis Lee May 29, 2020](https://medium.com/@dennislee22/all-in-one-ceph-2552f336420e)
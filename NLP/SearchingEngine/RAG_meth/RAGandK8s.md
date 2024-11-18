---
layout: default
title: K8s 的應用
parent: RAG Methodologies
grand_parent: SearchingEngine
nav_order: 99
date: 2024-10-12 
last_modified_date: 2024-11-18 20:32:31
tags: AI chat report
---

# K8s 的應用
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

## 訓練階段7500個節點

- [openAI,2021](https://juejin.cn/post/7255230505409429559)

本文討論了 OpenAI 如何擴展其 Kubernetes 基礎設施以支援 7,500 個節點，重點是優化資源調度、網路管理和 API 伺服器。解決的主要挑戰包括 GPU 資源分配、並行作業的群組調度、高效檢查點、網路效能和 API 伺服器負載管理。他們使用 Azure 的 VMSS 等工具進行擴展，使用 Kubernetes 1.16 的 EndpointSlices 來提高效能，並解決了 Prometheus 監控問題。總的來說，Kubernetes 被證明是一個可擴展且靈活的平台，用於管理 GPT-3 和 DALL·E 等大型 AI 模型。

![](https://openai.com/index/scaling-kubernetes-to-7500-nodes/#unsolvedproblems%E3%80%82)

## 推論階段可服務人數

在 Kubernetes (K8S) 中部署 GPU 推理服務時，每個節點能夠服務的使用者數量取決於多個因素，包括 GPU 的規格、模型的複雜性、推理的時間要求以及使用者的並發需求。以下是影響 GPU 推理服務能力的幾個關鍵因素：

	1.	GPU 性能：高性能的 GPU（如 NVIDIA A100 或 V100）能夠處理更多的推理請求。相較於入門級 GPU（如 T4 或 GTX 系列），這些高端 GPU 擁有更多 CUDA 核心、內存和加速能力，能夠更好地支持大規模並發請求。
	2.	模型大小與複雜性：較大的模型（如 GPT-3、BERT 這類生成式模型）需要更多的計算資源。相比之下，較小的模型（如 ResNet）對 GPU 資源的要求較低。因此，複雜的模型會降低單一 GPU 能夠同時處理的請求數量。
	3.	推理延遲與吞吐量要求：如果應用需要實時回應（如聊天機器人或即時推薦系統），那麼每個使用者的推理請求需要佔用更多的資源。如果允許較高的延遲或批處理推理，則可以增加服務的使用者數量。
	4.	並發用戶量：對於需要低延遲響應的場景，可能每個 GPU 同時僅能支持 5 到 10 個並發請求；而對於批次推理的應用場景，這個數量可能會增加。
	5.	K8S 節點配置：Kubernetes 節點上的資源分配方式（如 GPU 資源分片）也會影響每個 GPU 能夠同時服務的請求數量。K8S 允許將 GPU 資源分配給不同的 Pod，因此你可以將 GPU 資源共享給多個容器，這樣能夠有效提升服務多個用戶的能力。

大約服務人數範圍：
在典型的商業應用中，使用高端 GPU（如 NVIDIA A100），每個 GPU 在低延遲要求下可同時處理 5-10 個使用者的推理請求。如果應用允許較高延遲或批量處理，這一數字可以提升到數十甚至上百個使用者。

## k8s架構

> 我的應用有好幾個docker一起服務，面對使用者的可能會需要複製很多套，但資料庫會需要共用，這樣在k8s的架構中要怎麼規劃?

在 Kubernetes (k8s) 中，你的應用架構有多個 Docker 容器服務和共用的資料庫，建議根據以下方式進行規劃：

---

## 1. **應用與資料庫的分離部署**
   - **應用服務**：將每個服務分別部署為獨立的 Deployment 或 StatefulSet，並通過 Horizontal Pod Autoscaler (HPA) 來實現自動伸縮，應對使用者流量的波動。
   - **資料庫服務**：資料庫通常作為獨立的 StatefulSet 部署，因為資料庫需要穩定的存儲和網路連線。

---

## 2. **網路架構**
   使用 Kubernetes 的 Service 來提供穩定的網路端點：
   - **應用服務之間的連線**：
     - 每個應用的 Pod 通過 ClusterIP 或 Headless Service 進行內部通信。
     - 如果需要對外提供服務，使用 LoadBalancer 或 NodePort。
   - **資料庫連線**：
     - 建立一個 ClusterIP Service，為資料庫提供穩定的內部存取點。
     - 範例：
       ```yaml
       apiVersion: v1
       kind: Service
       metadata:
         name: database-service
       spec:
         selector:
           app: database
         ports:
           - protocol: TCP
             port: 3306
             targetPort: 3306
       ```

---

## 3. **資料持久化**
   資料庫需要使用 PersistentVolume (PV) 和 PersistentVolumeClaim (PVC) 來確保數據持久化。
   - 使用共用的 NAS 或分散式存儲系統（例如 Ceph、GlusterFS）。
   - 範例：
     ```yaml
     apiVersion: v1
     kind: PersistentVolume
     metadata:
       name: database-pv
     spec:
       capacity:
         storage: 50Gi
       accessModes:
         - ReadWriteOnce
       nfs:
         path: /data/db
         server: 192.168.1.10
     ---
     apiVersion: v1
     kind: PersistentVolumeClaim
     metadata:
       name: database-pvc
     spec:
       accessModes:
         - ReadWriteOnce
       resources:
         requests:
           storage: 50Gi
     ```

---

## 4. **資源管理與伸縮**
   - **應用服務**：
     - 設置資源限制，避免 Pod 過度佔用節點資源。
     - 開啟 HPA，根據 CPU 或流量自動調整 Pod 數量。
       ```yaml
       apiVersion: autoscaling/v2
       kind: HorizontalPodAutoscaler
       metadata:
         name: app-hpa
       spec:
         scaleTargetRef:
           apiVersion: apps/v1
           kind: Deployment
           name: app-deployment
         minReplicas: 2
         maxReplicas: 10
         metrics:
           - type: Resource
             resource:
               name: cpu
               targetAverageUtilization: 50
       ```

   - **資料庫**：
     - 資料庫不建議使用 HPA，因為數據一致性和資料恢復比較複雜。
     - 如果需要高可用，考慮使用主從複製（如 MariaDB 的 Galera Cluster 或 MySQL 的 Replication）。

---

## 5. **應用配置與環境變數管理**
   - 將資料庫連線資訊存入 Kubernetes 的 ConfigMap 或 Secret：
     ```yaml
     apiVersion: v1
     kind: ConfigMap
     metadata:
       name: db-config
     data:
       DB_HOST: database-service
       DB_PORT: "3306"
     ---
     apiVersion: v1
     kind: Secret
     metadata:
       name: db-secret
     type: Opaque
     data:
       DB_USER: bXl1c2Vy  # base64編碼
       DB_PASSWORD: cGFzc3dvcmQ=  # base64編碼
     ```

   - 在 Deployment 中引用：
     ```yaml
     env:
       - name: DB_HOST
         valueFrom:
           configMapKeyRef:
             name: db-config
             key: DB_HOST
       - name: DB_USER
         valueFrom:
           secretKeyRef:
             name: db-secret
             key: DB_USER
       - name: DB_PASSWORD
         valueFrom:
           secretKeyRef:
             name: db-secret
             key: DB_PASSWORD
     ```

---

## 6. **監控與日誌**
   - 部署監控工具（如 Prometheus 和 Grafana）來觀察應用服務和資料庫的資源使用情況。
   - 日誌採集（如 ELK 或 Loki）用於記錄和分析應用和資料庫的操作。

---

## 總結
### 規劃建議：
1. **應用服務**獨立部署並允許自動伸縮。
2. **資料庫服務**使用 StatefulSet 部署，並綁定 NAS 等持久存儲。
3. 設定內部 ClusterIP 服務進行通信，並用 PVC 確保數據持久化。
4. 為應用與資料庫定義資源限制，避免單個服務佔用過多資源。

這樣的架構既能應對高負載，又能保持數據的一致性與穩定性。

# # 記帳應用專案



## 專案簡介
這是 GDG on Campus NCU 和 cloud infra lab社群合作的 docker 和 K8s 社課所使用的範例檔案。

這是一個基於 Nuxt3 和 FastAPI 的記帳應用程式，使用 PostgreSQL 作為資料庫。前端使用 Nuxt3 框架，後端使用 FastAPI 框架，並透過 Docker 和 Docker Compose 進行容器化管理。

## 專案架構
- 前端：Nuxt3
- 後端：FastAPI
- 資料庫：PostgreSQL
- 容器化：Docker, Docker Compose

## 安裝與執行步驟

### 前置需求
你需要確保電腦安裝好了以下:
- Unix-like 系統（例如：Linux、macOS、WSL2 等）
- Docker
- Docker Compose


### 安裝步驟
1. clone 專案到本地端
    ```bash
    git clone https://github.com/your-repo/accounting_app_separating.git
    cd accounting_app_separating
    ```

2. 建立並啟動容器
    ```bash
    docker-compose up -d
    ```

3. 確認服務是否啟動成功
    - 前端應用程式應該可以透過 `http://localhost:3000` 訪問
    - 後端 API 應該可以透過 `http://localhost:8000/docs` 訪問
    - PostgreSQL 資料庫應該可以透過 `http://localhost:5432` 訪問

### 關閉容器

 若不想用 GUI 介面，而是透過指令來關閉正在運行的容器，可以按照以下步驟：

1. 在專案目錄中打開終端機。
2. 執行以下指令來停止並移除容器：
      ```bash
      docker-compose down
      ```
      若只希望暫時停止容器，可以使用：
      ```bash
      docker-compose stop
      ```
3. 使用以下命令確認容器已經停止：
      ```bash
      docker ps
      ```
      此命令應不再顯示目標容器。

    這樣即可安全地關閉所有服務容器。

## 環境變數設定
在 [docker-compose.yaml](http://_vscodecontentref_/1) 中已經設定好環境變數：
- `POSTGRES_USER`: 資料庫使用者名稱
- `POSTGRES_PASSWORD`: 資料庫密碼
- `POSTGRES_DB`: 資料庫名稱
- `DATABASE_URL`: 後端連接資料庫的 URL

## 使用說明
1. 前端應用程式：
    - 訪問 `http://localhost:3000` 查看前端應用程式
    - 根據路由導航到不同頁面

2. 後端 API：
    - 訪問 `http://localhost:8000/docs` 查看 API 文件
    - 使用 Postman 或其他工具測試 API

## 常見問題
- 如果遇到權限問題，請確保 Docker 和 Docker Compose 已正確安裝，並且當前使用者具有執行 Docker 的權限。
- 如果遇到資料庫連接問題，請檢查 [docker-compose.yaml](http://_vscodecontentref_/2) 中的環境變數設定是否正確。


## Docker Hub Image 連結補充

如果你希望直接從 Docker Hub 取得最新的鏡像，請參考以下連結：

- 前端: https://hub.docker.com/r/sunset513/accounting_app_separating-frontend
- 後端 : https://hub.docker.com/r/sunset513/accounting_app_separating-backend

你可以使用以下指令拉取鏡像：
```bash
docker pull sunset513/accounting_app_separating-backend
docker pull sunset513/accounting_app_separating-frontend
```
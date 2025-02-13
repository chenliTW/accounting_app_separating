# 透過官方的 node:lts-alpine 底鏡像
FROM node:lts-alpine

# 設定工作目錄
WORKDIR /app/frontend/

# 透過 npm 安裝 PNPM
RUN npm install -g pnpm

# 執行 pnpm install 安裝相依套件，並且 pnpm run dev 啟動開發伺服器
CMD pnpm install && pnpm run dev

# 開放 3000 連接埠
EXPOSE 3000
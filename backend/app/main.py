from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes
from app.models.account import Base
from app.database import engine

app = FastAPI(
    title="Accounting App API",
    description="API for Accounting App using FastAPI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 加入 CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 或使用 ["*"] 允許所有來源（開發時可用，生產環境建議指定）
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 建立資料表 (開發環境用，正式環境建議使用 migration 工具)
Base.metadata.create_all(bind=engine)

# 掛載 API 路由
app.include_router(routes.router, prefix="/api")

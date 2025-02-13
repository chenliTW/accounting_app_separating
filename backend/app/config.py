import os

# 使用環境變數設定連線字串，若未設定則使用預設值
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://your_user:your_password@localhost:5432/your_database"
)

# 如果你使用 SQLAlchemy，可進一步設定 SQLAlchemy 的參數：
SQLALCHEMY_DATABASE_URL = DATABASE_URL

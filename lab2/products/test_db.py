from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:6432/products"  # или тот путь, что у тебя
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

try:
    db = SessionLocal()
    print("✅ Соединение с БД успешно!")
except Exception as e:
    print("❌ Ошибка подключения к БД:", e)
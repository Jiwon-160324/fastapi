from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


# 데이터베이스와의 연결 생성
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 데이터베이스 작업을 위한 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 모델을 정의할 때 사용할 기본 클래스를 생성
Base = declarative_base()

# 데이터베이스 세션을 제공하는 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# # 데이터베이스에 연결
# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='password123', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Successfully connected to database!")
#         break
#     except Exception as error:
#         print("Failed to connect to database")
#         print("Error: ", error)
#         time.sleep(2)

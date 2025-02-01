from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# import contextlib # 의존성 주입 -> fastAPI는 제네레이터 기반 함수를 직접 지원하며 자동으로 리소스 관리를 처리
                    # 따라서, @contextlib.contextmanager를 사용하면 get_db 함수가 contextlib._GeneratorContextManager 객체를 반환하여 
                    # FastAPI의 종속성 주입이 제대로 작동하지 않는다.

# 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

# create_engine : 커넥션 풀을 생성
# 커넥션 풀은 데이터베이스에 접속하는 객체를 일정 갯수만큼 만들어 놓고 돌려가며 사용하는 것
# 데이터 베이스에 접속하는 세션 수를 제어하고, 또 세션 접속에 소요 되는 시간을 줄임
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}
)

# 데이터베이스에 접속하기 위해 필요한 클래스
# autocommit = False : 데이터를 변경했을 때 commit을 해야 실제 저장이 됨
# autocommit = True : commit이 없어도 즉시 데이터베이스에 변경사항이 적용되나, rollback이 없다.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# @contextlib.contextmanager # with문과 함께 사용할 수 있다.
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close() # 사용한 세션을 컨넥션 풀에 반환
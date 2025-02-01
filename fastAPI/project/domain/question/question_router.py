from fastapi import APIRouter

# 의존성 주입
from fastapi import Depends 
from sqlalchemy.orm import Session

from database import get_db
from domain.question import question_schema, question_crud
from models import Question

router = APIRouter(
    prefix="/api/question",
)


# 라우팅이란 FastAPI가 요청받은 URL을 해석하여 그에 맞는 함수를 실행하여 그 결과를 리턴하는 행위를 말한다.

# @router.get("/list")
# def question_list():
#     with get_db() as db: # with 문 활용 의존성 주입, with문을 벗어나는 순간 db.close()가 실행
#         _question_list = db.query(Question).order_by(Question.create_base.desc()).all() 
#     return _question_list

@router.get("/list", response_model=list[question_schema.Question]) # question_list 함수의 리턴값은 Question 스키마로 구성된 리스트이다.
def question_list(db: Session = Depends(get_db)): # Depends는 매개변수로 전달받은 함수를 호출하여 그 결과를 리턴
    _question_list = question_crud.get_question_list(db)
    return _question_list
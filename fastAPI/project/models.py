from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Question(Base): # database.py에서 정의한 Base 클래스를 상속
    __tablename__ = "question" # 모델에 의해 관리되는 테이블의 이름

    id = Column(Integer, primary_key=True) # 고유 번호처럼 숫자값에 사용, 중복값을 허용하지 않음.
    subject = Column(String, primary_key=False) # 제목처럼 글자 수가 제한된 텍스트에 사용
    content = Column(Text, primary_key=False) # 글 내용처럼 글자 수 제한이 없는 텍스트에 사용
    create_base = Column(DateTime, nullable=False) # 작성 일시, null값을 허용하지 않음.

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_base = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id")) # 답변과 질문을 연결하기 위해 외부 키 사용
    question = relationship("Question", backref="answers") # 답변 모델에서 질문 모델을 참조
                                                           # answer.question.subject처럼 참조할 수 있다.
                                                           # backref는 역참조 설정이다.  
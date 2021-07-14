from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db.base import Base, User, Writer, SnsAccount, BankingInfo, Novel, NovelNotice, Paragraph, Series  # noqa: F401
from app.db.session import engine, SessionLocal
import time

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    #     engine.execute(tbl.delete())

    # # DB 다시 만들때 이부분 돌리기
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    # if not user:
    #     user_in = schemas.UserCreate(
    #         email=settings.FIRST_SUPERUSER,
    #         password=settings.FIRST_SUPERUSER_PASSWORD,
    #         is_superuser=True,
    #     )
    #     user = crud.user.create(db, obj_in=user_in)  # noqa: F841
    # pass


if __name__ == "__main__":
    def create_tag(db: Session, create_field: dict):
        return crud.other_novel.create(db=db, obj_in=create_field)

    lst = [
        'BJGMNN',
        'TEMBBAL',
        'SOLOLVUP',
        'MISTERYCLUB',
        'GOLDENGLOVE',
        'GINISCOUTER',
        'MEDICALHS',
        'MAKDRAMAKING',
        'CHAEBOLCHILD',
        'JHHH',
        'KWMJ',
        'JSJ',
        'HAREMBOYS',
        'TSJL',
        'DBZGS',
        'KBSWHY',
        'NNFCOM',
        'JJZREADER',
        'TOPMNG'
    ]
    db = SessionLocal()
    [create_tag(db=db, create_field={'code': tag}) for tag in lst]

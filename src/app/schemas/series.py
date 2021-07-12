from typing import Optional, List, Dict

from pydantic import BaseModel

from .paragraph import Paragraph

'''
basic series metadata schema class
'''


# Shared properties
class SeriesMetaBase(BaseModel):
    title: str
    description: Optional[str] = ""
    language_code: str


# Properties to Create via API
class SeriesMetaCreate(SeriesMetaBase):
    pass


# Properties to Update via API
class SeriesMetaUpdate(SeriesMetaBase):
    id: int
    series_id: int


# Properties of API Response
class SeriesMeta(SeriesMetaBase):
    is_origin: bool

    class Config:
        orm_mode = True


'''
basic series status management schema class
'''


# Shared properties
class SeriesStatusBase(BaseModel):
    series_id: int
    manager_id: Optional[int]
    status: str = "UNAPPROVED"
    reason: str = "PRIVATE_ABUSE"


# Properties to Create via API
class SeriesStatusCreate(SeriesStatusBase):
    pass


# Properties to Update via API
class SeriesStatusUpdate(SeriesStatusCreate):
    pass


# Properties of API Response
class SeriesStatus(SeriesStatusBase):
    pass

    class Config:
        orm_mode = True


'''
basic series schema class
'''


# Shared properties
class SeriesBase(BaseModel):
    is_completed: Optional[bool] = False


# Properties to Create via API
class SeriesCreate(SeriesBase):
    title: str
    paragraph: list
    description: Optional[str] = ""


# Properties to Update via API
class SeriesUpdate(SeriesBase):
    id: int
    series_id: int
    title: str
    paragraph: dict
    description: str = ""


# Properties of API Response
class Series(SeriesBase):
    novel_id: int
    id: int
    order_number: int
    status: str
    paragraph: List[Paragraph]
    series_meta: Optional[List[SeriesMeta]]

    class Config:
        orm_mode = True
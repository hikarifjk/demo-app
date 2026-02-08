from typing import Optional

from pydantic import BaseModel, Field, ConfigDict



class TaskBase(BaseModel):

    # title: Optional[str] = Field(None,example="クリーニングを取りに行く")
    title: Optional[str] = Field(
        None,
        json_schema_extra={"example": "クリーニングを取りに行く"})


class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    #class Config:
        # orm_mode = True
    model_config = ConfigDict(from_attributes=True)

class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    # class Config:
        # orm_mode = True
    model_config = ConfigDict(from_attributes=True)




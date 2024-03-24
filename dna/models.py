from datetime import datetime
from enum import Enum
from typing import List, Optional

from humps import camelize
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int]
    benchling_id: str
    name: str
    handle: str

    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class DNASequence(BaseModel):
    id: Optional[int]
    benchling_id: str
    name: str
    created_at: datetime
    bases: str
    creator: Optional[User]

    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class DNASequenceList(BaseModel):
    __root__: List[DNASequence]


class Status(str, Enum):
    COMPLETED = "completed"
    INITIATED = "initiated"
    FAILED = "failed"


class DNABatchResponse(BaseModel):
    id: int


class DNABatchStatus(BaseModel):
    status: Status

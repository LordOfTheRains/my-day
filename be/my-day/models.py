from enum import Enum
from typing_extensions import Literal
from pydantic import BaseModel
from typing import Optional, List, Union

class ObligationType(Enum):
  Event = "Event"
  Chore = "Chore"

class Event(BaseModel):
  id: int
  obligation_type: ObligationType = ObligationType.Event
  name: str
  description: Optional[str]
    
class Chore(BaseModel):
  id: int
  obligation_type: ObligationType = ObligationType.Chore
  name: str
  description: Optional[str]
  duration: float

class Person(BaseModel):
  id: int
  name: str
  obligations: List[Union[Chore, Event]]

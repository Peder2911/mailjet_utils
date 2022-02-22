
from typing import List, Optional, Dict
import pydantic

class Contact(pydantic.BaseModel):
    Email: pydantic.EmailStr
    Name:  str
    Variables:        Optional[Dict[str,str]] = None

class Message(pydantic.BaseModel):
    From:             Contact
    To:               List[Contact]
    Subject:          str
    TextPart:         str
    HTMLPart:         str


class SendData(pydantic.BaseModel):
    Messages: List[Message]

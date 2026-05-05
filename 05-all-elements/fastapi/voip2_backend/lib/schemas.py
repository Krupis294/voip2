from pydantic import BaseModel

class ManagedCall(BaseModel):
 from_ext: str
 to_ext: str

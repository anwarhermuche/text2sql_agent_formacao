from pydantic import BaseModel, Field
from typing import List

class CheckerAgentResponse(BaseModel):
    cot: List[str] = Field(description = "Cadeia de pensamento para ver se a query é maliciosa ou não")
    malicioso: bool = Field(description = "Se a query é maliciosa (contém DELETE, UPDATE, CREATE etc.) ou não.")
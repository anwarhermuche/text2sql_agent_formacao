from pydantic import BaseModel, Field
from typing import List

class SQLAgentResponse(BaseModel):
    cot: List[str] = Field(description = "Cadeia de pensamento para montar a query SQL (se aplicável)")
    sql: str = Field(description = "Query SQL gerada. Se não houver query, retornar string vazia")
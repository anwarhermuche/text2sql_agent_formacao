from pydantic import BaseModel, Field
from typing import List

class DBAAgentResponse(BaseModel):
    cot: List[str] = Field(description = "Cadeia de pensamento para ver se responde à pergunta do usuário ou não.")
    makes_sense: bool = Field(description = "Se os dados retornados respondem à pergunta do usuário ou não.")
    feedback: str = Field(description = "Feedback da query para um profissional responsável por criar queries SQL melhorar caso a resposta não responda à pergunta do usuário. Se tudo fizer sentido, retorne uma string vazia")
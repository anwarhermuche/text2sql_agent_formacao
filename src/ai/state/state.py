from typing_extensions import TypedDict, Annotated
from typing import List
from langchain_core.messages import AnyMessage

class State(TypedDict):
    query: str
    sql: str
    history: List[AnyMessage]
    schema: str
    malicioso: Annotated[bool, "Se a query é maliciosa (contém DELETE, UPDATE, CREATE etc.)"]
    recursion_limit: int
    query_result: str
    makes_sense: bool
    feedback: str
    resposta: str

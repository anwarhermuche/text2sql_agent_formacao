from src.ai.graph.graph import graph
from src.utils.get_schema import SchemaExtractor

schema_extractor = SchemaExtractor()
config = {"configurable": {"thread_id": "teste123"}}
entrada = {
    "query": "",
    "history": [],
    "sql": "",
    "schema": schema_extractor.extract_schema(),
    "query_result": "",
    "recursion_limit": 0,
    "makes_sense": False,
    "feedback": "",
    "resposta": ""
}

print(f"Marcelo: Olá!. Tudo bem? Como posso ajudar?")
k = 0
while True:
  mensagem_usuario = input("Usuário: ")
  if k == 0:
    entrada["query"] = mensagem_usuario
    input_graph = entrada
  else:
    input_graph = {"query": mensagem_usuario}

  for output in graph.stream(input_graph, config=config):
    for key, value in output.items():
        print(f"{key}: {value}")

  resposta = value['resposta']
  print("Marcelo: " + resposta)
  k += 1
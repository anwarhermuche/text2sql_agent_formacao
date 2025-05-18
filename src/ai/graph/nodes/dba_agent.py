from langchain_core.prompts import ChatPromptTemplate
from src.ai.structured_outputs.dba_agent_response import DBAAgentResponse
from src.ai.state.state import State

class DBAAgent:

    def __init__(self, prompt_path: str, llm):
        self.__prompt = self.__get_prompt(prompt_path)
        self.__llm = llm.with_structured_output(DBAAgentResponse)

    def __get_prompt(self, prompt_path: str) -> str:
        with open(prompt_path, "r") as file:
            return file.read()

    def call(self, state: State) -> State:
        query = state["query"]
        sql = state["sql"]
        query_result = state["query_result"]
        schema = state["schema"]

        user_prompt = """
        # Pergunta do usuário
        {query}

        # Código SQL usado
        {sql}

        # Resultado da query retornado pelo banco de dados
        {query_result}
        """

        prompt = ChatPromptTemplate.from_messages([
            ("system", self.__prompt),
            ("user", user_prompt)
        ])
        
        chain = prompt | self.__llm

        resultado = chain.invoke({"schema": schema, "query": query, "sql": sql, "query_result": query_result})

        return {"feedback": resultado.feedback, "makes_sense": resultado.makes_sense, "query_result": query_result}
    
# from langchain_ollama import ChatOllama
# dba_agent = DBAAgent(
#     prompt_path="src/ai/prompts/dba_agent.txt",
#     llm=ChatOllama(model="qwen2.5:3b", temperature=0.1,)
# )

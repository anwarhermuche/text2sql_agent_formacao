from langchain_core.prompts import ChatPromptTemplate
from src.ai.state.state import State
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

class MarceloAgent:

    def __init__(self, prompt_path: str, llm):
        self.__prompt = self.__get_prompt(prompt_path)
        self.__llm = llm

    def __get_prompt(self, prompt_path: str) -> str:
        with open(prompt_path, "r") as file:
            return file.read()

    def call(self, state: State) -> State:
        query = state["query"]
        history = state["history"]

        if state.get("malicioso"):
            return {"resposta": "Você só pode executar comandos de seleção."}
        
        if state.get("recursion_limit") > 2:
            return {"resposta": "Infelizmente, não conseguimos encontrar uma resposta para sua pergunta.\nVocê pode tentar perguntar de outra forma, por favor?\nSendo mais detalhista e específico!"}

        query_result = state.get("query_result", "")

        user_prompt = f"""
        # Pergunta do usuário
        {query}

        # Resultado da query retornado pelo banco de dados
        {query_result}
        """

        messages = [SystemMessage(content = self.__prompt)]

        if history:
            messages += history

        messages += [HumanMessage(content = user_prompt)]

        prompt = ChatPromptTemplate.from_messages(messages)
        
        chain = prompt | self.__llm | StrOutputParser()

        resultado = chain.invoke({})

        state["history"].append(HumanMessage(content = state["query"]))
        state["history"].append(AIMessage(content = resultado))

        return {"resposta": resultado, "recursion_limit": 0, "history": history}
    


from langchain_core.prompts import ChatPromptTemplate
from src.ai.structured_outputs.checker_agent_response import CheckerAgentResponse
from src.ai.state.state import State

class CheckerAgent:

    def __init__(self, prompt_path: str, llm):
        self.__prompt = self.__get_prompt(prompt_path)
        self.__llm = llm.with_structured_output(CheckerAgentResponse)

    def __get_prompt(self, prompt_path: str) -> str:
        with open(prompt_path, "r") as file:
            return file.read()
        
    def call(self, state: State) -> State:
        sql = state["sql"]

        prompt = ChatPromptTemplate.from_messages([
            ("system", self.__prompt),
            ("user", sql)
        ])
        
        chain = prompt | self.__llm

        resultado = chain.invoke({"sql": sql})

        return {"malicioso": resultado.malicioso}
    


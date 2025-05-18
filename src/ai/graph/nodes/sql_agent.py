from langchain_core.prompts import ChatPromptTemplate
from src.ai.structured_outputs.sql_agent_response import SQLAgentResponse
from src.ai.state.state import State

class SQLAgent:

    def __init__(self, prompt_path: str, llm):
        self.__prompt = self.__get_prompt(prompt_path)
        self.__llm = llm.with_structured_output(SQLAgentResponse)

    def __get_prompt(self, prompt_path: str) -> str:
        with open(prompt_path, "r") as file:
            return file.read()
    
    def call(self, state: State) -> State:
        query = state["query"]
        schema = state["schema"]
        history = state["history"]

        user_prompt = f"""
        # Histórico de perguntas e respostas
        {list(map(lambda message: f"Role: {message.type}\nContent: {message.content}\n\n", history))}
        
        # Pergunta do usuário
        {query}
        """

        input_variables = {"schema": schema}
        
        if state.get("feedback"):
            feedback = state["feedback"]
            sql = state["sql"]
            user_prompt += f"""
            # Feedback do DBA
            {feedback}

            # Código SQL usado
            {sql}
            """


        prompt = ChatPromptTemplate.from_messages([
            ("system", self.__prompt),
            ("user", user_prompt)
        ])

        chain = prompt | self.__llm

        resultado = chain.invoke(input_variables)

        return {"sql": resultado.sql, "recursion_limit": state["recursion_limit"] + 1}

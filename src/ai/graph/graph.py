from src.ai.graph.nodes.checker_agent import CheckerAgent
from src.ai.graph.nodes.sql_agent import SQLAgent
from src.ai.graph.nodes.marcelo_agent import MarceloAgent
from src.ai.graph.nodes.db_consulter_agent import DBConsulterAgent
from src.ai.graph.nodes.dba_agent import DBAAgent
from ai.graph.nodes.dba_decider import dba_decider
from src.ai.graph.nodes.checker_agent_decider import checker_agent_decider
from src.ai.graph.nodes.sql_agent_decider import sql_agent_decider
from src.ai.state.state import State
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

builder = StateGraph(State)
llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.1)
agents = {
    "checker_agent": CheckerAgent,
    "sql_agent": SQLAgent,
    "marcelo_agent": MarceloAgent,
    "db_consulter_agent": DBConsulterAgent,
    "dba_agent": DBAAgent
}
for agent_name, agent_class in agents.items():
    prompt_path = f"src/ai/prompts/{agent_name}.txt"
    builder.add_node(agent_name, agent_class(prompt_path, llm).call)

builder.add_edge(START, "sql_agent")
builder.add_conditional_edges("sql_agent", sql_agent_decider)
builder.add_conditional_edges("checker_agent", checker_agent_decider)
builder.add_edge("db_consulter_agent", "dba_agent")
builder.add_conditional_edges("dba_agent", dba_decider)
builder.add_edge("marcelo_agent", END)

checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)


from src.ai.state.state import State

def sql_agent_decider(state: State) -> str:
    if state.get("sql", ""):
        return "checker_agent"
    
    return "marcelo_agent"
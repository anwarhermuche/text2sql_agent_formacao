from src.ai.state.state import State

def checker_agent_decider(state: State) -> str:
    if state.get("malicioso"):
        return "marcelo_agent"
    
    return "db_consulter_agent"
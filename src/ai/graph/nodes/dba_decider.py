from src.ai.state.state import State

def dba_decider(state: State) -> str:
    if state.get("makes_sense") or state.get("recursion_limit") > 2:
        return "marcelo_agent"
    
    
    return "sql_agent"
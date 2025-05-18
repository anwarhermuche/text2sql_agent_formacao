from langchain_core.prompts import ChatPromptTemplate
from src.ai.state.state import State
import pandas as pd
import duckdb

class DBConsulterAgent:

    def __init__(self, prompt_path: str, llm):
        pass

    def __query_bd(self, sql: str) -> str:
        resultado_query = duckdb.sql(sql)
        return resultado_query.df()
    
    def __get_str_representation(self, df: pd.DataFrame, max_rows: int = 20) -> str:
        # Garante que não ultrapasse o limite
        df_preview = df.head(max_rows).copy()

        # Adiciona os tipos das colunas como primeira linha
        dtypes_row = {col: str(dtype) for col, dtype in df.dtypes.items()}
        types_df = pd.DataFrame([dtypes_row])

        # Concatena os tipos + dados
        final_df = pd.concat([types_df, df_preview], ignore_index=True)

        # Converte para markdown
        markdown_str = final_df.to_markdown(index=False)

        return f"### DataFrame Snapshot (máx. {max_rows} linhas)\n\n{markdown_str}"

    def call(self, state: State) -> State:
        sql = state["sql"]
        try:
            df_query = self.__query_bd(sql.replace("\n", " "))
            df_str = self.__get_str_representation(df_query)
        except Exception as e:
            df_str = f"### Erro ao executar a consulta:\n\n```sql\n{sql}\n```\n\nErro: {str(e)}"

        return {"query_result": df_str}
    


import os
import pandas as pd

class SchemaExtractor:
    def __init__(self, data_path='src/data'):
        self.data_path = data_path
        self.schema_str = ""

    def infer_dtype(self, series):
        if pd.api.types.is_integer_dtype(series):
            return "int"
        elif pd.api.types.is_float_dtype(series):
            return "float"
        elif pd.api.types.is_bool_dtype(series):
            return "bool"
        elif pd.api.types.is_datetime64_any_dtype(series):
            return "datetime"
        else:
            return "str"

    def get_unique_values(self, series):
        unique_vals = series.dropna().unique()
        if len(unique_vals) < len(series.dropna()):
            return list(unique_vals[:40])  # mostra no máximo 15 valores únicos
        return None

    def extract_schema(self):
        for filename in os.listdir(self.data_path):
            if filename.endswith('.csv'):
                file_path = os.path.join(self.data_path, filename)
                try:
                    df = pd.read_csv(file_path)
                except Exception as e:
                    continue  # pula arquivos corrompidos ou mal formatados

                self.schema_str += f"# Tabela = '{file_path}'\nColunas:\n"
                for col in df.columns:
                    dtype = self.infer_dtype(df[col])
                    unique_values = self.get_unique_values(df[col])
                    if unique_values:
                        self.schema_str += f"- {col}: {dtype} (Unique values: {unique_values})\n"
                    else:
                        self.schema_str += f"- {col}: {dtype}\n"
                self.schema_str += "\n"

        return self.schema_str
    

if __name__ == '__main__':
    extractor = SchemaExtractor()
    schema = extractor.extract_schema()
    print(schema)
# import pandas as pd
# from pandasql import sqldf
# import json


# def dataframe_description(df: pd.DataFrame) -> str:
#     """
#     Reads the columns of a dataframe and generates a description.

#     Args:
#         df (pd.DataFrame): The Pandas DataFrame to be described.

#     Returns:
#         str: A description of the DataFrame columns and their types.
#     """
#     cols = list(df.columns)
#     types = df.dtypes.astype(str).tolist()
#     msg = "\n\t".join(
#         [f"- {name}. ({types[i]})" for i, name in enumerate(cols)]
#     )
#     description = f"Columns in DataFrame:\n\t{msg}"
#     return description


# def dataframe_stats(df: pd.DataFrame) -> str:
#     """
#     Retorna estatísticas descritivas do DataFrame com base na função describe() do pandas.

#     Args:
#         df (pd.DataFrame): O DataFrame a ser analisado.

#     Returns:
#         str: Estatísticas descritivas das colunas numéricas do DataFrame.
#     """
#     stats = df.describe().transpose()
#     linhas = []
#     for coluna, valores in stats.iterrows():
#         linha = (f"- {coluna}: média = {valores['mean']:.2f}, "
#                  f"mínimo = {valores['min']:.2f}, "
#                  f"máximo = {valores['max']:.2f}, "
#                  f"desvio padrão = {valores['std']:.2f}")
#         linhas.append(linha)
#     return "\n".join(linhas)



# def query_dataframe(query: str, df: pd.DataFrame) -> str:
#     """
# Make a query in pandas DataFrame using Data Query Language, which is a
# subset of SQL.

# Args:
#     query: str - SQL-like query
#     df: pd.DataFrame - Pandas DataFrame
# Returns:
#         str: Data from Query.
#     """
#     result = sqldf(query, {"df": df})
#     return json.dumps(result)
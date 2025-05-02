from google.adk.agents import Agent
from .adktools import *


class AdkAgent:
    def __init__(self, llm, df):
      self._llm = llm
      self._df = df
      self._agent = None;


    @property
    def df(self):
        return self._df
   
    @property
    def llm(self):
       return self._llm

    def _create_agent(self):

      def get_df() -> pd.DataFrame:
            """
            The tool return  the Pandas DataFrame, df, to be analised by Agents
            Returns:
                pd.DataFrame: A Pandas DataFrame to be used by agent
            """
            return self.df

      self._agents = Agent(
        name="akdagent",
        model=self._llm,
        description=(
            "Agente que responde perguntas simples"
        ),
        instruction=(
            "Você é um agente que responde perguntas do usuario de forma simples"
        ),
        tools=[],
      )

    @property
    def agent(self):
        if self._agents is None:
            self._create_agents()
        return self._agents
    
    def run(self, query: str) -> str:
        mensagem = f"Responda esta pergunta do usuario {query}"

        return self._agent.predict(user_input=mensagem)
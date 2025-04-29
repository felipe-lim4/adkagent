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

      _agents = Agent(
        name="",
        model="",
        description=(
            ""
        ),
        instruction=(
            ""
        ),
        tools=[get_df,],
      )
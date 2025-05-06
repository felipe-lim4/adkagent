from adkagentpandas import AdkAgent
from adkagentpandas import AgentRunner
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()


# Configurando serviços de memória
agente_basic=AdkAgent()

runner = AgentRunner(agente_basic.agent)

resposta = runner.send_query_to_agent("Qual a capital da França?")

print(resposta)
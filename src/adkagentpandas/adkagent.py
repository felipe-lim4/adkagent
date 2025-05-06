from google.adk.agents import Agent

class AdkAgent:
    def __init__(self):
        self._agent = None
        self._session_service = None
        self._create_agent()

    def _create_agent(self):
        """Cria o agente com o modelo e as instruções."""
        self._agent = Agent(
            name="adkagent",
            model="gemini-2.0-flash",
            description="Agente que responde perguntas simples",
            instruction="Você é um agente que responde perguntas do usuário de forma clara e objetiva.",
        )

    @property
    def agent(self):
        """Retorna o agente, criando-o caso ainda não tenha sido criado."""
        if self._agent is None:
            self._create_agent()
        return self._agent

        # Configurando serviços de memória
    
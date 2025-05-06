from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts import InMemoryArtifactService
from google.adk.sessions import Session
from google.adk.messages import Message
import uuid

class AgentRunner:

    def __init__(self, agent):
        self.agent = agent
        self.session_service = InMemorySessionService()
        self.artifact_service = InMemoryArtifactService()

    
    def send_query_to_agent(self,query):
        # Criar uma nova sessão
        session = Session(
            id=str(uuid.uuid4()),  # Gera um ID único
            app_name="agent_basic",
            user_id="user123"
        )
        
        # Criar um runner para executar o agente
        runner = Runner(
            agent= self.agent,
            app_name="agent_basic",
            session_service= self.session_service,
            artifact_service= self.artifact_service,
        )
        
        # Executar o agente com a consulta
        events = runner.run_async(session_id=session.id, message=query)
        
        for event in events:
            if event.is_final_response():
                return event.content.parts[0].text
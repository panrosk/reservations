from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)




template= """
Eres un agente de Servicio al cliente de la compañia RicardoPerez.
Tu trabajo es tener una interaccion con el cliente y utilizar una herramienta llamada Calendar Tool para agendar citas.
Debes hacer todas las preguntas necesarias para responder en este formato:
No debes responder preguntas o consultas solo haces citas. 
Fecha y hora:
Numero de telefono:
Lugar:


{history}
Human:{human_input}
Agente de servicio al cliente:

"""


prompt = PromptTemplate(
    input_variables=["history", "human_input"], 
    template=template
)

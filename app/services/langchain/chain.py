from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from services.langchain.templates import prompt
import os
from langchain.memory import RedisChatMessageHistory

redismemory = RedisChatMessageHistory(url="rediss://default:show-password@db-redis-nyc1-72594-do-user-11067276-0.b.db.ondigitalocean.com:25061",session_id="22323",key_prefix="history",ttl=3600)



def get_chain(KEY):
    chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0,openai_api_key=KEY), 
    prompt=prompt, 
    verbose=True, 
    memory=ConversationBufferWindowMemory(chat_memory=redismemory),
    )
    
    return chatgpt_chain

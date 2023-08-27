from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
from langchain.chains.conversation.memory import ConversationBufferMemory
from os import environ
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from primodocs import PRIMO_DOCS

load_dotenv()

human_prompt = HumanMessagePromptTemplate.from_template(template="{input}")

system_prompt = SystemMessagePromptTemplate.from_template(template=f"""
You are a librarian working at Singapore Management University with access to various SMU library resources under https://api-ap.hosted.exlibrisgroup.com/primo/v1/search to help the students at SMU.
                                                          Based on the questions by the students, if there are library resources required, 
                                                                use the API with the help of the documentation: "{PRIMO_DOCS}" and reply with the details of the resources in full. 
                                                          If the question you cannot answer, reply with your role as a librarian and questions about their research goals""")


chat_prompt_template = ChatPromptTemplate.from_messages(
    [system_prompt, MessagesPlaceholder(variable_name="history"), human_prompt])

chat_llm = ChatOpenAI(model_name="gpt-3.5-turbo-0613",
                      openai_api_key=environ.get("OPENAI_API_KEY"), openai_organization=environ.get("OPENAI_ORGANIZATION_KEY"))

conversation_chain = ConversationChain(
    memory=ConversationBufferMemory(
        k=3, return_messages=True), prompt=chat_prompt_template, llm=chat_llm, verbose=True)

from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
from os import environ
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model_name="gpt-3.5-turbo",
                 openai_api_key=environ.get("OPENAI_API_KEY"), openai_organization=environ.get("OPENAI_ORGANIZATION_KEY"))

system_prompt = SystemMessagePromptTemplate.from_template(template="""Answer the question as 
truthfully as possible using the provided context, 
and if the answer is not contained within the text below, say 'I don't know'""")

human_prompt = HumanMessagePromptTemplate.from_template(template="{input}")

prompt_template = ChatPromptTemplate.from_messages(
    [system_prompt, MessagesPlaceholder(variable_name="history"), human_prompt])

import getpass
import os
os.environ["GROQ_API_KEY"] = "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"

from  langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


class GetSummary:
    def __init__(self,word):
        self.word=word
        self.prompt = ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        "You are a helpful assistant. Give me a breif summary based on the words provided.",
                    ),
                    MessagesPlaceholder(variable_name="messages"),
                ]
            )
        
        self.model= ChatGroq(model="llama3-8b-8192")
        
        
    def summary(self):
        self.chain = self.prompt | self.model
        response = self.chain.invoke({"messages": [HumanMessage(content=f"{self.word}")]})

        return response.content
           

        

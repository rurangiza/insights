
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, AIMessageChunk
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from typing import List

load_dotenv()


class LLM:
    def __init__(self):
        self._llm = ChatOpenAI()
        self._prompt = self.set_prompt()
        self._output_parser = self.set_output_parser()
        self._chain = self.set_chain()
    
    def set_chain(self):
        return self._prompt | self._llm | self._output_parser
    
    def set_prompt(self):
        system_message = "You are a helpful assistant."
        return ChatPromptTemplate.from_messages([
            ('system',system_message),
            ('user','{input}'),
        ])
    
    def set_output_parser(self) -> str:
        """ Format the LLM's answer """
        return StrOutputParser()

    def invoke(self, question: str):
        """ get LLM answer once it's ready """
        return self._chain.invoke({
            'input': question
        })


    def stream(self, question: str, streamlit_container = None, display_func = None) -> str:
        """ Stream answer SYNChronously """
        response: str = ""
        chunks: List[AIMessageChunk] = []
        for chunk in self._llm.stream(question):
            response += chunk.content
            chunks.append(chunk)
            if streamlit_container:
                streamlit_container.markdown(response)
            elif display_func:
                display_func(response)
            else:
                print(chunk.content, end="", flush=True)
        
        return response

    async def astream(self, question: str, streamlit_container = None, display_func = None) -> str:
        """ Stream answer ASYNChronously """
        for chunk in self._llm.stream(question):
            yield chunk.content
            # response += chunk.content
            # chunks.append(chunk)
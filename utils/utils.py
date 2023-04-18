from datasets import load_dataset
from dotenv import load_dotenv

from langchain.document_loaders import DirectoryLoader , TextLoader
from langchain.text_splitter import CharacterTextSplitter

from langchain.vectorstores import Chroma, ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain import OpenAI

from huggingface_hub import hf_hub_download
from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
import numpy as np
import os

load_dotenv("./env/.env")
API_KEYS = os.getenv("API_KEY")
# Get your API keys from openai, you will need to create an account. 
# Here is the link to get the keys: https://platform.openai.com/account/billing/overview
os.environ["OPENAI_API_KEY"] = API_KEYS 

class Dataloader():
    def __init__(self , config) -> None:
        self.config = config

    def __len__(self):
        return len(self.load_dataset()) 
    
    def json2text(self):

        with open(self.config['dataset_txt'] ,mode="w",encoding="utf-8") as file:
        
            for idx in range(self.__len__()):
                file.write(self.load_dataset()[idx]['output'] + "\n" + "\n")
            file.close()

    def load_jsondataset(self):
        return load_dataset("json" , data_files = self.config['dataset_json'], split="train")

    def load_dataset(self):
        loader=TextLoader(self.config['dataset_txt'])
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=self.config["chunk_size"] , chunk_overlap=0)
        texts = text_splitter.split_documents(documents)
        return texts

class Functional(Dataloader):
    def __init__(self , config) -> None:
        super(Functional ,self).__init__(config)
        self.config = config

    def embeddings_chroma(self):

        doc_search = Chroma.from_documents(self.load_dataset() , OpenAIEmbeddings())
        return doc_search

    def embeddings_faiss(self):
        doc_search = FAISS.from_texts(self.load_dataset() , OpenAIEmbeddings())
        return doc_search

    def QA_chroma(self, question : str ="who are you?"):
        llm = self.config["llm"]
        if llm=="GPT4ALL":
            if not os.path.exists(self.config['weights']):
                os.makedirs(self.config['weights'])
                #Download the model
                hf_hub_download(repo_id="LLukas22/gpt4all-lora-quantized-ggjt",
                                filename="ggjt-model.bin",
                                local_dir=self.config['weights'])
            llm = LlamaCpp(model_path=self.config['weights']+"ggjt-model.bin")
            qa  = RetrievalQA.from_chain_type(llm = llm,
                            chain_type="stuff",
                            retriever = self.embeddings_chroma().as_retriever())
            answer = qa.run(question) 
            return answer
        else:
            qa  = RetrievalQA.from_chain_type(llm = OpenAI(),
                            chain_type="stuff",
                            retriever = self.embeddings_chroma().as_retriever())
            answer = qa.run(question) 
            return answer



     
   

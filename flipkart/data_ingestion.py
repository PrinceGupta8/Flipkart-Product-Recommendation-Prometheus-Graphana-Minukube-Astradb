from langchain_astradb import astradbvector
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from flipkart.config import Config
from flipkart.data_converter import DataConverter

class Data_Ingestion:
    def __init__(self):
        self.embedding=HuggingFaceEndpointEmbeddings(model=Config.RAG_MODEL)
        self.vstore=astradbvector(
            name="flipkart_database",
            api_endpoint=Config.ASTRA_DB_API_ENDPOINT,
            token=Config.ASTRA_DB_APPLICATION_TOKEN,
            namespace=Config.ASTRA_DB_KEYSPACE
        )

    def ingest(self,load_existing=True):
        if load_existing==True:
            return self.vstore
        docs=DataConverter("data/flipkart_product_review.csv").convert()
        self.vstore.add_documents(docs)
        return self.vstore
        
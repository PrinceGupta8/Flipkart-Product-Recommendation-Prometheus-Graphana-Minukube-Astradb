import pandas as pd
from langchain_core.documents import Document

class DataConverter:
    def __init__(self,file_path):
        self.file_path=file_path

    def convert(self):
        df=pd.read_csv(self.file_path)[["product_title","review"]]
        docs=[Document(page_content=raw["review"], metadata={"product_name":raw["product_title"]}) for _,raw in df.iterrows()]

        return docs
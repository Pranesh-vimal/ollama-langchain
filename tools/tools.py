from typing import Optional
 
from langchain_core.tools import BaseTool
from langchain_core.tools.base import ArgsSchema
from pydantic import BaseModel, Field
from langchain_community.document_loaders import Docx2txtLoader
 
class DocxFileInput(BaseModel):
    file_path: str = Field(description="Path to the docx file")
 
 
class DocxFileLoad(BaseTool):
    name:str = "docx_file_load"
    description:str = "Loads the content of a docx file"
    args_schema:Optional[ArgsSchema]=DocxFileInput
 
    def _run(self, file_path:str):
        """Use the tool."""
        return Docx2txtLoader(file_path).load()
 
 
    
 
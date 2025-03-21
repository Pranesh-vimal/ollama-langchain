# Import necessary libraries
from langchain_ollama import OllamaEmbeddings  # For creating embeddings using Ollama
import os  # For working with files and directories
from langchain_community.vectorstores import FAISS  # Vector database
from langchain_text_splitters import RecursiveCharacterTextSplitter  # For splitting text into chunks
import PyPDF2  # For processing PDF files
 
# Step 1: Set up the embedding model
# This model converts text into numerical vectors
print("Step 1: Setting up the embedding model...")
embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
)
 
# Step 2: Set up a text splitter
# This splits long documents into smaller chunks for better processing
print("Step 2: Setting up the text splitter...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,  # Each chunk will have approximately 100 characters
    chunk_overlap=20,  # Overlap between chunks to maintain context
    length_function=len,
)
 
# Step 3: Get all text files and PDF files from the current directory
print("Step 3: Finding text and PDF files in the current directory...")
# List of file extensions we want to process
file_extensions = ['.txt', '.pdf']
files_to_process = []
 
# Define the resumes directory path
resumes_dir = '/Users/mageshkumarnallasivam/Desktop/Testing/resumes'
 
# Walk through the resumes directory
for file in os.listdir(resumes_dir):
    # Check if the file has one of our target extensions
    if any(file.endswith(ext) for ext in file_extensions):
        # Store the full path to the file
        full_path = os.path.join(resumes_dir, file)
        files_to_process.append(full_path)
 
print(f"Found {len(files_to_process)} files to process")
 
# Step 4: Read and process each file
print("Step 4: Processing files and creating document chunks...")
all_documents = []
 
for file_path in files_to_process:
    try:
        # Check if the file is a PDF
        if file_path.endswith('.pdf'):
            print(f"Processing PDF: {os.path.basename(file_path)}")
            # Extract text from PDF
            content = ""
            with open(file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                # Extract text from each page
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    content += page.extract_text() + "\n"
        else:
            # For text files, read directly
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        
        # Add metadata to keep track of which file each chunk came from
        metadata = {"source": file_path, "filename": os.path.basename(file_path)}
        
        # Split the content into chunks
        docs = text_splitter.create_documents(
            [content],
            metadatas=[metadata]
        )
 
        print("Docs : ",docs)
        
        # Add the chunks to our collection
        all_documents.extend(docs)
        print(f"Processed: {os.path.basename(file_path)}")
    except Exception as e:
        print(f"Error processing {os.path.basename(file_path)}: {e}")
 
print(f"Created {len(all_documents)} document chunks")
 
# Step 5: Create a vector store from the documents
print("Step 5: Creating vector embeddings and storing in FAISS...")
vector_store = FAISS.from_documents(all_documents, embeddings)
 
# Step 6: Save the vector store to disk
print("Step 6: Saving the vector database...")
vector_store.save_local("faiss_index")
print("Vector database saved to 'faiss_index'")
 
print("Done! You can now use search.py to query the vector database.")
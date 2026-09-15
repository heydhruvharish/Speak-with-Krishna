from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
import uuid
import os
# from sklearn.metrics.pairwise import cosine_similarity

#Chunks
def split_docs(document,chunk_size=800,chunk_overlap=100):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    chunked_doc=text_splitter.split_documents(document)
    
    return chunked_doc
    
#Embedding
class EmbeddingManager:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model_name=model_name
        print("loading model....", self.model_name)
        self.model = SentenceTransformer(self.model_name)
        print("embedding dimensions=", self.model.get_embedding_dimension())
    def generate_embeddings(self, text):
        embedding =self.model.encode(text, show_progress_bar=True)
        print("embeddings shape:", embedding.shape)
        return embedding

#Vector DB
class VectorStoreManager:
    def __init__(self, persist_directory="Data/vector_store", collection_name="pdf_document"):  #Collecection is like table in normal DB ,it stores chunks and embeddings
        self.collection_name = collection_name
        self.persist_directory = persist_directory
        self.collection = None
        self.client = None

        self._initialize_store()

    def _initialize_store(self):
        os.makedirs(self.persist_directory, exist_ok=True)
        
        # create a client
        self.client = chromadb.PersistentClient(path=self.persist_directory)

        # create the collection
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"description": "vector store collection for pdf embeddings in RAG"}
        )

        print("initialized the vector store with collection:", self.collection_name)
        print("docs in collection:", self.collection.count())
        

    def add_documents(self, documents, embeddings):
        
        #Every document has 1 embedding list
        if len(documents) != len(embeddings):
            raise ValueError("num of documents does not match num of embeddings")


        # store => ids, embedding, document, metadata
        ids = []
        all_metadata = []
        documents_content = []
        embeddings_list = []

        for i, (doc, embedding) in enumerate(zip(documents, embeddings)):   #if documents=[a,b] embeddings[jh,lk] then zip turns them to (a,jh)(b,lk)
            doc_id = f"doc_{uuid.uuid4()}"
            ids.append(doc_id)

            metadata = dict(doc.metadata)
            metadata["doc_index"] = i
            metadata["content_length"] = len(doc.page_content)
            all_metadata.append(metadata)

            documents_content.append(doc.page_content)

            embeddings_list.append(embedding.tolist())

        self.collection.add(
            ids=ids,
            metadatas=all_metadata,
            documents=documents_content,
            embeddings=embeddings_list
        )

        print("total documents added in vector store=", len(documents_content))
        print("docs in collection:", self.collection.count())

#Retriver
class RAGRetriever:
    def __init__(self, embedding_manager, vector_store):
        self.embedding_manager = embedding_manager
        self.vector_store = vector_store


    def retrieve(self, query, top_k=10, score_threshold=0.0):
        # query => embedding
        query_embeddings = self.embedding_manager.generate_embeddings([query])[0]   #Converting the query to numbers(embedding)

        # semantic search
        results = self.vector_store.collection.query(
            query_embeddings=[query_embeddings.tolist()],
            n_results=top_k
        )
        #Result structure
        # results["documents"] = [
        # [
        #     "This is chunk 1",
        #     "This is chunk 2",
        #     "This is chunk 3"
        # ]
        # ]
        
        # cosine similarity
        retrieved_docs=[]
        
        if results["documents"] and results["documents"][0]:
            ids = results["ids"][0]
            metadatas = results["metadatas"][0]
            documents = results["documents"][0]
            distances = results["distances"][0]    #Smaller distance ,more similarity

            for i, (doc_id, metadata, document, distance) in enumerate(zip(ids, metadatas, documents, distances)):
                similarity_score = 1 - distance

                if similarity_score >= score_threshold:
                    retrieved_docs.append({
                        "id": doc_id,
                        "document": document,
                        "metadata": metadata,
                        "distance": distance,
                        "similarity_score": similarity_score,
                        "rank" : i + 1
                    })

            print(f"retrieved {len(retrieved_docs)} documents")

        else:
            print("no documents found")

        return retrieved_docs

embedding_manager=EmbeddingManager()
vector_store=VectorStoreManager()

# pdf_loader = PyMuPDFLoader("Data/Bhagvad_gita_as_it_is.pdf")
# document = pdf_loader.load()

# chunk=split_docs(document)

# texts=[doc.page_content for doc in chunk]

# embeddings=embedding_manager.generate_embeddings(texts)

# vector_store.add_documents(chunk,embeddings)

#RETRIVAL Pipeline
rag_retriever = RAGRetriever(embedding_manager, vector_store)
# rag_retriever.retrieve("karma")


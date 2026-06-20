import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import fitz

from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


PDF_FOLDER = "documents"
FAISS_INDEX_FOLDER = "cpf_act_faiss_nomic_index"


# ------------------------------------------------------------
# 1. Split long text into smaller chunks
# ------------------------------------------------------------
def chunk_text(text, chunk_size=2000, overlap=300):
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# ------------------------------------------------------------
# 2. Read text from PDF files
# ------------------------------------------------------------
def load_pdf_text(folder):
    all_text = ""

    for filename in os.listdir(folder):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(folder, filename)
            print(f"Reading: {filename}")

            doc = fitz.open(file_path)

            for page in doc:
                all_text += page.get_text()

            doc.close()

    return all_text


# ------------------------------------------------------------
# 3. Build or load saved FAISS index
# ------------------------------------------------------------
def build_simple_index():
    embeddings = OllamaEmbeddings(model="nomic-embed-text-v2-moe")

    if os.path.exists(FAISS_INDEX_FOLDER):
        print("Loading saved FAISS index...")

        vectorstore = FAISS.load_local(
            FAISS_INDEX_FOLDER,
            embeddings,
            allow_dangerous_deserialization=True
        )

        print("Saved FAISS index loaded.")
        return vectorstore, embeddings

    print("No saved FAISS index found. Building new FAISS index...")

    print("Loading PDF...")
    text = load_pdf_text(PDF_FOLDER)

    print("Chunking text...")
    chunks = chunk_text(text)

    print(f"Total chunks created: {len(chunks)}")

    print("Creating FAISS vectorstore...")
    vectorstore = FAISS.from_texts(chunks, embeddings)

    print("Saving FAISS index...")
    vectorstore.save_local(FAISS_INDEX_FOLDER)

    print("FAISS index is ready and saved.")

    return vectorstore, embeddings


# ------------------------------------------------------------
# 4. Retrieve the most relevant chunks using FAISS
# ------------------------------------------------------------
def retrieve_relevant_chunks(question, top_k=4):
    docs = vectorstore.similarity_search(question, k=top_k)

    top_chunks = [doc.page_content for doc in docs]

    return top_chunks



# ------------------------------------------------------------
# 5. Build/load index when this file starts
# ------------------------------------------------------------
print("Building SINGAPORE CPF ACT FAISS RAG system...")
vectorstore, embeddings = build_simple_index()


# ------------------------------------------------------------
# 6. Set up Ollama LLM and prompt
# ------------------------------------------------------------
llm = ChatOllama(model="llama3.2")

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant answering questions based on the Singapore Central Provident Fund Act 1953.

Answer only from the provided context.
                                          
If the answer is not found in the context, say that the CPF Act context provided does not contain enough information.

When possible, cite the relevant section number or Part of the Act.
                                          
Do not provide financial, legal, tax, CPF planning, or investment advice.
Explain in clear and simple language.

Important rules:
1. Do not guess.
2. Do not use outside knowledge.
3. If the answer is not found in the context, say:
"I could not find the answer in the provided Singapore Central Provident Fund Act 1953 context."
4. If the context contains relevant section numbers, mention them clearly.
5. Explain in plain language, but stay faithful to the Act.
6. When referring to provisions of Singapore Central Provident Fund Act, use “section” instead of “article”.                                          
                                          

Language rules:
- Answer in the same language as the user's question.
- If the user's question is not in English, answer fully in that language.
- Do not mix languages unless quoting a legal term from the Act is necessary.
- When explaining English legal terms in another language, provide a clear explanation in that language.

Formatting rules:
- Use short paragraphs.
- Use bullet points where helpful.
- Put each bullet point on a new line.
- Leave a blank line between paragraphs.
- Do not put everything into one long paragraph.
- If there are several conditions, list them clearly.
- If there are exceptions or limitations, mention them separately.                                         

Context:
{context}

Question:
{question}

Answer:
""")



# ------------------------------------------------------------
# 7. Main RAG function
# ------------------------------------------------------------
def translate_question_to_english(question):
    translation_prompt = ChatPromptTemplate.from_template("""
Translate the following question into clear English for legal document search.
Do not answer the question.
Only provide the translated English question.

Question:
{question}

English translation:
""")

    chain = translation_prompt | llm | StrOutputParser()

    translated_question = chain.invoke({
        "question": question
    })

    return translated_question.strip()


def ask_rag(question):
    if question.isascii():
        search_question = question
    else:
        search_question = translate_question_to_english(question)

    print(f"Original question: {question}")
    print(f"Search question: {search_question}")

    relevant_chunks = retrieve_relevant_chunks(search_question, top_k=4)

    context = "\n\n".join(relevant_chunks)

    chain = prompt | llm | StrOutputParser()

    answer = chain.invoke({
        "context": context,
        "question": question
    })

    return answer

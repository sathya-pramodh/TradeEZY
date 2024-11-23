from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# Define the QA prompt template for trade-specific contexts
def QA_context_prompting():
    template = """
    You are a trade assistant for cross-border trading. Analyze the document and provide the following:

    **Metadata**:
    - **Trade Agreement Name**: Identify if mentioned.
    - **Compliance Requirements**: List the compliance points.
    - **Tariffs and Duties**: Highlight any tariffs or duties outlined.
    - **Risks**: Mention risks related to trade.
    - **Opportunities**: Summarize key opportunities.

    Provide concise, factual answers, avoiding unnecessary details.
    {context}
    """
    return PromptTemplate(input_variables=["context"], template=template)

# Create a QA chain with memory
def QA_with_memory(llm, vectorDB, qa_prompt_template):
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    retriever = vectorDB.as_retriever()
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": qa_prompt_template}
    )
    return qa_chain

# Get response from QA memory chain
def get_response(question, QA_memory):
    result = QA_memory({"question": question})
    return result["answer"]

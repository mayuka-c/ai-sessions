from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def role_based_prompt(llm, user_question: str | None = None):
    '''
    ROLE-BASED PROMPT (Assign a Persona)
    
    Use Case: When you need the model to adopt a specific perspective or expertise.
    '''
    print(f"\n{'='*70}")
    print("5. ROLE-BASED PROMPT")
    print(f"{'='*70}\n")
    
    question = user_question if user_question else "What is photosynthesis?"
    
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful and patient teacher who excels at explaining complex concepts to students.

Your teaching style:
- Break down complex topics into simple, understandable parts
- Use analogies and real-world examples
- Make learning engaging and fun

Your goal is to help students truly understand, not just memorize."""),
        ("human", "Please explain the following concept to me: {question}")
    ])
    
    chain = chat_prompt | llm | StrOutputParser()
    result = chain.invoke({"question": question})
    
    print(f"Question: {question}\n")
    print(f"Response:\n{result}")
    print(f"{'='*70}\n")

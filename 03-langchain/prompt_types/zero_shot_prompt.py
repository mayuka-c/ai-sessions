from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def zero_shot_prompt(llm, user_prompt: str | None = None):
    '''
    ZERO-SHOT PROMPT (No Examples Given)
    
    Use Case: When the model has sufficient pre-trained knowledge to handle
    the task without examples.
    '''
    print(f"\n{'='*70}")
    print("1. ZERO-SHOT PROMPT")
    print(f"{'='*70}\n")
    
    if not user_prompt:
        user_prompt = "Translate to Spanish: Hello, how are you?"
    
    template = """Task: {task}

Please provide a clear and concise response."""
    
    prompt = PromptTemplate(
        input_variables=["task"],
        template=template
    )
    
    chain = prompt | llm | StrOutputParser()
    result = chain.invoke({"task": user_prompt})
    
    print(f"Input: {user_prompt}")
    print(f"\nResponse: {result}")
    print(f"{'='*70}\n")

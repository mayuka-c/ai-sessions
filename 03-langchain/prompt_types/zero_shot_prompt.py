from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def zero_shot_prompt(llm, user_prompt: str | None = None):
    '''
    ZERO-SHOT PROMPT (No Examples Given) - LangChain Implementation
    
    Demonstrates LangChain's PromptTemplate and LLMChain for zero-shot prompting.
    
    Key LangChain Concepts:
    - PromptTemplate: Structured way to define prompts with variables
    - LLMChain: Combines prompt template with LLM for reusable chains
    - Input Variables: Dynamic prompt construction
    
    Use Case: When the model has sufficient pre-trained knowledge to handle
    the task without examples. LangChain makes it easy to create reusable
    prompt templates that can be applied to different inputs.
    '''
    print(f"\n{'='*70}")
    print("1. ZERO-SHOT PROMPT - LangChain PromptTemplate & LLMChain")
    print(f"{'='*70}")
    
    if not user_prompt:
        user_prompt = "Translate to Spanish: Hello, how are you?"
        print(f"Using default: {user_prompt}")
    
    print("\n--- LangChain Components ---")
    print("1. PromptTemplate: Defines the structure")
    print("2. LLMChain: Combines template + LLM")
    print("3. Input Variables: Dynamic content injection")
    
    # Create a PromptTemplate - LangChain's way to structure prompts
    template = """Task: {task}

Please provide a clear and concise response."""
    
    prompt = PromptTemplate(
        input_variables=["task"],
        template=template
    )
    
    print("\n--- Prompt Template ---")
    print(f"Template: {template}")
    print(f"Input Variables: {prompt.input_variables}")
    
    # Create LLMChain - combines prompt with LLM
    chain = LLMChain(llm=llm, prompt=prompt, verbose=False)
    
    print("\n--- Execution ---")
    print(f"User Input: {user_prompt}")
    
    # Run the chain
    result = chain.run(task=user_prompt)
    
    print(f"\n--- Model Response ---")
    print(f"Response: {result}")
    
    print("\n--- LangChain Benefits ---")
    print("✓ Reusable prompt templates")
    print("✓ Type-safe input variables")
    print("✓ Easy to modify and version control")
    print("✓ Chainable with other LangChain components")
    print(f"{'='*70}\n")

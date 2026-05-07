from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field


# ============================================================================
# 1. BASIC LLM SETUP
# ============================================================================

def basic_llm_setup():
    """Initialize and use LLM directly"""
    print("\n=== 1. Basic LLM Setup ===")
    
    # Create LLM instance
    llm = OllamaLLM(model="granite3.3:8b", temperature=0.7)
    
    # Simple invocation
    response = llm.invoke("What is LangChain in one sentence in simple words?")
    print(f"Response: {response}\n")
    
    return llm


# ============================================================================
# 2. PROMPT TEMPLATES
# ============================================================================

def prompt_templates(llm):
    """Using PromptTemplate for reusable prompts"""
    print("\n=== 2. Prompt Templates ===")
    
    # Create a template
    template = "Explain {topic} in simple terms."
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    
    # Format and use
    formatted = prompt.format(topic="deep learning")
    response = llm.invoke(formatted)
    print(f"Response: {response[:150]}...\n")


# ============================================================================
# 3. LLM CHAINS
# ============================================================================

def llm_chains(llm):
    """Combining prompts with LLMs using LCEL (LangChain Expression Language)"""
    print("\n=== 3. LLM Chains (LCEL) ===")
    
    template = "Translate '{text}' to {language}."
    prompt = PromptTemplate(input_variables=["text", "language"], template=template)
    
    # Modern LCEL approach using pipe operator
    chain = prompt | llm | StrOutputParser()
    
    result = chain.invoke({"text": "Hello, world!", "language": "Spanish"})
    print(f"Translation: {result}\n")


# ============================================================================
# 4. CHAT TEMPLATES
# ============================================================================

def chat_templates(llm):
    """Using ChatPromptTemplate for structured conversations"""
    print("\n=== 4. Chat Templates ===")
    
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful coding assistant."),
        ("human", "Explain {concept} briefly.")
    ])
    
    # Modern LCEL approach
    chain = chat_prompt | llm | StrOutputParser()
    result = chain.invoke({"concept": "list comprehension in Python"})
    print(f"Explanation: {result[:150]}...\n")


# ============================================================================
# 5. OUTPUT PARSERS
# ============================================================================

def output_parsers(llm):
    """Parsing structured output from LLMs"""
    print("\n=== 5. Output Parsers ===")
    
    # Define a Pydantic model for structured output
    class AnalysisOutput(BaseModel):
        language: str = Field(description="The programming language")
        difficulty: str = Field(description="Difficulty level: easy/medium/hard")
    
    parser = PydanticOutputParser(pydantic_object=AnalysisOutput)
    format_instructions = parser.get_format_instructions()
    
    template = """Analyze this: {query}

{format_instructions}"""
    
    prompt = PromptTemplate(
        template=template,
        input_variables=["query"],
        partial_variables={"format_instructions": format_instructions}
    )
    
    # Modern LCEL approach with parser
    chain = prompt | llm | parser
    result = chain.invoke({"query": "Python programming"})
    print(f"Structured output:\n{result}\n")


# ============================================================================
# 6. BATCH PROCESSING
# ============================================================================

def batch_processing(llm):
    """Processing multiple inputs efficiently"""
    print("\n=== 6. Batch Processing ===")
    
    prompts = [
        "Capital of France?",
        "Capital of Japan?",
        "Capital of Brazil?"
    ]
    
    responses = llm.batch(prompts)
    for q, a in zip(prompts, responses):
        print(f"Q: {q} → A: {a}")
    print()


# ============================================================================
# 7. STREAMING
# ============================================================================

def streaming_responses(llm):
    """Streaming responses for real-time output"""
    print("\n=== 7. Streaming ===")
    print("Response: ", end="")
    
    for chunk in llm.stream("List 3 benefits of LangChain."):
        print(chunk, end="", flush=True)
    print("\n")


# ============================================================================
# MAIN RUNNER
# ============================================================================

def run_all_examples():
    """Run all examples sequentially"""
    print("\n" + "="*60)
    print("LANGCHAIN FUNDAMENTALS - TEACHING MODULE")
    print("="*60)
    
    llm = basic_llm_setup()
    prompt_templates(llm)
    llm_chains(llm)
    chat_templates(llm)
    output_parsers(llm)
    batch_processing(llm)
    streaming_responses(llm)
    
    print("="*60)
    print("✓ All examples completed!")
    print("="*60 + "\n")


def run_interactive():
    """Interactive menu to run examples individually"""
    llm = OllamaLLM(model="granite3.3:8b", temperature=0.7)
    
    examples = {
        "1": ("Basic LLM Setup", lambda: basic_llm_setup()),
        "2": ("Prompt Templates", lambda: prompt_templates(llm)),
        "3": ("LLM Chains", lambda: llm_chains(llm)),
        "4": ("Chat Templates", lambda: chat_templates(llm)),
        "5": ("Output Parsers", lambda: output_parsers(llm)),
        "6": ("Batch Processing", lambda: batch_processing(llm)),
        "7": ("Streaming", lambda: streaming_responses(llm)),
    }
    
    while True:
        print("\n" + "="*60)
        print("LangChain Fundamentals - Choose Example:")
        print("="*60)
        for key, (name, _) in examples.items():
            print(f"{key}. {name}")
        print("8. Run All")
        print("0. Exit")
        print("="*60)
        
        choice = input("\nChoice: ").strip()
        
        if choice == "0":
            break
        elif choice == "8":
            run_all_examples()
        elif choice in examples:
            examples[choice][1]()
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    # Run interactively
    run_interactive()
    
    # Or run all at once:
    # run_all_examples()

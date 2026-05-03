from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.prompts import FewShotPromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema


# ============================================================================
# 1. BASIC LLM SETUP
# ============================================================================

def basic_llm_setup():
    """Initialize and use LLM directly"""
    print("\n=== 1. Basic LLM Setup ===")
    
    # Create LLM instance
    llm = Ollama(model="granite3.3:8b", temperature=0.7)
    
    # Simple invocation
    response = llm.invoke("What is LangChain in one sentence?")
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
    formatted = prompt.format(topic="machine learning")
    response = llm.invoke(formatted)
    print(f"Response: {response[:150]}...\n")


# ============================================================================
# 3. LLM CHAINS
# ============================================================================

def llm_chains(llm):
    """Combining prompts with LLMs using chains"""
    print("\n=== 3. LLM Chains ===")
    
    template = "Translate '{text}' to {language}."
    prompt = PromptTemplate(input_variables=["text", "language"], template=template)
    
    chain = LLMChain(llm=llm, prompt=prompt)
    
    result = chain.run(text="Hello, world!", language="Spanish")
    print(f"Translation: {result}\n")


# ============================================================================
# 4. FEW-SHOT PROMPTING
# ============================================================================

def few_shot_examples(llm):
    """Using FewShotPromptTemplate for examples"""
    print("\n=== 4. Few-Shot Prompting ===")
    
    examples = [
        {"word": "happy", "antonym": "sad"},
        {"word": "tall", "antonym": "short"},
    ]
    
    example_template = "Word: {word}\nAntonym: {antonym}"
    example_prompt = PromptTemplate(
        input_variables=["word", "antonym"],
        template=example_template
    )
    
    few_shot_prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix="Give antonyms:",
        suffix="\nWord: {input}\nAntonym:",
        input_variables=["input"]
    )
    
    formatted = few_shot_prompt.format(input="big")
    response = llm.invoke(formatted)
    print(f"Antonym: {response}\n")


# ============================================================================
# 5. CHAT TEMPLATES
# ============================================================================

def chat_templates(llm):
    """Using ChatPromptTemplate for structured conversations"""
    print("\n=== 5. Chat Templates ===")
    
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful coding assistant."),
        ("human", "Explain {concept} briefly.")
    ])
    
    chain = LLMChain(llm=llm, prompt=chat_prompt)
    result = chain.run(concept="list comprehension in Python")
    print(f"Explanation: {result[:150]}...\n")


# ============================================================================
# 6. OUTPUT PARSERS
# ============================================================================

def output_parsers(llm):
    """Parsing structured output from LLMs"""
    print("\n=== 6. Output Parsers ===")
    
    response_schemas = [
        ResponseSchema(name="language", description="The programming language"),
        ResponseSchema(name="difficulty", description="Difficulty level: easy/medium/hard")
    ]
    
    parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = parser.get_format_instructions()
    
    template = """Analyze this: {query}

{format_instructions}"""
    
    prompt = PromptTemplate(
        template=template,
        input_variables=["query"],
        partial_variables={"format_instructions": format_instructions}
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(query="Python programming")
    print(f"Structured output:\n{result}\n")


# ============================================================================
# 7. BATCH PROCESSING
# ============================================================================

def batch_processing(llm):
    """Processing multiple inputs efficiently"""
    print("\n=== 7. Batch Processing ===")
    
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
# 8. STREAMING
# ============================================================================

def streaming_responses(llm):
    """Streaming responses for real-time output"""
    print("\n=== 8. Streaming ===")
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
    few_shot_examples(llm)
    chat_templates(llm)
    output_parsers(llm)
    batch_processing(llm)
    streaming_responses(llm)
    
    print("="*60)
    print("✓ All examples completed!")
    print("="*60 + "\n")


def run_interactive():
    """Interactive menu to run examples individually"""
    llm = Ollama(model="granite3.3:8b", temperature=0.7)
    
    examples = {
        "1": ("Basic LLM Setup", lambda: basic_llm_setup()),
        "2": ("Prompt Templates", lambda: prompt_templates(llm)),
        "3": ("LLM Chains", lambda: llm_chains(llm)),
        "4": ("Few-Shot Prompting", lambda: few_shot_examples(llm)),
        "5": ("Chat Templates", lambda: chat_templates(llm)),
        "6": ("Output Parsers", lambda: output_parsers(llm)),
        "7": ("Batch Processing", lambda: batch_processing(llm)),
        "8": ("Streaming", lambda: streaming_responses(llm)),
    }
    
    while True:
        print("\n" + "="*60)
        print("LangChain Fundamentals - Choose Example:")
        print("="*60)
        for key, (name, _) in examples.items():
            print(f"{key}. {name}")
        print("9. Run All")
        print("0. Exit")
        print("="*60)
        
        choice = input("\nChoice: ").strip()
        
        if choice == "0":
            break
        elif choice == "9":
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

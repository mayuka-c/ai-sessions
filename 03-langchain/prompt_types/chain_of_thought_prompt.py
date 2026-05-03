from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def chain_of_thought_prompt(llm, user_question: str | None = None):
    '''
    CHAIN-OF-THOUGHT PROMPT (Step-by-Step Reasoning) - LangChain Implementation
    
    Demonstrates using LangChain to implement chain-of-thought prompting.
    
    Key LangChain Concepts:
    - PromptTemplate with reasoning instructions
    - LLMChain for structured reasoning flow
    - Template variables for flexible question input
    - Prompt engineering for step-by-step thinking
    
    Use Case: Complex reasoning tasks that benefit from intermediate steps.
    LangChain's templates make it easy to consistently apply CoT patterns.
    '''
    print(f"\n{'='*70}")
    print("3. CHAIN-OF-THOUGHT PROMPT - LangChain Reasoning Chains")
    print(f"{'='*70}")
    
    print("\n--- LangChain Components ---")
    print("1. PromptTemplate: Structures the reasoning request")
    print("2. LLMChain: Manages the reasoning flow")
    print("3. CoT Trigger: 'Let's think step by step' instruction")
    print("4. Template Variables: Flexible question input")
    
    if user_question:
        print("\n--- Single Question Mode ---")
        template = """Question: {question}

Let's approach this step by step:
1. First, identify what we know
2. Then, determine what we need to find
3. Finally, work through the solution

Answer:"""
        
        prompt = PromptTemplate(
            input_variables=["question"],
            template=template
        )
        
        print(f"Question: {user_question}")
        print("\n--- Prompt Template Structure ---")
        print("• Explicit step-by-step instructions")
        print("• Numbered reasoning framework")
        print("• Clear answer section")
        
        chain = LLMChain(llm=llm, prompt=prompt, verbose=False)
        
        print("\n--- Executing Chain ---")
        result = chain.run(question=user_question)
        
    else:
        print("\n--- Few-Shot CoT Mode ---")
        print("Demonstrating CoT with examples to teach the pattern")
        
        # Few-shot CoT template
        template = """Solve math word problems by thinking step by step.

Example 1:
Question: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?
Answer: Let's think step by step.
- Roger started with 5 balls
- He bought 2 cans with 3 balls each
- 2 cans × 3 balls = 6 balls
- Total: 5 + 6 = 11 balls
The answer is 11.

Now solve this problem:
Question: {question}
Answer: Let's think step by step."""
        
        prompt = PromptTemplate(
            input_variables=["question"],
            template=template
        )
        
        default_question = "The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?"
        print(f"Question: {default_question}")
        
        print("\n--- CoT Pattern Components ---")
        print("• Example with reasoning steps")
        print("• Explicit step markers")
        print("• Clear calculation breakdown")
        print("• Final answer statement")
        
        chain = LLMChain(llm=llm, prompt=prompt, verbose=False)
        
        print("\n--- Executing Chain ---")
        result = chain.run(question=default_question)
    
    print("\n--- Model Response ---")
    print(result)
    
    print("\n--- LangChain Benefits for CoT ---")
    print("✓ Consistent reasoning structure")
    print("✓ Reusable CoT templates")
    print("✓ Easy to switch between single/few-shot modes")
    print("✓ Can chain with other reasoning steps")
    print("✓ Trackable intermediate reasoning")
    print(f"{'='*70}\n")

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def comparative_demo(llm, user_prompt: str | None = None):
    '''
    COMPARATIVE DEMO - LangChain's Advantages in Prompt Engineering
    
    Demonstrates how LangChain makes it easy to compare different prompting techniques.
    
    Key LangChain Concepts:
    - Template reusability across techniques
    - Consistent chain interface
    - Easy A/B testing of prompts
    - Modular prompt components
    
    Use Case: Understanding how different prompt engineering techniques affect
    model responses. LangChain's structure makes comparison straightforward.
    '''
    print(f"\n{'='*70}")
    print("6. COMPARATIVE DEMO - LangChain Prompt Engineering Comparison")
    print(f"{'='*70}")
    
    prompt = user_prompt if user_prompt else "How do airplanes fly?"
    if user_prompt is None:
        print(f"Using default: {prompt}")
    
    print("\n--- LangChain Advantage: Easy Comparison ---")
    print("We'll run the same question through different prompt templates")
    print("to demonstrate how prompt engineering affects responses.")
    
    # Define different prompt templates
    techniques = {
        "1. Direct (Minimal)": {
            "template": "{question}",
            "description": "No prompt engineering - just the raw question"
        },
        "2. Instructional": {
            "template": "Instructions: Provide a clear, concise explanation.\n\nQuestion: {question}",
            "description": "Adds explicit instructions for clarity"
        },
        "3. Chain-of-Thought": {
            "template": "Question: {question}\n\nLet's think through this step by step:",
            "description": "Encourages reasoning process"
        },
        "4. Role-Based": {
            "template": "You are a physics teacher explaining concepts to students.\n\nQuestion: {question}\n\nExplanation:",
            "description": "Assigns expert persona"
        },
        "5. Structured Output": {
            "template": """Question: {question}

Please structure your answer as:
1. Simple explanation (1-2 sentences)
2. Key principles involved
3. Real-world application

Answer:""",
            "description": "Requests specific output format"
        }
    }
    
    print(f"\n{'='*70}")
    print(f"QUESTION: {prompt}")
    print(f"{'='*70}")
    
    results = {}
    
    for technique_name, config in techniques.items():
        print(f"\n{technique_name}")
        print(f"Description: {config['description']}")
        print("-" * 70)
        
        # Create prompt template
        prompt_template = PromptTemplate(
            input_variables=["question"],
            template=config["template"]
        )
        
        # Create chain
        chain = LLMChain(llm=llm, prompt=prompt_template, verbose=False)
        
        # Execute
        result = chain.run(question=prompt)
        results[technique_name] = result
        
        print(f"Response: {result[:200]}...")
        print()
    
    print(f"{'='*70}")
    print("COMPARISON SUMMARY")
    print(f"{'='*70}")
    
    print("\nKey Observations:")
    print("• Different techniques produce different response styles")
    print("• More structured prompts → more structured outputs")
    print("• Role-based prompts → domain-specific language")
    print("• CoT prompts → explicit reasoning steps")
    
    print("\n--- LangChain Benefits for Comparison ---")
    print("✓ Consistent interface across techniques")
    print("✓ Easy to create template variations")
    print("✓ Simple to run A/B tests")
    print("✓ Reusable prompt components")
    print("✓ Clear separation of prompt logic")
    print("✓ Easy to track and version prompts")
    
    print("\n--- Prompt Engineering Best Practices ---")
    print("1. Start simple, add complexity as needed")
    print("2. Be explicit about desired output format")
    print("3. Use examples when pattern is unclear")
    print("4. Assign roles for domain expertise")
    print("5. Request step-by-step for complex reasoning")
    print("6. Test multiple approaches and compare")
    
    print("\n--- LangChain Makes This Easy ---")
    print("• Templates are reusable and versionable")
    print("• Chains provide consistent execution")
    print("• Easy to swap and compare techniques")
    print("• Built-in tools for prompt optimization")
    
    print(f"\n{'='*70}")
    print("TIP: Try the same question with options 1-5 to see")
    print("how each technique affects the response!")
    print(f"{'='*70}\n")
    
    return results

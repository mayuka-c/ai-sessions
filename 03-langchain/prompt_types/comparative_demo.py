from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def comparative_demo(llm, user_prompt: str | None = None):
    '''
    COMPARATIVE DEMO - Comparing Different Prompting Techniques
    
    Use Case: Understanding how different prompt engineering techniques affect model responses.
    '''
    print(f"\n{'='*70}")
    print("6. COMPARATIVE DEMO")
    print(f"{'='*70}\n")
    
    prompt = user_prompt if user_prompt else "How do airplanes fly?"
    
    techniques = {
        "1. Direct": {
            "template": "{question}",
            "description": "No prompt engineering"
        },
        "2. Instructional": {
            "template": "Instructions: Provide a clear, concise explanation.\n\nQuestion: {question}",
            "description": "Explicit instructions"
        },
        "3. Chain-of-Thought": {
            "template": "Question: {question}\n\nLet's think through this step by step:",
            "description": "Encourages reasoning"
        },
        "4. Role-Based": {
            "template": "You are a physics teacher explaining concepts to students.\n\nQuestion: {question}\n\nExplanation:",
            "description": "Expert persona"
        },
        "5. Structured": {
            "template": """Question: {question}

Please structure your answer as:
1. Simple explanation (1-2 sentences)
2. Key principles involved
3. Real-world application

Answer:""",
            "description": "Specific output format"
        }
    }
    
    print(f"Question: {prompt}\n")
    print("="*70)
    
    for technique_name, config in techniques.items():
        print(f"\n{technique_name} - {config['description']}")
        print("-" * 70)
        
        prompt_template = PromptTemplate(
            input_variables=["question"],
            template=config["template"]
        )
        
        chain = prompt_template | llm | StrOutputParser()
        result = chain.invoke({"question": prompt})
        
        print(f"{result[:200]}...\n")
    
    print("="*70 + "\n")

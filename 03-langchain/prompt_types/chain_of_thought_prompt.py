from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def chain_of_thought_prompt(llm, user_question: str | None = None):
    '''
    CHAIN-OF-THOUGHT PROMPT (Step-by-Step Reasoning)
    
    Use Case: Complex reasoning tasks that benefit from intermediate steps.
    '''
    print(f"\n{'='*70}")
    print("3. CHAIN-OF-THOUGHT PROMPT")
    print(f"{'='*70}\n")
    
    if user_question:
        template = """Question: {question}

Let's approach this step by step:
1. First, identify what we know
2. Then, determine what we need to find
3. Finally, work through the solution

Answer:"""
        
        prompt = PromptTemplate(input_variables=["question"], template=template)
        chain = prompt | llm | StrOutputParser()
        result = chain.invoke({"question": user_question})
        
        print(f"Question: {user_question}")
    else:
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
        
        prompt = PromptTemplate(input_variables=["question"], template=template)
        default_question = "The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?"
        
        chain = prompt | llm | StrOutputParser()
        result = chain.invoke({"question": default_question})
        
        print(f"Question: {default_question}")
    
    print(f"\nResponse:\n{result}")
    print(f"{'='*70}\n")

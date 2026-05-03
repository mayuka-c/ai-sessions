from langchain.prompts import FewShotPromptTemplate, PromptTemplate

def few_shot_prompt(llm, user_text: str | None = None):
    '''
    FEW-SHOT PROMPT (Learning from Examples) - LangChain Implementation
    
    Demonstrates LangChain's FewShotPromptTemplate for structured few-shot learning.
    
    Key LangChain Concepts:
    - FewShotPromptTemplate: Specialized template for few-shot learning
    - Example Formatting: Consistent structure for training examples
    - Dynamic Example Selection: Can be extended with example selectors
    - Prefix/Suffix Pattern: Clear separation of context and task
    
    Use Case: Teaching the model a specific pattern or format through examples.
    LangChain's FewShotPromptTemplate makes it easy to manage and format examples.
    '''
    print(f"\n{'='*70}")
    print("2. FEW-SHOT PROMPT - LangChain FewShotPromptTemplate")
    print(f"{'='*70}")
    
    print("\n--- LangChain Components ---")
    print("1. FewShotPromptTemplate: Manages multiple examples")
    print("2. Example Template: Formats each example consistently")
    print("3. Prefix/Suffix: Provides context and task instruction")
    print("4. Example Separator: Controls spacing between examples")
    
    # Define examples as structured data
    examples = [
        {
            "text": "The food was delicious and the service was excellent.",
            "sentiment": "positive"
        },
        {
            "text": "The wait time was too long and the staff was rude.",
            "sentiment": "negative"
        },
        {
            "text": "The restaurant was okay, nothing special.",
            "sentiment": "neutral"
        }
    ]
    
    print("\n--- Example Data Structure ---")
    print(f"Number of examples: {len(examples)}")
    print(f"Example keys: {list(examples[0].keys())}")
    
    # Create example template - defines how each example is formatted
    example_template = """Text: {text}
Sentiment: {sentiment}"""
    
    example_prompt = PromptTemplate(
        input_variables=["text", "sentiment"],
        template=example_template
    )
    
    print("\n--- Example Template ---")
    print(example_template)
    
    # Create few-shot prompt template
    prefix = """Classify the sentiment of text as positive, negative, or neutral.

Here are some examples:"""
    
    suffix = """
Now classify this text:
Text: {input}
Sentiment:"""
    
    few_shot_prompt_template = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix=prefix,
        suffix=suffix,
        input_variables=["input"],
        example_separator="\n\n"
    )
    
    print("\n--- FewShotPromptTemplate Configuration ---")
    print(f"Prefix: Provides task context")
    print(f"Examples: {len(examples)} training examples")
    print(f"Suffix: Contains the actual task")
    print(f"Separator: '\\n\\n' between examples")
    
    final_text = user_text if user_text else "I absolutely loved the experience and will definitely return!"
    if user_text is None:
        print(f"\nUsing default text: {final_text}")
    
    # Format the complete prompt
    formatted_prompt = few_shot_prompt_template.format(input=final_text)
    
    print("\n--- Generated Prompt ---")
    print(formatted_prompt)
    
    print("\n--- Model Response ---")
    result = llm.invoke(formatted_prompt)
    print(f"Response: {result}")
    
    print("\n--- LangChain Benefits ---")
    print("✓ Structured example management")
    print("✓ Consistent formatting across examples")
    print("✓ Easy to add/remove examples")
    print("✓ Can integrate with ExampleSelector for dynamic selection")
    print("✓ Reusable across different inputs")
    print(f"{'='*70}\n")

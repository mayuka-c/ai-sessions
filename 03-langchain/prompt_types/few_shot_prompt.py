from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

def few_shot_prompt(llm, user_text: str | None = None):
    '''
    FEW-SHOT PROMPT (Learning from Examples)
    
    Use Case: Teaching the model a specific pattern or format through examples.
    '''
    print(f"\n{'='*70}")
    print("2. FEW-SHOT PROMPT")
    print(f"{'='*70}\n")
    
    examples = [
        {"text": "The food was delicious and the service was excellent.", "sentiment": "positive"},
        {"text": "The wait time was too long and the staff was rude.", "sentiment": "negative"},
        {"text": "The restaurant was okay, nothing special.", "sentiment": "neutral"}
    ]
    
    example_template = """Text: {text}
Sentiment: {sentiment}"""
    
    example_prompt = PromptTemplate(
        input_variables=["text", "sentiment"],
        template=example_template
    )
    
    few_shot_prompt_template = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix="Classify the sentiment of text as positive, negative, or neutral.\n\nHere are some examples:",
        suffix="\nNow classify this text:\nText: {input}\nSentiment:",
        input_variables=["input"],
        example_separator="\n\n"
    )
    
    final_text = user_text if user_text else "I absolutely loved the experience and will definitely return!"
    formatted_prompt = few_shot_prompt_template.format(input=final_text)
    
    result = llm.invoke(formatted_prompt)
    
    print(f"Input: {final_text}")
    print(f"\nResponse: {result}")
    print(f"{'='*70}\n")

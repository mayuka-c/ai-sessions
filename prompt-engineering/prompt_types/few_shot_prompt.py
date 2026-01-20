def few_shot_prompt(generator):
    '''
    FEW-SHOT PROMPT (Learning from Examples)
    
    Provide examples to guide the model's response format.
    By showing 2-5 examples, you teach the model the pattern you want it to follow.
    This is particularly effective for classification, formatting, or custom task patterns.
    
    Additional Example Prompts:
    - Text Classification: Show examples of categories and let model classify new items
    - Format Conversion: Show input-output pairs for desired transformation
    - Q&A Style: Provide question-answer examples for consistent response format
    '''
    print(f"\n{'='*70}")
    print("3. FEW-SHOT PROMPT (Learning from Examples)")
    print(f"{'='*70}")
    
    prompt = """Classify the sentiment as positive, negative, or neutral.

Example 1: The food was delicious and the service was excellent.
Sentiment: positive

Example 2: The wait time was too long and the staff was rude.
Sentiment: negative

Example 3: The restaurant was okay, nothing special.
Sentiment: neutral

Now classify: I absolutely loved the experience and will definitely return!
Sentiment:"""
    
    print("\nFew-Shot Prompt:")
    print(prompt)
    print("\n--- Model Response ---")
    result = generator(prompt, max_length=50, do_sample=False)
    print(f"Response: {result[0]['generated_text']}")
    print(f"{'='*70}\n")

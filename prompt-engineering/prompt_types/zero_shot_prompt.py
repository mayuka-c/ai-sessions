def zero_shot_prompt(generator):
    '''
    ZERO-SHOT PROMPT (No Examples Given)
    
    Ask the model to perform a task without providing examples.
    The model relies on its pre-trained knowledge to understand and complete the task.
    Useful for tasks the model has been trained on but you want to test without guidance.
    
    Additional Example Prompts:
    - "Translate to Spanish: Hello, how are you?"
    - "What is the capital of Germany?"
    - "Is this statement positive or negative: I hate waiting in long lines."
    '''
    print(f"\n{'='*70}")
    print("2. ZERO-SHOT PROMPT (No Examples Given)")
    print(f"{'='*70}")
    
    user_prompt = input("\nEnter your prompt (or press Enter for default): ").strip()
    if not user_prompt:
        user_prompt = "Classify the sentiment: This movie was absolutely fantastic! I loved every minute."
        print(f"Using default: {user_prompt}")
    
    print(f"\nPrompt: {user_prompt}")
    result = generator(user_prompt, max_length=50, do_sample=False)
    print(f"Response: {result[0]['generated_text']}")
    print(f"{'='*70}\n")

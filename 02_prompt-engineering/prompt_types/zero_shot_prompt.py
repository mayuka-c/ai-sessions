def zero_shot_prompt(generator, user_prompt: str | None = None):
    '''
    ZERO-SHOT PROMPT (No Examples Given)
    
    Ask the model to perform a task without providing examples.
    The model relies on its pre-trained knowledge to understand and complete the task.
    Useful for tasks the model has been trained on but you want to test without guidance.
    
    Additional Example Prompts:
    - "Is this statement positive or negative: I hate waiting in long lines."
    - "How do airplanes fly?"
    - "Translate to German: Hello, how are you?"
    '''
    print(f"\n{'='*70}")
    print("1. ZERO-SHOT PROMPT (No Examples Given)")
    print(f"{'='*70}")
    
    if not user_prompt:
        user_prompt = "Translate to Spanish: Hello, how are you?."
        print(f"Using default: {user_prompt}")
    
    print(f"\nPrompt: {user_prompt}")
    result = generator(user_prompt, max_length=100)
    print(f"Response: {result}")
    print(f"{'='*70}\n")

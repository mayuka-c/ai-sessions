def simple_prompt(generator):
    '''
    SIMPLE PROMPT (Direct Question)
    
    A straightforward question or statement without examples.
    This is the most basic form of prompting where you directly ask the model a question.
    '''
    print(f"\n{'='*70}")
    print("1. SIMPLE PROMPT (Direct Question)")
    print(f"{'='*70}")
    
    user_prompt = input("\nEnter your prompt (or press Enter for default): ").strip()
    if not user_prompt:
        user_prompt = "What is the capital of India?"
        print(f"Using default: {user_prompt}")
    
    print(f"\nPrompt: {user_prompt}")
    result = generator(user_prompt, max_length=100, do_sample=False)
    print(f"Response: {result[0]['generated_text']}")
    print(f"{'='*70}\n")

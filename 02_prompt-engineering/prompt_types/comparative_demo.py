def comparative_demo(generator, user_prompt: str | None = None):
    '''
    COMPARATIVE DEMO (Same Question, Different Techniques)
    
    See how different prompting styles affect the response.
    This demonstrates the impact of prompt engineering by applying multiple
    techniques to the same question and comparing results.
    
    Try asking the same question with different techniques:
    - Simple: "How do airplanes fly?"
    - Instructional: "Instructions: Explain in simple terms. How do airplanes fly?"
    - Chain-of-Thought: "How do airplanes fly? Let's think step by step."
    - Role-Based: "You are a physics teacher. How do airplanes fly?"
    '''
    print(f"\n{'='*70}")
    print("6. COMPARATIVE DEMO (Same Question, Different Techniques)")
    print(f"{'='*70}")
    
    prompt = user_prompt if user_prompt else "How do airplanes fly?"
    if user_prompt is None:
        print(f"Using default: {prompt}")
    
    print(f"\nPrompt: {prompt}")
    result = generator(prompt, max_length=100)
    print(f"Response: {result}")
    print(f"\n{'='*70}")
    print("TIP: Try the same question with different techniques (options 1-6)")
    print("to see how prompting style affects the response!")
    print(f"{'='*70}\n")

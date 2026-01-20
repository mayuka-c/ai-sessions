def comparative_demo(generator):
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
    print("7. COMPARATIVE DEMO (Same Question, Different Techniques)")
    print(f"{'='*70}")
    
    prompt = input("\nEnter a prompt to test (or press Enter for default): ").strip()
    if not prompt:
        prompt = "How do airplanes fly?"
        print(f"Using default: {prompt}")
    
    print(f"\nPrompt: {prompt}")
    result = generator(prompt, max_length=100, do_sample=False)
    print(f"Response: {result[0]['generated_text']}")
    print(f"\n{'='*70}")
    print("TIP: Try the same question with different techniques (options 1-6)")
    print("to see how prompting style affects the response!")
    print(f"{'='*70}\n")

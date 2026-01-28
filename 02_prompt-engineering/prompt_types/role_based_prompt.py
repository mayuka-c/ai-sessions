def role_based_prompt(generator, user_question: str | None = None):
    '''
    ROLE-BASED PROMPT (Assign a Persona)
    
    Instruct the model to respond as a specific character or expert.
    Starting with "You are a [role]..." helps the model adopt a specific perspective.
    Useful for getting domain-specific answers or controlling response style.
    
    Additional Example Prompts:
    - "You are a professional chef. Question: How do I make the perfect dosa?"
    - "You are a fitness trainer. Question: What are the benefits of regular exercise?"
    - "You are a poet. Write a short poem about nature."
    - "You are a scientist. Explain how vaccines work."
    '''
    print(f"\n{'='*70}")
    print("5. ROLE-BASED PROMPT (Assign a Persona)")
    print(f"{'='*70}")
    
    question = user_question if user_question else "What is photosynthesis?"
    if user_question is None:
        print(f"Using default question: {question}")
    prompt = f"""You are a helpful teacher explaining concepts to students.

Question: {question}

Answer:"""
    
    print("\nRole-Based Prompt:")
    print(prompt)
    print("\n--- Model Response ---")
    result = generator(prompt, max_length=150)
    print(f"Response: {result}")
    print(f"{'='*70}\n")

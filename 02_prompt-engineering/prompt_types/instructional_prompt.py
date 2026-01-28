def instructional_prompt(generator, user_text: str | None = None):
    '''
    INSTRUCTIONAL PROMPT (Clear Directives)
    
    Give explicit instructions about format, tone, or constraints.
    Use clear directives like "Summarize in 3 bullet points" or "Explain like I'm 10 years old".
    This helps control the output structure and style precisely.
    
    Additional Example Prompts:
    - Tone Control: "Instructions: Explain the following in simple terms that a 
      10-year-old would understand. Text: [complex topic]"
    - Length Constraints: "Instructions: Summarize in exactly 2 sentences."
    - Format Specific: "Instructions: List the main points as numbered items."
    '''
    print(f"\n{'='*70}")
    print("4. INSTRUCTIONAL PROMPT (Clear Directives)")
    print(f"{'='*70}")
    
    if not user_text:
      user_text = (
        "Artificial intelligence is transforming industries worldwide. "
        "Machine learning algorithms can analyze vast amounts of data to identify patterns and make predictions. "
        "Deep learning, a subset of machine learning, uses neural networks with multiple layers to process complex information. "
        "Natural language processing enables computers to understand and generate human language. "
        "Computer vision allows machines to interpret and analyze visual information from the world."
      )
      print("Using default source text.")
    prompt = f"""Instructions: Summarize the following text.

Write exactly three sentences.
  Text: {user_text}"""
    
    print("\nInstructional Prompt:")
    print(prompt)
    print("\n--- Model Response ---")
    result = generator(prompt, max_length=150)
    print(f"Response: {result}")
    print(f"{'='*70}\n")

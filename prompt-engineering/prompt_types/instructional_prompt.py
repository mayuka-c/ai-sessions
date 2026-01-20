def instructional_prompt(generator):
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
    print("5. INSTRUCTIONAL PROMPT (Clear Directives)")
    print(f"{'='*70}")
    
    prompt = """Instructions: Summarize the following text in exactly 3 bullet points.

Text: Artificial intelligence is transforming industries worldwide. Machine learning algorithms can analyze vast amounts of data to identify patterns and make predictions. Deep learning, a subset of machine learning, uses neural networks with multiple layers to process complex information. Natural language processing enables computers to understand and generate human language. Computer vision allows machines to interpret and analyze visual information from the world.

Summary:"""
    
    print("\nInstructional Prompt:")
    print(prompt)
    print("\n--- Model Response ---")
    result = generator(prompt, max_length=150, do_sample=False)
    print(f"Response: {result[0]['generated_text']}")
    print(f"{'='*70}\n")

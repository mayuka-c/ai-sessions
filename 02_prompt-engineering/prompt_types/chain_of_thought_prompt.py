def chain_of_thought_prompt(generator, user_question: str | None = None):
    '''
    CHAIN-OF-THOUGHT PROMPT (Step-by-Step Reasoning)
    
    Encourage the model to show its reasoning process.
    Phrases like "Let's think step by step" help the model break down complex problems.
    Particularly effective for math, logic, and multi-step reasoning tasks.
    
    Additional Example Prompts:
    - Logic: "If all roses are flowers and some flowers fade quickly, can we conclude 
      that some roses fade quickly? Let's think step by step."
    - Word Problems: Multi-step math calculations with intermediate reasoning
    - Causal Reasoning: Explain cause-and-effect relationships step by step
    '''
    print(f"\n{'='*70}")
    print("3. CHAIN-OF-THOUGHT PROMPT (Step-by-Step Reasoning)")
    print(f"{'='*70}")
    
    if user_question:
      prompt = f"Q: {user_question}\nA: Let's think step by step."
    else:
      prompt = """Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?
  A: Let's think step by step. Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11.

  Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?
  A: Let's think step by step."""
      print("Using default chain-of-thought examples.")
    
    print("\nChain-of-Thought Prompt:")
    print(prompt)
    print("\n--- Model Response ---")
    result = generator(prompt, max_length=128)
    print(f"Response: {result}")
    print(f"{'='*70}\n")

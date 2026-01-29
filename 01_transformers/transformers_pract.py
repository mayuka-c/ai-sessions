from transformers import pipeline, AutoTokenizer, GenerationConfig

def create_simple_llm():
    """Create a simple language model pipeline"""
    # Choose a small, fast GPT-2 variant suitable for demos/tests
    model_name = "distilgpt2"

    # Load the matching tokenizer (handles text ⇄ token IDs)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Provide a pad token (GPT-2 family lacks one); using EOS avoids warnings/errors
    tokenizer.pad_token = tokenizer.eos_token

    # Build a high-level text-generation pipeline with the model + tokenizer
    llm_pipeline = pipeline("text-generation", model=model_name, tokenizer=tokenizer)
    
    return llm_pipeline, tokenizer

def generate_text(generator, prompt):
    """Generate text from a prompt"""
    print(f"\n{'='*60}")
    print("GENERATING TEXT")
    print(f"{'='*60}")
    print(f"Input Prompt: {prompt}\n")
    # Use a GenerationConfig exclusively to avoid deprecation warnings
    # about mixing generation_config with explicit generation parameters.
    gen_config = GenerationConfig(
        max_new_tokens=500,
        temperature=0.7,        # Controls randomness (0.7-0.9 is good for creative text)
        top_p=0.95,             # Nucleus sampling - consider tokens that make up 95% probability
        repetition_penalty=1.2, # Penalize repeated tokens
        do_sample=True,         # Enable sampling
        # Explicitly unset max_length to avoid the "both set" warning
        max_length=None,
    )

    results = generator(prompt, generation_config=gen_config)
    
    print(f"\nGenerated Text:\n\n{results[0]['generated_text']}")
    print(f"{'='*60}\n")

def tokenization_demo(tokenizer, text):
    """Demonstrate tokenization with encode and decode"""
    print(f"\n{'='*60}")
    print("TOKENIZATION DEMO")
    print(f"{'='*60}")
    print(f"Original Text: {text}\n")
    
    # Encoding: Convert text to token IDs
    print("--- ENCODING (Text → Token IDs) ---")
    token_ids = tokenizer.encode(text)
    print(f"Token IDs: {token_ids}")
    print(f"Number of tokens: {len(token_ids)}")
    
    # Show each token with its ID
    print("\n--- Token Breakdown ---")
    tokens = tokenizer.tokenize(text) # helpful to see how text gets segmented
    print(f"Tokens: {tokens}")
    for i, (token, token_id) in enumerate(zip(tokens, token_ids)):
        print(f"  {i+1}. Token: '{token}' → ID: {token_id}")
    
    # Decoding: Convert token IDs back to text
    print("\n--- DECODING (Token IDs → Text) ---")
    decoded_text = tokenizer.decode(token_ids)
    print(f"Decoded Text: {decoded_text}")
    
    # Explanation
    print("\n--- EXPLANATION ---")
    print("• Encoding: Transforms text into numerical token IDs that the model understands")
    print("• Each token represents a word, subword, or character")
    print("• Token IDs are used as input to the neural network")
    print("• Decoding: Converts token IDs back to human-readable text")
    print("• This process allows models to work with text numerically")
    print(f"{'='*60}\n")

    

def display_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("TRANSFORMERS PRACTICE - INTERACTIVE MENU")
    print("="*60)
    print("1. Generate Text from Custom Prompt")
    print("2. Tokenization Demo (Encode & Decode)")
    print("3. Exit")
    print("="*60)

def main():
    """Main function to run the interactive program"""
    print("\nInitializing models...")
    generator, tokenizer = create_simple_llm()
    print("Models loaded successfully!\n")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            prompt = input("\nEnter your prompt (Press Enter to use default): ").strip()
            if not prompt:
                prompt = "Once upon a time in a land far, far away"
                print(f"No prompt entered. Using default: {prompt}")
            generate_text(generator, prompt)
            
        elif choice == '2':
            text = input("\nEnter text to tokenize (Press Enter to use default): ").strip()
            if not text:
                text = "Hello, how are you today?"
                print(f"No text entered. Using default: {text}")
            tokenization_demo(tokenizer, text)
            
        elif choice == '3':
            print("\nThank you for using Transformers Practice!")
            print("Goodbye! 👋\n")
            break
            
        else:
            print("\nInvalid choice! Please enter a number between 1 and 3.\n")

if __name__ == "__main__":
    main()

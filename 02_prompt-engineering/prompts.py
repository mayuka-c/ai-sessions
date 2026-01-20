from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from prompt_types import (
    simple_prompt,
    zero_shot_prompt,
    few_shot_prompt,
    chain_of_thought_prompt,
    instructional_prompt,
    role_based_prompt,
    comparative_demo
)

def initialize_model():
    """Initialize the FLAN-T5 model and tokenizer"""
    print("\nLoading google/flan-t5-small model...")
    model_name = "google/flan-t5-small"
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    generator = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    
    print("Model loaded successfully!\n")
    return generator, tokenizer

def display_menu():
    """Display the main menu"""
    print("\n" + "="*70)
    print("PROMPT ENGINEERING WITH FLAN-T5 - INTERACTIVE DEMO")
    print("="*70)
    print("1. Simple Prompt (Direct Question)")
    print("2. Zero-Shot Prompt (No Examples)")
    print("3. Few-Shot Prompt (Learning from Examples)")
    print("4. Chain-of-Thought Prompt (Step-by-Step Reasoning)")
    print("5. Instructional Prompt (Clear Directives)")
    print("6. Role-Based Prompt (Assign a Persona)")
    print("7. Comparative Demo (Compare Techniques)")
    print("8. Exit")
    print("="*70)

def main():
    """Main function to run the interactive program"""
    print("\n" + "="*70)
    print("PROMPT ENGINEERING DEMONSTRATION")
    print("="*70)
    print("This program demonstrates various prompting techniques using")
    print("the google/flan-t5-small model.")
    print("="*70)
    
    generator, tokenizer = initialize_model()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            simple_prompt(generator)
        elif choice == '2':
            zero_shot_prompt(generator)
        elif choice == '3':
            few_shot_prompt(generator)
        elif choice == '4':
            chain_of_thought_prompt(generator)
        elif choice == '5':
            instructional_prompt(generator)
        elif choice == '6':
            role_based_prompt(generator)
        elif choice == '7':
            comparative_demo(generator)
        elif choice == '8':
            print("\n" + "="*70)
            print("Thank you for exploring prompt engineering techniques!")
            print("Key Takeaway: The way you phrase your prompt significantly")
            print("impacts the model's response. Experiment with different")
            print("techniques to get the best results!")
            print("="*70 + "\n")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 8.\n")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

import os
import argparse
from langchain_community.llms import Ollama
from prompt_types import (
    zero_shot_prompt,
    few_shot_prompt,
    chain_of_thought_prompt,
    instructional_prompt,
    role_based_prompt,
    comparative_demo
)

def initialize_model(model_name: str | None = None):
    """Initialize Ollama LLM with the specified model.
    
    Args:
        model_name: Name of the Ollama model to use (default: granite3.3:8b)
    
    Returns:
        Ollama LLM instance
    """
    if model_name is None:
        model_name = os.environ.get("MODEL_NAME", "granite3.3:8b")
    
    llm = Ollama(
        model=model_name,
        temperature=0.7,
    )
    
    return llm

def parse_args():
    parser = argparse.ArgumentParser(description="Prompt Engineering Demo with LangChain and Granite")
    parser.add_argument(
        "--model",
        default="granite3.3:8b",
        help="Ollama model to use (default: granite3.3:8b)",
    )
    return parser.parse_args()

def display_menu():
    """Display the main menu"""
    print("\n" + "="*70)
    print("PROMPT ENGINEERING WITH LANGCHAIN & GRANITE - INTERACTIVE DEMO")
    print("="*70)
    print("1. Zero-Shot Prompt (No Examples)")
    print("2. Few-Shot Prompt (Learning from Examples)")
    print("3. Chain-of-Thought Prompt (Step-by-Step Reasoning)")
    print("4. Instructional Prompt (Clear Directives)")
    print("5. Role-Based Prompt (Assign a Persona)")
    print("6. Comparative Demo (Compare Techniques)")
    print("7. Exit")
    print("="*70)

def read_multiline_input(message: str) -> str:
    """Read multi-line input from the user until EOF (Ctrl-D).
    
    Behavior:
    - Paste/type lines and press Ctrl-D to finish.
    - Press Ctrl-D immediately (on an empty first line) to use the default.
    
    Returns the collected text as a single string. An empty string indicates default.
    """
    print("\n" + message)
    print("(Finish with Ctrl-D. Press Ctrl-D immediately to use default.)")
    lines: list[str] = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        lines.append(line)
    return "\n".join(lines).strip()

def main():
    """Main function to run the interactive program"""
    print("\n" + "="*70)
    print("PROMPT ENGINEERING DEMONSTRATION - LANGCHAIN IMPLEMENTATION")
    print("="*70)
    args = parse_args()
    
    chosen_model = args.model or os.environ.get("MODEL_NAME", "granite3.3:8b")
    print(f"This program demonstrates various prompting techniques using")
    print(f"LangChain with {chosen_model}")
    print("="*70)
    
    llm = initialize_model(chosen_model)
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            user_prompt = read_multiline_input(
                "Enter your prompt (multi-line supported). Finish with Ctrl-D; Ctrl-D immediately uses default."
            )
            zero_shot_prompt(llm, user_prompt if user_prompt else None)
        elif choice == '2':
            to_classify = read_multiline_input(
                "Enter text to classify (multi-line supported). Finish with Ctrl-D; Ctrl-D immediately uses default."
            )
            few_shot_prompt(llm, to_classify if to_classify else None)
        elif choice == '3':
            question = read_multiline_input(
                "Enter a question/problem (multi-line supported). Finish with Ctrl-D; Ctrl-D immediately uses default."
            )
            chain_of_thought_prompt(llm, question if question else None)
        elif choice == '4':
            source_text = read_multiline_input(
                "Paste the source text to summarize (multi-line). Finish with Ctrl-D; Ctrl-D immediately uses default."
            )
            instructional_prompt(llm, source_text if source_text else None)
        elif choice == '5':
            question = read_multiline_input(
                "Enter the question/task for the role (multi-line supported). Finish with Ctrl-D; Ctrl-D immediately uses default."
            )
            role_based_prompt(llm, question if question else None)
        elif choice == '6':
            test_prompt = read_multiline_input(
                "Enter a prompt to test (multi-line supported). Finish with Ctrl-D; Ctrl-D immediately uses default."
            )
            comparative_demo(llm, test_prompt if test_prompt else None)
        elif choice == '7':
            print("\n" + "="*70)
            print("Thank you for exploring prompt engineering techniques!")
            print("Key Takeaway: The way you phrase your prompt significantly")
            print("impacts the model's response. Experiment with different")
            print("techniques to get the best results!")
            print("="*70 + "\n")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 7.\n")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

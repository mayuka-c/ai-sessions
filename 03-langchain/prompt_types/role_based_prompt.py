from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain

def role_based_prompt(llm, user_question: str | None = None):
    '''
    ROLE-BASED PROMPT (Assign a Persona) - LangChain Implementation
    
    Demonstrates LangChain's ChatPromptTemplate with system and human messages.
    
    Key LangChain Concepts:
    - ChatPromptTemplate: Structured chat-based prompts
    - SystemMessagePromptTemplate: Defines the AI's role/persona
    - HumanMessagePromptTemplate: User's actual query
    - Message separation: Clear distinction between role and task
    
    Use Case: When you need the model to adopt a specific perspective or expertise.
    LangChain's chat templates provide clean separation of role definition and queries.
    '''
    print(f"\n{'='*70}")
    print("5. ROLE-BASED PROMPT - LangChain Chat Templates")
    print(f"{'='*70}")
    
    print("\n--- LangChain Components ---")
    print("1. ChatPromptTemplate: Manages multi-message prompts")
    print("2. SystemMessage: Defines AI role and behavior")
    print("3. HumanMessage: Contains user's actual query")
    print("4. Message Chain: Structured conversation flow")
    
    question = user_question if user_question else "What is photosynthesis?"
    if user_question is None:
        print(f"Using default question: {question}")
    
    # Define system message (role definition)
    system_template = """You are a helpful and patient teacher who excels at explaining complex concepts to students.

Your teaching style:
- Break down complex topics into simple, understandable parts
- Use analogies and real-world examples
- Encourage curiosity and questions
- Adapt explanations to the student's level
- Make learning engaging and fun

Remember: Your goal is to help students truly understand, not just memorize."""
    
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    
    print("\n--- System Message (Role Definition) ---")
    print("Defines the AI's persona, expertise, and behavior")
    print(f"Length: {len(system_template)} characters")
    print("\nKey role attributes:")
    print("• Persona: Patient teacher")
    print("• Expertise: Explaining complex concepts")
    print("• Style: Simple, engaging, example-driven")
    
    # Define human message (actual query)
    human_template = """Please explain the following concept to me:

{question}

Provide a clear, educational explanation that helps me understand."""
    
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    
    print("\n--- Human Message (Query) ---")
    print("Contains the actual question or task")
    print(f"Question: {question}")
    
    # Combine into chat prompt template
    chat_prompt = ChatPromptTemplate.from_messages([
        system_message_prompt,
        human_message_prompt
    ])
    
    print("\n--- Chat Prompt Structure ---")
    print("Message 1: System (Role)")
    print("Message 2: Human (Query)")
    print("This separation allows:")
    print("  • Consistent role across queries")
    print("  • Easy role modification")
    print("  • Clear context boundaries")
    
    # Create chain
    chain = LLMChain(llm=llm, prompt=chat_prompt, verbose=False)
    
    print("\n--- Executing Chain ---")
    result = chain.run(question=question)
    
    print("\n--- Model Response ---")
    print(result)
    
    print("\n--- LangChain Benefits for Role-Based Prompts ---")
    print("✓ Clean separation of role and query")
    print("✓ Reusable role definitions")
    print("✓ Easy to swap personas")
    print("✓ Structured message history")
    print("✓ Compatible with chat models")
    print("✓ Maintains context across conversations")
    
    print("\n--- Try Different Roles ---")
    print("Examples you could try:")
    print("• 'You are a professional chef...'")
    print("• 'You are a fitness trainer...'")
    print("• 'You are a scientist...'")
    print("• 'You are a poet...'")
    print(f"{'='*70}\n")

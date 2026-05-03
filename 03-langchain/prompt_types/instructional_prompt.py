from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

def instructional_prompt(llm, user_text: str | None = None):
    '''
    INSTRUCTIONAL PROMPT (Clear Directives) - LangChain Implementation
    
    Demonstrates LangChain's structured output parsing with clear instructions.
    
    Key LangChain Concepts:
    - PromptTemplate with explicit instructions
    - OutputParser for structured responses
    - ResponseSchema for defining expected output format
    - Format instructions injection
    
    Use Case: When you need specific output format or structure.
    LangChain's output parsers ensure consistent, parseable responses.
    '''
    print(f"\n{'='*70}")
    print("4. INSTRUCTIONAL PROMPT - LangChain Output Parsers")
    print(f"{'='*70}")
    
    print("\n--- LangChain Components ---")
    print("1. PromptTemplate: Structures the instruction")
    print("2. ResponseSchema: Defines expected output fields")
    print("3. StructuredOutputParser: Parses model output")
    print("4. Format Instructions: Auto-generated formatting guide")
    
    if not user_text:
        user_text = (
            "Artificial intelligence is transforming industries worldwide. "
            "Machine learning algorithms can analyze vast amounts of data to identify patterns and make predictions. "
            "Deep learning, a subset of machine learning, uses neural networks with multiple layers to process complex information. "
            "Natural language processing enables computers to understand and generate human language. "
            "Computer vision allows machines to interpret and analyze visual information from the world."
        )
        print("Using default source text.")
    
    # Define the expected output structure
    response_schemas = [
        ResponseSchema(
            name="summary",
            description="A concise summary of the text in exactly 3 sentences"
        ),
        ResponseSchema(
            name="key_topics",
            description="List of 3-5 main topics covered in the text"
        ),
        ResponseSchema(
            name="word_count",
            description="Approximate word count of the summary"
        )
    ]
    
    print("\n--- Output Schema Definition ---")
    for schema in response_schemas:
        print(f"• {schema.name}: {schema.description}")
    
    # Create output parser
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    
    # Get format instructions
    format_instructions = output_parser.get_format_instructions()
    
    print("\n--- Auto-Generated Format Instructions ---")
    print(format_instructions[:200] + "...")
    
    # Create prompt template with format instructions
    template = """Analyze and summarize the following text according to these instructions:

{format_instructions}

Text to analyze:
{text}

Provide your response in the specified format:"""
    
    prompt = PromptTemplate(
        input_variables=["text"],
        partial_variables={"format_instructions": format_instructions},
        template=template
    )
    
    print("\n--- Prompt Template Structure ---")
    print("• Format instructions automatically injected")
    print("• Clear task definition")
    print("• Structured output request")
    
    # Create chain
    chain = LLMChain(llm=llm, prompt=prompt, verbose=False)
    
    print("\n--- Executing Chain ---")
    print(f"Input text length: {len(user_text)} characters")
    
    result = chain.run(text=user_text)
    
    print("\n--- Raw Model Response ---")
    print(result)
    
    # Try to parse the output
    print("\n--- Attempting to Parse Output ---")
    try:
        parsed_output = output_parser.parse(result)
        print("✓ Successfully parsed!")
        print("\nParsed Structure:")
        for key, value in parsed_output.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"⚠ Parsing note: {str(e)[:100]}")
        print("(Model output may need adjustment for strict parsing)")
    
    print("\n--- LangChain Benefits for Instructions ---")
    print("✓ Structured output definitions")
    print("✓ Automatic format instruction generation")
    print("✓ Built-in output parsing")
    print("✓ Type-safe output handling")
    print("✓ Consistent response structure")
    print("✓ Easy validation and error handling")
    print(f"{'='*70}\n")

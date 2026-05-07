from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

def instructional_prompt(llm, user_text: str | None = None):
    '''
    INSTRUCTIONAL PROMPT (Clear Directives)
    
    Use Case: When you need specific output format or structure.
    '''
    print(f"\n{'='*70}")
    print("4. INSTRUCTIONAL PROMPT")
    print(f"{'='*70}\n")
    
    if not user_text:
        user_text = (
            "Artificial intelligence is transforming industries worldwide. "
            "Machine learning algorithms can analyze vast amounts of data to identify patterns and make predictions. "
            "Deep learning, a subset of machine learning, uses neural networks with multiple layers to process complex information. "
            "Natural language processing enables computers to understand and generate human language. "
            "Computer vision allows machines to interpret and analyze visual information from the world."
        )
    
    class TextAnalysis(BaseModel):
        summary: str = Field(description="A concise summary of the text in exactly 3 sentences")
        key_topics: list[str] = Field(description="List of 3-5 main topics covered in the text")
        word_count: int = Field(description="Approximate word count of the summary")
    
    output_parser = PydanticOutputParser(pydantic_object=TextAnalysis)
    format_instructions = output_parser.get_format_instructions()
    
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
    
    chain = prompt | llm | output_parser
    result = chain.invoke({"text": user_text})
    
    print(f"Input text length: {len(user_text)} characters\n")
    print("Parsed Structure:")
    print(f"  summary: {result.summary}")
    print(f"  key_topics: {result.key_topics}")
    print(f"  word_count: {result.word_count}")
    print(f"{'='*70}\n")

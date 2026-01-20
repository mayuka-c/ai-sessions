"""
Prompt Engineering Types Module

This module contains different prompting techniques for LLMs.
"""

from .simple_prompt import simple_prompt
from .zero_shot_prompt import zero_shot_prompt
from .few_shot_prompt import few_shot_prompt
from .chain_of_thought_prompt import chain_of_thought_prompt
from .instructional_prompt import instructional_prompt
from .role_based_prompt import role_based_prompt
from .comparative_demo import comparative_demo

__all__ = [
    'simple_prompt',
    'zero_shot_prompt',
    'few_shot_prompt',
    'chain_of_thought_prompt',
    'instructional_prompt',
    'role_based_prompt',
    'comparative_demo'
]

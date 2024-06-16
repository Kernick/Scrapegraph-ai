"""
MergeExploreGraphsNode Module
"""

# Imports from standard library
from typing import List, Optional

# Imports from Langchain
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from tqdm import tqdm
from ..models import Ollama
from .base_node import BaseNode


class MergeExploreGraphsNode(BaseNode):
    """
    A node that generates an answer using a large language model (LLM) based on the user's input
    and the content extracted from a webpage. It constructs a prompt from the user's input
    and the scraped content, feeds it to the LLM, and parses the LLM's response to produce
    an answer.

    Attributes:
        llm_model: An instance of a language model client, configured for generating answers.
        verbose (bool): A flag indicating whether to show print statements during execution.

    Args:
        input (str): Boolean expression defining the input keys needed from the state.
        output (List[str]): List of output keys to be updated in the state.
        node_config (dict): Additional configuration for the node.
        node_name (str): The unique identifier name for the node, defaulting to "GenerateAnswer".
    """

    def __init__(
        self,
        input: str,
        output: List[str],
        node_config: Optional[dict] = None,
        node_name: str = "MergeExploreGraph",
    ):
        super().__init__(node_name, "node", input, output, 2, node_config)

        self.llm_model = node_config["llm_model"]

        if isinstance(node_config["llm_model"], Ollama):
            self.llm_model.format="json"

        self.verbose = (
            True if node_config is None else node_config.get("verbose", False)
        )

    def execute(self, state: dict) -> dict:
        """
        Generates an answer by constructing a prompt from the user's input and the scraped
        content, querying the language model, and parsing its response.

        Args:
            state (dict): The current state of the graph. The input keys will be used
                            to fetch the correct data from the state.

        Returns:
            dict: The updated state with the output key containing the generated answer.

        Raises:
            KeyError: If the input keys are not found in the state, indicating
                      that the necessary information for generating an answer is missing.
        """

        self.logger.info(f"--- Executing {self.node_name} Node ---")

        template_answer = ""

        answers = str(state.get("answer"))
        relevant_links = str(state.get("relevant_links"))
        answer = {}

        merge_prompt = PromptTemplate(
                template=template_answer,
                 #input_variables=["context", "question"],
                 #partial_variables={"format_instructions": format_instructions},
            )

         #answer = merge_prompt.invoke({"question": user_prompt})

        state.update({"relevant_links": "TODO"})
        state.update({"answer": "TODO"})
        return state

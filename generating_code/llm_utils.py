"""LLM utilities for multi-provider support with Langchain.

This module provides:
- Multi-provider LLM client setup (Anthropic, OpenAI, Google)
- Cost tracking for LLM calls
- Message format conversion
- Common helper functions for LLM interactions
"""

import json
import random

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.callbacks import BaseCallbackHandler
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_google_vertexai import ChatVertexAI


# Model name mappings
MODELS = {
    # Anthropic models
    "haiku": "claude-3-5-haiku-20241022",
    "sonnet": "claude-3-5-sonnet-20241022",
    "sonnet_4": "claude-4-sonnet-20250514",
    "opus_4": "claude-opus-4-20250514",
}


def get_client(model, timeout=300, **kwargs):
    """Get configured LLM client for the specified model.

    Args:
        model: Model name or alias (e.g., 'haiku', 'gpt-5.2', 'gemini-2.5-pro')
        timeout: Request timeout in seconds
        **kwargs: Additional arguments passed to the client

    Returns:
        Configured Langchain chat client
    """
    if model in MODELS:
        model_name = MODELS[model]
    else:
        model_name = model

    # Anthropic models
    if 'claude' in model_name or model in ["haiku", "sonnet", "sonnet_4", "opus_4"]:
        return ChatAnthropic(model=model_name, timeout=timeout, **kwargs)
    # OpenAI models
    elif 'gpt' in model or (model[0] == 'o' and model[1] != 'p'):
        return ChatOpenAI(model=model_name, timeout=timeout, **kwargs)
    # Google models
    elif model.startswith("gemini"):
        return ChatVertexAI(model=model_name, timeout=timeout, **kwargs)
    else:
        raise ValueError(f"Unknown model: {model}")


def make_langchain_messages(messages):
    """Convert message dicts to Langchain message format.

    Args:
        messages: List of dicts with 'role' and 'content' keys

    Returns:
        List of Langchain message objects
    """
    MESSAGE_TYPES = {
        "user": HumanMessage,
        "assistant": AIMessage,
        "system": SystemMessage
    }

    lc_messages = []
    for msg in messages:
        content = msg["content"]
        if isinstance(content, list):
            content = "\n".join(
                item["text"] for item in content
                if isinstance(item, dict) and item.get("type") == "text"
            )

        message_class = MESSAGE_TYPES.get(msg["role"])
        if message_class:
            lc_messages.append(message_class(content=content))

    return lc_messages


class CostTracker(BaseCallbackHandler):
    """Track token usage and costs for multi-provider LLM calls.

    Usage:
        tracker = CostTracker('gpt-5.2')
        response = client.invoke(messages, config={"callbacks": [tracker]})
        tracker.print_summary()
    """

    # (input, output) cost per million tokens
    COSTS = {
        # Anthropic models: https://www.anthropic.com/pricing#api
        'haiku': (0.8, 4.0),
        'sonnet': (3.0, 15.0),
        'sonnet_4': (3.0, 15.0),
        'opus_4': (15.0, 75.0),

        # OpenAI models: https://openai.com/api/pricing/
        'gpt_4o': (2.5, 10.0),
        'o4_mini': (1.1, 4.4),
        'o3': (2.0, 8.0),
        'gpt-5': (1.25, 10.0),
        'gpt-5.1': (1.25, 10.0),
        'gpt-5.2': (1.75, 14.0),
        'gpt-5-mini': (0.25, 2.0),
        'gpt-5-nano': (0.05, 0.4),

        # Google models: https://ai.google.dev/gemini-api/docs/pricing
        'gemini-2.5-pro': (1.25, 10.0),
        'gemini-2.5-flash': (0.30, 2.50),
        'gemini-2.5-flash-lite': (0.075, 0.3),
    }

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.input_tokens = 0
        self.output_tokens = 0
        self.requests = 0
        self.debug = False

    def on_llm_start(self, serialized, prompts, **kwargs):
        """Track when request starts."""
        if self.debug:
            print(f"LLM request starting for {self.model}")

    def on_llm_end(self, response, **kwargs):
        """Extract usage from Langchain response."""
        self.requests += 1
        usage_data = None

        # Check llm_output (OpenAI format)
        if hasattr(response, 'llm_output') and response.llm_output:
            llm_out = response.llm_output
            usage_data = (llm_out.get('usage') or llm_out.get('token_usage') or
                          (llm_out if 'prompt_tokens' in llm_out else None))

        # Check response_metadata.usage
        if not usage_data and hasattr(response, 'response_metadata'):
            usage_data = response.response_metadata.get('usage', {})

        # Check generations[0].generation_info.usage
        if not usage_data and response.generations:
            for gen in response.generations:
                if hasattr(gen[0], 'generation_info') and gen[0].generation_info:
                    usage_data = gen[0].generation_info.get('usage', {})
                    if usage_data:
                        break

        if usage_data:
            # Handle different provider formats
            if 'input_tokens' in usage_data:  # Anthropic
                self.input_tokens += usage_data.get('input_tokens', 0)
                self.output_tokens += usage_data.get('output_tokens', 0)
            elif 'prompt_tokens' in usage_data:  # OpenAI
                self.input_tokens += usage_data.get('prompt_tokens', 0)
                self.output_tokens += usage_data.get('completion_tokens', 0)
            elif 'prompt_token_count' in usage_data:  # Google
                self.input_tokens += usage_data.get('prompt_token_count', 0)
                self.output_tokens += usage_data.get('candidates_token_count', 0)

    def calculate_cost(self):
        """Calculate total cost in dollars."""
        model_key = None
        for k in self.COSTS:
            if k in self.model.lower() or self.model.lower() in k:
                model_key = k
                break

        if not model_key:
            return 0.0

        input_cost, output_cost = self.COSTS[model_key]
        return (self.input_tokens * input_cost + self.output_tokens * output_cost) / 1_000_000

    def get_summary(self):
        """Return summary as dict for programmatic access."""
        return {
            'model': self.model,
            'requests': self.requests,
            'input_tokens': self.input_tokens,
            'output_tokens': self.output_tokens,
            'total_cost': self.calculate_cost(),
            'avg_input_per_request': self.input_tokens / self.requests if self.requests > 0 else 0,
            'avg_output_per_request': self.output_tokens / self.requests if self.requests > 0 else 0
        }

    def print_summary(self):
        """Print usage summary to console."""
        print(f"\n=== Cost Summary: {self.model} ===")
        print(f"Requests: {self.requests}")
        print(f"Input tokens: {self.input_tokens:,}")
        print(f"Output tokens: {self.output_tokens:,}")
        print(f"Total cost: ${self.calculate_cost():.4f}")

        if self.requests > 0:
            avg_input = self.input_tokens / self.requests
            avg_output = self.output_tokens / self.requests
            print(f"Avg per request: {avg_input:.0f} in, {avg_output:.0f} out")


# =============================================================================
# Helper Functions
# =============================================================================

def extract_json(text):
    """Extract JSON object from LLM response text.

    Finds the first { and last } in the text and parses as JSON.
    Returns empty dict if parsing fails.
    """
    try:
        start = text.find('{')
        end = text.rfind('}') + 1
        if start == -1 or end == 0:
            return {}
        return json.loads(text[start:end])
    except json.JSONDecodeError:
        return {}


def sample_distribution(probs):
    """Sample a key from a probability distribution dict.

    Handles string values (e.g., "0.3") by converting to float.
    Returns None if probs is empty or malformed.
    """
    try:
        weights = [float(v) for v in probs.values()]
        return random.choices(list(probs.keys()), weights=weights)[0]
    except (ValueError, TypeError, IndexError, AttributeError):
        return None


def call_with_retry(ctx, messages, max_retries=3):
    """Make LLM call and extract JSON, retrying silently on parse failures.

    Each retry is independent - failed responses are discarded, not accumulated.
    Only warns user if all retries fail.

    Returns:
        Tuple of (result_dict, raw_content) or ({}, None) if all retries fail.
    """
    for attempt in range(max_retries):
        content = ctx.call(messages)
        result = extract_json(content)
        if result:
            return result, content

    # All retries failed - warn user
    print(f"Warning: Failed to parse JSON after {max_retries} attempts")
    return {}, None


def llm_call(client, messages, callbacks=None):
    """Make LLM call and return response content.

    Args:
        client: Langchain chat client
        messages: List of message dicts with 'role' and 'content' keys
        callbacks: Optional list of callback handlers (e.g., CostTracker)

    Returns:
        Response content as string (stripped)
    """
    lc_messages = make_langchain_messages(messages)
    response = client.invoke(lc_messages, config={"callbacks": callbacks or []})
    return response.content.strip()


def llm_call_json(client, messages, callbacks=None):
    """Make LLM call and extract JSON from response.

    Args:
        client: Langchain chat client
        messages: List of message dicts with 'role' and 'content' keys
        callbacks: Optional list of callback handlers

    Returns:
        Parsed JSON dict (empty dict if parsing fails)
    """
    return extract_json(llm_call(client, messages, callbacks))


def setup_client(model, show_cost=False):
    """Set up LLM client with optional cost tracking.

    Args:
        model: Model name or alias
        show_cost: Whether to enable cost tracking

    Returns:
        Tuple of (client, callbacks) where callbacks includes CostTracker if show_cost=True
    """
    client = get_client(model)
    cost_tracker = CostTracker(model) if show_cost else None
    callbacks = [cost_tracker] if cost_tracker else []
    return client, callbacks, cost_tracker


class GenerationContext:
    """Bundle LLM client, callbacks, and settings for generation pipeline.

    Simplifies passing generation state through pipeline functions.

    Usage:
        ctx = GenerationContext(model='haiku', quiet=False, show_cost=True)
        ctx.log("Starting generation...")
        result = ctx.call(messages)
        result_json = ctx.call_json(messages)
        ctx.finish()  # prints cost summary if show_cost=True
    """

    def __init__(self, model="haiku", quiet=True, show_cost=False):
        self.model = model
        self.quiet = quiet
        self.show_cost = show_cost

        self.client = get_client(model)
        self.cost_tracker = CostTracker(model) if show_cost else None
        self.callbacks = [self.cost_tracker] if self.cost_tracker else []

    def log(self, message, end="\n", flush=False):
        """Print message if not in quiet mode."""
        if not self.quiet:
            print(message, end=end, flush=flush)

    def call(self, messages):
        """Make LLM call and return response content."""
        return llm_call(self.client, messages, self.callbacks)

    def call_json(self, messages):
        """Make LLM call and extract JSON from response."""
        return llm_call_json(self.client, messages, self.callbacks)

    def finish(self):
        """Print cost summary if show_cost is enabled."""
        if self.cost_tracker and self.show_cost:
            self.cost_tracker.print_summary()



"""
OpenRouter Provider
Uses OpenRouter API to access LLaMA, Mistral, Gemini, and more.
"""

import os
from openai import OpenAI

class LLMProvider:
    """LLM provider using OpenRouter"""

    def __init__(self, model="meta-llama/llama-3.1-8b-instruct"):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            raise ValueError("Missing OPENROUTER_API_KEY environment variable")

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=self.api_key
        )

        self.model = model
        self.provider = "OpenRouter"

    def generate(self, system_prompt, user_message, temperature=0.7, max_tokens=500):
        """Generate text using an OpenRouter model"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=temperature,
                max_tokens=max_tokens,
            )

            return response.choices[0].message.content

        except Exception as e:
            print("OpenRouter Error:", e)
            return "I'm having trouble generating a response right now."

    def get_model_info(self):
        return {
            "provider": "OpenRouter",
            "model": self.model
        }

    def test_connection(self):
        """Minimal valid test"""
        try:
            info = self.get_model_info()
            return True
        except:
            return False

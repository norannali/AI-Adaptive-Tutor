"""
Prompt Builder
Builds system and user prompts based on level
"""

class PromptBuilder:

    def build_system_prompt(self, level):
        if level == "beginner":
            return ("You are a helpful AI tutor. Explain in simple, beginner-friendly "
                    "way using easy examples and short sentences.")

        elif level == "intermediate":
            return ("You are an AI tutor. Explain with moderate depth, using structured "
                    "reasoning, technical terms if needed, and practical examples.")

        elif level == "advanced":
            return ("You are an expert AI educator. Give deep technical explanations, "
                    "mathematical intuition, and advanced insights.")

        return "You are a helpful AI tutor."

    def build_user_prompt(self, question):
        return f"Explain this question clearly:\n{question}"

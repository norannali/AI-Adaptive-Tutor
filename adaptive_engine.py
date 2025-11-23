# adaptive_engine.py
from memory_manager import MemoryManager
from response_style import ResponseStyleController
from struggle_detector import StruggleDetector
from vocabulary_controller import VocabularyController
from prompt_builder import PromptBuilder
from LLMProvider import LLMProvider

class AdaptiveEngine:
    def __init__(self):
        self.memory = MemoryManager()
        self.style = ResponseStyleController()
        self.struggle = StruggleDetector()
        self.vocab = VocabularyController()
        self.prompts = PromptBuilder()

        try:
            self.llm = LLMProvider(model="meta-llama/llama-3.1-8b-instruct")
        except:
            self.llm = None

    def _build_system_prompt(self, level, tone, struggling):
        base_prompt = self.prompts.build_system_prompt(level)
        struggle_note = "User seems to be struggling." if struggling else ""
        return f"""
You are an adaptive AI tutor.
Difficulty level: {level}
Tone: {tone}
{struggle_note}

{base_prompt}
        """

    def process(self, user_id, question, level=None):
        # Load state
        state = self.memory.get_user_state(user_id)
        user_level = level or state["level"]

        recent_questions = self.memory.get_recent_questions(user_id)
        struggle_info = self.struggle.analyze_question(question, recent_questions)
        struggling = struggle_info["severity"] == "high"
        repeated = struggle_info["is_repeated"]

        # Determine tone
        tone = self.style.determine_tone(
            emotion="confused" if struggling else "neutral",
            is_struggling=struggling,
            user_level=user_level
        )

        # Build prompts
        system_prompt = self._build_system_prompt(user_level, tone, struggling)
        user_prompt = self.prompts.build_user_prompt(question)

        # Generate AI response
        if self.llm:
            response = self.llm.generate(system_prompt, user_prompt)
        else:
            response = f"[{tone}] Simple explanation: {question}"

        final_response = self.style.format_response(response, tone, user_level, struggling)

        # Store in memory
        self.memory.store_interaction(
            user_id=user_id,
            question=question,
            answer=final_response,
            performance_score=50,
            complexity_score=5
        )

        return {
            "response": final_response,
            "metadata": {
                "user_level": user_level,
                "tone": tone,
                "is_struggling": struggling,
                "is_repeated_question": repeated,
                "struggle_score": struggle_info["struggle_points"],
                "llm_provider": self.llm.provider if self.llm else "fallback"
            }
        }

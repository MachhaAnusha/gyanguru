import os
import time
import google.generativeai as genai
from typing import Dict, Any


class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    def _call(self, prompt: str):
        for _ in range(3):
            try:
                response = self.model.generate_content(prompt)
                return response.text
            except Exception:
                time.sleep(2)
        raise Exception("Gemini API failed after retries")

    def generate_text_explanation(self, topic: str, depth: str) -> Dict[str,]()

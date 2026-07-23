import os
from google import genai

# API Key Environment Variable se aayegi (Safe practice)
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def generate_exam_response(user_prompt):
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_prompt
    )
    return response.text

if __name__ == "__main__":
    prompt = "Give me a quick 3-step daily routine for an exam aspirant."
    print(generate_exam_response(prompt))

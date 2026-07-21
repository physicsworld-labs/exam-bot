print("Eximport os
from google import genai

# Gemini API Client Initialization
# Note: GEMINI_API_KEY env variable se key read karega
client = genai.Client()

SYSTEM_PROMPT = """
You are an expert AI exam assistant for UPSC, NDA, and CHSL aspirants. 
Provide concise, accurate, and highly structured explanations for questions.
Always keep answers syllabus-aligned and easy to revise.
"""

def generate_exam_response(user_query):
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_query,
            config={'system_instruction': SYSTEM_PROMPT}
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    test_question = "What are the core subjects for UPSC Prelims?"
    print(f"Question: {test_question}\n")
    print("AI Response:")
    print(generate_exam_response(test_question))am Bot Server Initialized Successfully!")

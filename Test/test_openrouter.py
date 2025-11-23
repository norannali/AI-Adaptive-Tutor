import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

def test_api():
    try:
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Say hello in one sentence."}
            ]
        )

        print("API Test Success!")
        print("Response:", response.choices[0].message.content)

    except Exception as e:
        print("API Test Failed!")
        print("Error:", str(e))

if __name__ == "__main__":
    test_api()

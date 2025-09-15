import google.generativeai as genai

# Configure Gemini API key directly
genai.configure(api_key="AIzaSyB2HoIfYQeIcZkZi33TkPd3JQ3o81abhmM")  # Replace with your key

# Initialize Gemini model
model = genai.GenerativeModel("models/gemini-2.5-flash")

prompts = [
    "what is the capital of France",
    "Can you tell me the capital of India?",
    "capital of Japan?",
    "what is the capital of Brazil?",
    "what is the capital of USA"
]

for prompt in prompts:
    response = model.generate_content(prompt)
    # Access the generated text properly
    print(f"Q: {prompt}\nA: {response.text}\n")

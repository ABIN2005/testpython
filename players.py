import google.generativeai as genai
import json

# Configure Gemini API key
genai.configure(api_key="AIzaSyB2HoIfYQeIcZkZi33TkPd3JQ3o81abhmM")  # replace with your API key

# Initialize Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Prompt asking for JSON format output
prompt = (
    "Give me a JSON object where keys are decades or years (e.g., '1930s', '1940s', '1950s', etc.) "
    "and values are lists of Indian cricketers who represented India in that period. "
    "Start from the first Test match in 1932 till now."
)

# Generate response
response = model.generate_content(prompt)

# Try to parse as JSON (if possible)
try:
    players_data = json.loads(response.text)
    print("✅ Parsed JSON Data:\n")
    print(json.dumps(players_data, indent=2))
except json.JSONDecodeError:
    print("⚠️ Could not parse as JSON. Raw output:\n")
    print(response.text)

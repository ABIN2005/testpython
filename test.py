import google.generativeai as genai

# Configure Gemini directly with API key
genai.configure(api_key="AIzaSyB2HoIfYQeIcZkZi33TkPd3JQ3o81abhmM")

# Use a stronger model
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Ask a question
prompt = "Explain the significance of the Battle of Plassey in Indian history in 5 simple sentences."
response = model.generate_content(prompt)

# Print the answer
print("🤖 Gemini says:\n")
print(response.text)

import google.generativeai as genai

genai.configure(api_key="AIzaSyB2HoIfYQeIcZkZi33TkPd3JQ3o81abhmM")

# Use correct model
model = genai.GenerativeModel("models/gemini-2.5-flash")

prompt = "Explain blockchain in simple words."
response = model.generate_content(prompt)

print(response.text)

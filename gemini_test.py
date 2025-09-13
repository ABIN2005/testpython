import google.generativeai as genai

genai.configure(api_key="AIzaSyCf7zr_7oEBMr1NopLK0KdivSsvsxR7HG8")

# Use correct model
model = genai.GenerativeModel("models/gemini-1.5-flash")

prompt = "Explain blockchain in simple words."
response = model.generate_content(prompt)

print(response.text)

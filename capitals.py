import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyB2HoIfYQeIcZkZi33TkPd3JQ3o81abhmM")  # Replace with your key

# Initialize Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Prompt to get all Indian states and their capitals
prompt = "List all the states of India along with their capitals in a clear format."

response = model.generate_content(prompt)

# Print the generated response
print("Capitals of Indian States:\n")
print(response.text)

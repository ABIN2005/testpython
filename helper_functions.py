def print_llm_response(question):
    # A small dictionary of countries and their capitals
    capitals = {
        "france": "Paris",
        "germany": "Berlin",
        "italy": "Rome",
        "spain": "Madrid",
        "india": "New Delhi",
        "usa": "Washington, D.C.",
        "japan": "Tokyo"
    }

    # Convert question to lowercase for easy matching
    q_lower = question.lower()

    # Check if the question is about the capital
    for country, capital in capitals.items():
        if country in q_lower:
            print(f"The capital of {country.capitalize()} is {capital}")
            return
    
    print("I don't know the answer to that yet.")

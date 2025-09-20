def print_llm_response(question):
    """
    Prints the response to a question about capitals.
    """
    capitals = {
        "france": "Paris",
        "germany": "Berlin",
        "italy": "Rome",
        "spain": "Madrid",
        "india": "New Delhi",
        "usa": "Washington, D.C.",
        "japan": "Tokyo"
    }

    q_lower = question.lower()

    for country, capital in capitals.items():
        if country in q_lower:
            print(f"The capital of {country.capitalize()} is {capital}")
            return
    
    print("I don't know the answer to that yet.")


def get_llm_response(question):
    """
    Returns the response to a question about capitals (as a string).
    """
    capitals = {
        "france": "Paris",
        "germany": "Berlin",
        "italy": "Rome",
        "spain": "Madrid",
        "india": "New Delhi",
        "usa": "Washington, D.C.",
        "japan": "Tokyo"
    }

    q_lower = question.lower()

    for country, capital in capitals.items():
        if country in q_lower:
            return f"The capital of {country.capitalize()} is {capital}"
    
    return "I don't know the answer to that yet."

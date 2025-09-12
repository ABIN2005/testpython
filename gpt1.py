def get_llm_response(prompt):
    # For now, just return a fake answer
    return f"Couplet: My friend {name} with potatoes five, makes every feast come alive!"

name = "Tommy"
potatoes = 4.75
prompt = f"""Write a couplet about my friend {name} who has about {round(potatoes)} potatoes"""
response = get_llm_response(prompt)
print(response)
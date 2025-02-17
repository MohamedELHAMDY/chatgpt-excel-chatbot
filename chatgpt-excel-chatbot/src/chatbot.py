import openai
import pandas as pd

# Your OpenAI API key
openai.api_key = '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'

# Load Excel data
df = pd.read_excel('your_file.xlsx')

# Function to search the Excel file based on user input
def search_excel(query):
    result = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    if not result.empty:
        return result.to_string(index=False)
    else:
        return "No matching data found."

# Simple chat loop
def chat():
    while True:
        user_input = input("Ask me something: ")
        if user_input.lower() == 'exit':
            break
        
        # Search the Excel data
        excel_result = search_excel(user_input)
        
        # Call GPT for a response
        gpt_response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=user_input, 
            max_tokens=50
        ).choices[0].text.strip()
        
        print("GPT Response: ", gpt_response)
        print("Excel Data:\n", excel_result)

# Start chat
chat()

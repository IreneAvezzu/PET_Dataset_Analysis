import pandas as pd
from support_methods import *
from groq import Groq
import os


# 1 Load the phrases from the dataset
phrases = load_phrases('Data/Data.parquet')


# 2 Initialize necessary variables
# 2.1 Arrays where the results and interactions count will be stored
results = []
interactions = []

# 2.2 Load instruction and process information from files
instruction = read_file("Prompts/1_constraints_templates.md")
meta_constraints = read_file("Prompts/2_additional_constraints_templates.md")
hirearch_instruction = read_file("Prompts/3_meta_constraints.txt")
process_description = read_file("Prompts/4_dataset_phrase_mock.txt")

# 2.3 Define the information necessary for the API model
API_KEY = "" # Set your Groq API key here
os.environ["GROQ_API_KEY"] = API_KEY #set environment variable
model_maverik = "meta-llama/llama-4-maverick-17b-128e-instruct"
model_3_1 = "llama-3.1-8b-instant"
model_scout = "meta-llama/llama-4-scout-17b-16e-instruct"
MODEL = model_scout

# 2.4 Initialize client for Groq API
client = Groq()


# 3 Analyse each phrase
for phrase in phrases:
    # for each phrase the interaction_counter is reset
    interaction_counter = 0 

    # Introduce chat
    print(f"\n\n\n\n\n\n 💻 This is a new chat with Ollama model {MODEL} \n   Once you are satisfied with the results, please type 'save' to save constraints and procede to the next phrase.\n   If you would like to close the chat please type 'exit' \n   It is currently analysing the dataset phrase: \n   {phrase}. ")


    # load phrase prompt and format it with current phrase
    formatted_prompt = process_description.format(textual_description=phrase)

    # 3.1 Start chat
    conversation = []
    conversation.append(
        {'role': 'system',
        'content': instruction})
    conversation.append(
        {'role': 'system',
        'content': meta_constraints})
    conversation.append(
        {'role': 'system',
        'content': hirearch_instruction})
    conversation.append(
        {'role': 'system',
        'content': formatted_prompt})


    # 3.2 While loop to handle interactions
    while True:
        # get the AI's reply
        response = client.chat.completions.create(
            model=MODEL,
            messages=conversation
        )

        # Extract and display model's reply
        response_dict = dict(response)
        choices = response_dict.get("choices", [])

        reply = "The model did not return a valid response."
        if choices:
            reply = choices[0].message.content
        
        # print result
        print(f"\n\n💻 AI: {reply}")

        # Add model's response to the conversation
        conversation.append({'role': 'assistant', 'content': reply})

        user_input = input("\n\n🧠 You: ")
        interaction_counter = interaction_counter + 1

        if user_input.lower() in ['exit',]:
            exit()

        if user_input.lower() in ['save']:
            # 3.3 Save results and interaction counter
            results.append(reply)
            interactions.append(interaction_counter-1)
            break

        # Add user's message to the conversation
        conversation.append({'role': 'user', 'content': user_input})


# 4 Parse the results
constraints = []
const_nums = []
activities = []
activities_nums = []

for result in results:
    # Parse the AI's reply to find the constraints
    matches = parse_response_constraints(result)
    constraints.append(matches)
    num_constraints = len(matches)
    const_nums.append(num_constraints)

    # Extract the activities
    activities_list = extract_activities(result)
    activities.append(activities_list)
    num_activities = len(activities_list)
    activities_nums.append(num_activities)



# Print to check the results 
#print(f"OG results: \n{results}")
#print(f"Parsed results: \n{parsed_results}")    
#print(f"\n\nNumber of constraints per phrase: \n{const_nums}")
#print(f"\n\nNumber of interactions per phrase: \n{interactions}")

# 5 Save the results as a pandas' dataframe exported as a CSV file 
df = pd.DataFrame({
    'dataset_phrase': phrases,
    'extracted_constraints': constraints,
    'interactions': interactions,
    'constraints_count': const_nums,
    'activities': activities,
    'activity_count': activities_nums
})

#df.to_csv('Results\1_basic_templates.csv', index=False)
#df.to_csv('Results\2_additional_templates.csv', index=False)
df.to_csv('Results\3_hierarchy_rules.csv', index=False)
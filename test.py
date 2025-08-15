import dill
import spacy
from dotenv import load_dotenv
import google.generativeai as genai
import os
load_dotenv()

nlp = spacy.load("en_core_web_sm") 

# Load the functions dictionary from the pickle file
with open('model.pkl', 'rb') as f:
    loaded_functions = dill.load(f)

# Extract individual functions
model_train = loaded_functions['model_train']
extract_key_points = loaded_functions['extract_key_points']
is_coding_related_bow = loaded_functions['is_coding_related_bow']
is_general_question = loaded_functions['is_general_question']

sentence = "What essay on C language evaluation?"

model_train(sentence)
print(model_train)
api_key=""
if(model_train=='Claude'):
    api_key=os.getenv('CLAUDE_KEY')
elif(model_train=='Gemini'):
    api_key=os.getenv('GEMINI_KEY')
else:
    api_key=os.getenv('PERPLEXITY_KEY')

genai.configure(api_key=api_key)

system_prompt = "You are a fun cat named Milo. Give mischievous answers in 3 lines max."


model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(sentence)
print(response.text)



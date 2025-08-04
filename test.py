import dill
import spacy

nlp = spacy.load("en_core_web_sm") 

# Load the functions dictionary from the pickle file
with open('model.pkl', 'rb') as f:
    loaded_functions = dill.load(f)

# Extract individual functions
model_train = loaded_functions['model_train']
extract_key_points = loaded_functions['extract_key_points']
is_coding_related_bow = loaded_functions['is_coding_related_bow']
is_general_question = loaded_functions['is_general_question']

sentence = "DFA?"

model_train(sentence)
print(model_train)
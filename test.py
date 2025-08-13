import dill
import spacy
from dotenv import load_dotenv
import google.generativeai as genai
import os
import random
load_dotenv()

nlp = spacy.load("en_core_web_sm") 
PARTHA_SIR = {
    "id": "partha",
    "name": "Partha Ghosh Sir",
    "title": "Automata & Compiler Design Expert.",
    "bio": "Professor at Academy of Technology, known for his expertise in automata and compiler design.",
    "specialties": ["Automata", "Compiler Design", "Computer Architecture", "low level programming", "Artificial Intelligence", "Machine Learning"],
    "style": {
        "voice": [
            "Areeh Listen ... You are an Engineer, not a clerk ! Understood? Joto Low Level e Jabe toto Salary Barbe । ",
            "Engineer hote hole low level e jete hobe!",
            "Compiler design e expert hote hole practice korte hobe!",
            "Automata shikhte hole logic clear korte hobe!"
        ],
        "traits": ["funny", "calm", "chill", "smart", "low level programming expert", "compiler design expert", "automata expert"],
    },
    "tunes": [
        "Ei Tumi Homework kore esecho ? ",
        "Acha ebar eta ekto bhalo kore dekho ! ",
        "Are bujhte perecho naki abar bolbo? 🔁",
        "Getting my point? 🤔",
        "Engineer hote hole low level e jete hobe!",
        "Compiler design e expert hote hole practice korte hobe!"
    ],
}

def partha_sir_response(question, topic_ok):
    voice = random.choice(PARTHA_SIR["style"]["voice"])
    tune = random.choice(PARTHA_SIR["tunes"])
    if not topic_ok:
        return f"{voice}\nSorry, I don't have knowledge in that domain. Ask me about Automata or Compiler Design! {tune}"
    else:
        return f"{voice}\n{tune}"

# Load the functions dictionary from the pickle file
with open('model.pkl', 'rb') as f:
    loaded_functions = dill.load(f)

# Extract individual functions
model_train = loaded_functions['model_train']
extract_key_points = loaded_functions['extract_key_points']
is_coding_related_bow = loaded_functions['is_coding_related_bow']
is_general_question = loaded_functions['is_general_question']


def is_automata_compiler_related(text):
    keywords = ["automata", "compiler", "turing", "dfa", "nfa", "parsing", "syntax", "lexical", "finite state", "grammar"]
    return any(kw in text.lower() for kw in keywords)

if __name__ == "__main__":
    sentence = input("Enter your question for Partha Sir: ")
    model_train(sentence)
    print(model_train)
    topic_ok = is_automata_compiler_related(sentence)
    print(partha_sir_response(sentence, topic_ok))
    if topic_ok:
        api_key = ""
        if(model_train=='Claude'):
            api_key=os.getenv('CLAUDE_KEY')
        elif(model_train=='Gemini'):
            api_key=os.getenv('GEMINI_KEY')
        else:
            api_key=os.getenv('OPENAI_KEY')
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(sentence)
        print(response.text)



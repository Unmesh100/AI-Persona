import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
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


# This response is given my Gemini
def ResponseByGemini(isRelated,myKey,Question):
       api_key=os.getenv(myKey)
       genai.configure(api_key=api_key)
       model = genai.GenerativeModel('gemini-1.5-flash')
       bio="\n".join(PARTHA_SIR['bio'])
       tunes_string = "\n".join(PARTHA_SIR["tunes"])
       traits = "\n".join( PARTHA_SIR["style"]["traits"])
       voice="\n".join(PARTHA_SIR["style"]['voice'])
       myQuestion="The person does not know the answer to a particular question generate a suitable response based on the {voice} that the person might give .Give only one option" if isRelated==False else f"Please tell me how the person will reply to this question :{Question} Generate this response similar to this {voice} the answer should be detailed"
       sentence=f"This is the person's bio:{bio} The person is has the following Tunes :{tunes_string} The person has the following traits :{traits} The person has the following voices: {voice}  {myQuestion}"
       response = model.generate_content(sentence)
       return response.text

# Respone given by Claude
def ResponseByClaude(isRelated,myKey,Question):
       api_key=os.getenv(myKey)
       genai.configure(api_key=api_key)
       model = genai.GenerativeModel('gemini-1.5-flash')
       bio="\n".join(PARTHA_SIR['bio'])
       tunes_string = "\n".join(PARTHA_SIR["tunes"])
       traits = "\n".join( PARTHA_SIR["style"]["traits"])
       voice="\n".join(PARTHA_SIR["style"]['voice'])
       myQuestion="The person does not know the answer to a particular question generate a suitable response based on the {voice} that the person might give .Give only one option" if isRelated==False else f"Please tell me how the person will reply to this question :{Question} Generate this response similar to this {voice} the answer should be detailed"
       sentence=f"This is the person's bio:{bio} The person is has the following Tunes :{tunes_string} The person has the following traits :{traits} The person has the following voices: {voice}  {myQuestion}"
       response = model.generate_content(sentence)
       return response.text

# Respone given by GPT
def ResponseByGPT(isRelated,myKey,Question):
       api_key=os.getenv(myKey)
       genai.configure(api_key=api_key)
       model = genai.GenerativeModel('gemini-1.5-flash')
       bio="\n".join(PARTHA_SIR['bio'])
       tunes_string = "\n".join(PARTHA_SIR["tunes"])
       traits = "\n".join( PARTHA_SIR["style"]["traits"])
       voice="\n".join(PARTHA_SIR["style"]['voice'])
       myQuestion="The person does not know the answer to a particular question generate a suitable response based on the {voice} that the person might give .Give only one option" if isRelated==False else f"Please tell me how the person will reply to this question :{Question} Generate this response similar to this{voice} the answer should be detailed"
       sentence=f"This is the person's bio:{bio} The person is has the following Tunes :{tunes_string} The person has the following traits :{traits} The person has the following voices: {voice}  {myQuestion}"
       response = model.generate_content(sentence)
       return response.text




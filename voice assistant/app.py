import speech_recognition as sr
import pyttsx3
from transformers import pipeline
from datetime import datetime
import webbrowser as wb
import os

recognizer = sr.Recognizer()

engine = pyttsx3.init()

nlp = pipeline("question-answering", model='distilbert-base-uncased-distilled-squad')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-IN')
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, there seems to be an issue with the speech service.")
            return ""

def tell_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return f"The current time is {current_time}"

def greeting():
    speak("hi what\'s your name?")
    name = listen()
    if not name:
        speak("Maybe your the creator of this program")
        name = "Divij"
    if int(datetime.now().strftime('%H'))< 12:
        speak(f"Good morning {name}")
    elif 12<=int(datetime.now().strftime('%H'))<18:
        speak(f"Good afternoon {name}")
    else:
        speak(f"Good evening {name}")

def create_file(name):
    with open(name + '.txt', "w") as file:
        speak('What should I write in the file!')
        info = listen()
        if info:
            file.write(info)
            speak("file Was saved")
        else:
            speak('Sorry no content could be saved')
    return info

def read_file(name):
    with open(name + '.txt', "r") as file:
        data = file.read()
    return data

def answer_question(query):
    context = """
    The Amazon rainforest (Portuguese: Floresta Amazônica or Amazônia; Spanish: Selva Amazónica, Amazonía or usually Amazonia; French: Forêt amazonienne; Dutch: Amazoneregenwoud), also known in English as Amazonia or the Amazon Jungle, is a moist broadleaf forest that covers most of the Amazon basin of South America. This basin encompasses 7,000,000 square kilometres (2,700,000 sq mi), of which 5,500,000 square kilometres (2,100,000 sq mi) are covered by the rainforest. This region includes territory belonging to nine nations. The majority of the forest is contained within Brazil, with 60% of the rainforest, followed by Peru with 13%, Colombia with 10%, and with minor amounts in Venezuela, Ecuador, Bolivia, Guyana, Suriname and French Guiana. States or departments in four nations contain "Amazonas" in their names. The Amazon represents over half of the planet's remaining rainforests, and comprises the largest and most biodiverse tract of tropical rainforest in the world, with an estimated 390 billion individual trees divided into 16,000 species.
    The Solar System is the gravitationally bound system of the Sun and the objects that orbit it, either directly or indirectly. Of the objects that orbit the Sun directly, the largest are the eight planets, with the remainder being smaller objects, the dwarf planets and small Solar System bodies.
    Earth is the third planet from the Sun and the only astronomical object known to harbor life. This is enabled by Earth being an ocean world, the only one in the Solar System sustaining liquid surface water. Almost all of Earth's water is contained in its global ocean, covering 70.8% of Earth's crust. The remaining 29.2% of Earth's crust is land, most of which is located in the form of continental landmasses within Earth's land hemisphere. Most of Earth's land is somewhat humid and covered by vegetation, while large sheets of ice at Earth's polar deserts retain more water than Earth's groundwater, lakes, rivers and atmospheric water combined. Earth's crust consists of slowly moving tectonic plates, which interact to produce mountain ranges, volcanoes, and earthquakes. Earth has a liquid outer core that generates a magnetosphere capable of deflecting most of the destructive solar winds and cosmic radiation.
    India, officially the Republic of India (ISO: Bhārat Gaṇarājya),[21] is a country in South Asia. It is the seventh-largest country by area; the most populous country as of June 2023;[22][23] and from the time of its independence in 1947, the world's most populous democracy.[24][25][26] It is physiographically bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, the Bay of Bengal on the southeast, and High-mountain Asia on the northeast. It shares land borders with Pakistan to the northwest;[j] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia.
    """
    result = nlp(question=query, context=context)
    return result['answer']

def handle_query(query):
    if not query:
        return 'Please repeat the question I did not get it?'
    if 'hello' in query or 'hi' in query or 'namaste' in query:
        return greeting()
    elif 'time' in query:
        return tell_time()
    elif 'search' in query:
        return wb.open(query)
    elif query.startswith('read'):
        return read_file(query.split(' ')[1])
    elif query.startswith('create'):
        return create_file(query.split(' ')[1])
    else:
        return answer_question(query)

if __name__ == "__main__":
    while True:
        query = listen().lower()
        if 'exit' in query or 'stop' in query or 'thank you' in query:
            speak("Have a great day, Goodbye!")
            break
        response = handle_query(query)
        speak(response)

""" 

Links:
PrivateGPT - https://github.com/imartinez/privateGPT
GPT4All - https://github.com/nomic-ai/gpt4all


#pip install gpt4all  # OK
import gpt4all
#model = gpt4all.GPT4All("ggml-gpt4all-j-v1.3-groovy")
#model = gpt4all.GPT4All("ggml-gpt4all-j.bin")
#model = gpt4all.GPT4All("ggml-nous-gpt4-vicuna-13b.bin")
#error ///// model = gpt4all.GPT4All("ggml-gpt4all-l13b-snoozy.bin")
model = gpt4all.GPT4All("ggml-model-gpt4all-falcon-q4_0.bin")
#model = gpt4all.GPT4All("ggml-mpt-7b-chat.bin")

#pip install translate  # OK
"""

import gpt4all
from translate import Translator
import tkinter as tk

model = gpt4all.GPT4All("ggml-model-gpt4all-falcon-q4_0.bin")

#sentence = textbox.get("1.0", tk.END).strip()   
 
while True:
    question = input('Diga Algo: ')
    
    with model.chat_session():
        # Generate a response to a prompt
        response = model.generate(prompt=question, temp=0.5 )
        
        # Translate the response from English to Spanish
        target_language_code = "es"
        translator = Translator(to_lang=target_language_code)
        translated_response = translator.translate(response)
        
        print("Chatbot:", translated_response)

"""    

import tkinter as tk
from translate import Translator
import gpt4all

window = tk.Tk()
window.title("Translate App")
question_textbox = tk.Entry(window)
question_textbox.pack()

model = gpt4all.GPT4All("ggml-model-gpt4all-falcon-q4_0.bin")

def get_question():
    question = question_textbox.get()

    with model.chat_session():
            # Generate a response to a prompt
            response = model.generate(prompt=question, temp=0.5, )
            
            print("Question:", question)    

button = tk.Button(window, text="Send", command=get_question)
button.pack()

window.mainloop()

"""
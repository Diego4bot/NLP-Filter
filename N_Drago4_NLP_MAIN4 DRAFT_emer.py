import pygame
import os
import re
import random
import pyaudio
import vosk
import wave
import unicodedata
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import scrolledtext
from N_Drago4_NLP_voicer_utils import (va,vb,vc,vd,ve,vf,vg,vh,
                                   vi,vj,vk,vl,vm,vn,vo,vp,
                                   vq,vz,vbuda,vgreetings)

from N_Drago4_NLP_frame3_word_map import (load_text_into_textbox, close_frame) 
from N_Drago4_NLP_PATH import (general_path_AUDIO_ESP, image_address, voice_recog_model)




# Set up the audio stream # ***************************************************************************
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000)





# Paths, words to recognize & sounds EX:// #***********************************************************

#x_general_path =  'C:/Users/user/Documents/N_Drago/'
#x_recognize = "hola|honda|hornelo"
#x_sounds = ['1','2','3']

#Greetings Filter Path
greetings_general_path = f'{general_path_AUDIO_ESP}/Greetings/'
greetings_recognize = vgreetings 
greetings_sounds = []
# Get the list of files in the directory
file_list = os.listdir(greetings_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(greetings_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
greetings_sounds = file_list
# Print the resulting lists
print("File Names:", greetings_sounds)

#Buda Filter Path 
buda_general_path =  f'{general_path_AUDIO_ESP}/Buda/'
buda_recognize = vbuda 
buda_sounds = []
# Get the list of files in the directory
file_list = os.listdir(buda_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(buda_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
buda_sounds = file_list
# Print the resulting lists
print("File Names:", buda_sounds)

#Standard Filter Path ***********
a_general_path =  f'{general_path_AUDIO_ESP}/a/'
a_recognize = va 
a_sounds = []
# Get the list of files in the directory
file_list = os.listdir(a_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(a_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
a_sounds = file_list
# Print the resulting lists
print("File Names:", a_sounds)

b_general_path =  f'{general_path_AUDIO_ESP}/b/'
b_recognize = vb
b_sounds = []
# Get the list of files in the directory
file_list = os.listdir(b_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(b_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
b_sounds = file_list
# Print the resulting lists
print("File Names:", b_sounds)

c_general_path =  f'{general_path_AUDIO_ESP}/c/'
c_recognize = vc
c_sounds = []
# Get the list of files in the directory
file_list = os.listdir(c_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(c_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
c_sounds = file_list
# Print the resulting lists
print("File Names:", c_sounds)

d_general_path =  f'{general_path_AUDIO_ESP}/d/'
d_recognize = vd
d_sounds = []
# Get the list of files in the directory
file_list = os.listdir(d_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(d_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
d_sounds = file_list
# Print the resulting lists
print("File Names:", d_sounds)

e_general_path =  f'{general_path_AUDIO_ESP}/e/'
e_recognize = ve
e_sounds = []
# Get the list of files in the directory
file_list = os.listdir(e_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(e_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
e_sounds = file_list
# Print the resulting lists
print("File Names:", e_sounds)

f_general_path =  f'{general_path_AUDIO_ESP}/f/'
f_recognize = vf
f_sounds = []
# Get the list of files in the directory
file_list = os.listdir(f_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(f_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
f_sounds = file_list
# Print the resulting lists
print("File Names:", f_sounds)

g_general_path =  f'{general_path_AUDIO_ESP}/g/'
g_recognize = vg
g_sounds = []
# Get the list of files in the directory
file_list = os.listdir(g_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(g_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
g_sounds = file_list
# Print the resulting lists
print("File Names:", g_sounds)

h_general_path =  f'{general_path_AUDIO_ESP}/h/'
h_recognize = vh
h_sounds = []
# Get the list of files in the directory
file_list = os.listdir(h_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(h_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
h_sounds = file_list
# Print the resulting lists
print("File Names:", h_sounds)

i_general_path =  f'{general_path_AUDIO_ESP}/i/'
i_recognize = vi
i_sounds = []
# Get the list of files in the directory
file_list = os.listdir(i_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(i_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
i_sounds = file_list
# Print the resulting lists
print("File Names:", i_sounds)

j_general_path =  f'{general_path_AUDIO_ESP}/j/'
j_recognize = vj
j_sounds = []
# Get the list of files in the directory
file_list = os.listdir(j_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(j_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
j_sounds = file_list
# Print the resulting lists
print("File Names:", j_sounds)

k_general_path =  f'{general_path_AUDIO_ESP}/k/'
k_recognize = vk
k_sounds = []
# Get the list of files in the directory
file_list = os.listdir(k_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(k_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
k_sounds = file_list
# Print the resulting lists
print("File Names:", k_sounds)

l_general_path =  f'{general_path_AUDIO_ESP}/l/'
l_recognize = vl
l_sounds = []
# Get the list of files in the directory
file_list = os.listdir(l_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(l_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
l_sounds = file_list
# Print the resulting lists
print("File Names:", l_sounds)

m_general_path =  f'{general_path_AUDIO_ESP}/m/'
m_recognize = vm
m_sounds = []
# Get the list of files in the directory
file_list = os.listdir(m_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(m_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
m_sounds = file_list
# Print the resulting lists
print("File Names:", m_sounds)

n_general_path =  f'{general_path_AUDIO_ESP}/n/'
n_recognize = vn
n_sounds = []
# Get the list of files in the directory
file_list = os.listdir(n_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(n_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
n_sounds = file_list
# Print the resulting lists
print("File Names:", n_sounds)

o_general_path =  f'{general_path_AUDIO_ESP}/o/'
o_recognize = vo
o_sounds = []
# Get the list of files in the directory
file_list = os.listdir(o_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(o_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
o_sounds = file_list
# Print the resulting lists
print("File Names:", o_sounds)

p_general_path =  f'{general_path_AUDIO_ESP}/p/'
p_recognize = vp
p_sounds = []
# Get the list of files in the directory
file_list = os.listdir(p_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(p_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
p_sounds = file_list
# Print the resulting lists
print("File Names:", p_sounds)

q_general_path =  f'{general_path_AUDIO_ESP}/q/'
q_recognize = vq
q_sounds = []
# Get the list of files in the directory
file_list = os.listdir(q_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(q_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
q_sounds = file_list
# Print the resulting lists
print("File Names:", q_sounds)

# No match Path
z_general_path = f'{general_path_AUDIO_ESP}/z/'
z_recognize = vz
z_sounds = []
# Get the list of files in the directory
file_list = os.listdir(z_general_path)
# Filter out non-file items (directories, subdirectories, etc.)
file_list = [file for file in file_list if os.path.isfile(os.path.join(z_general_path, file))]
# Count the number of files
num_files = len(file_list)
# Generate the corresponding numbers and names
z_sounds = file_list
# Print the resulting lists
print("File Names:", z_sounds)





# Multiple inits # #***********************************************************************************
# Pygame initialization 

pygame.mixer.init()
pygame.mixer.music.set_volume(1)
st = ".mp3" 





# TIME ************************************************************************************************
#* 
time1 = 4000 # button_ask_the _robot - delay time to activate, deactivate
#*
time2 = 6000 # Time to delete any info in the Textbox if there is no activity
#*
time3 = 2000  # Call "check_activity" function again after a interval
time4 = 7000 # Time to activate the "enter key" virtually after last voice was listened
sensitivity=5





#___________________________________________________________________

# Functions to enable / disable button
def enable_button():
    button_ask_the_bot.config(state=tk.NORMAL)





# MAIN EVENT // Function to Search for words in Sentences # *******************************************

def get_user_input():
    sentence = textbox.get("1.0", tk.END).strip()
    # Remove special characters using regular expressions
    sentence = re.sub(r"[^\w\s]", "", sentence)
    # Remove diacritics (tildes) using Unicode normalization
    sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    print(sentence)

    #Greetings filtering 
    if re.search(greetings_recognize, sentence):
        greetings_random_sound = random.choice(greetings_sounds)
        greetings_file_path = f'{greetings_general_path}{greetings_random_sound}'
        pygame.mixer.music.load(greetings_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print("Greetings!!!!!")
        print(greetings_recognize)
        print(greetings_file_path) 
    
    #Buda filtering 
    #Buddha replied calmly: 
    # "If I give you a horse but you don't accept it,
    #  whose horse is it?" The student, after hesitating for a moment, 
    # replied: "If I didn't accept it, it would still be yours."
    # so, this robot wont accept injuries through this filter.
    elif re.search(buda_recognize, sentence):
        buda_random_sound = random.choice(buda_sounds)
        buda_file_path = f'{buda_general_path}{buda_random_sound}'
        pygame.mixer.music.load(buda_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print("Buda word!!!!!")
        print(buda_recognize)
        print(buda_file_path)
        
    #words to recognize / Standard Filtering
    elif re.search(a_recognize, sentence):
        a_random_sound = random.choice(a_sounds)
        a_file_path = f'{a_general_path}{a_random_sound}'
        pygame.mixer.music.load(a_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(a_file_path)
        print(a_recognize)
                
    elif re.search(b_recognize, sentence):
        b_random_sound = random.choice(b_sounds)
        b_file_path = f'{b_general_path}{b_random_sound}'
        pygame.mixer.music.load(b_file_path )
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(b_file_path)
        print(b_recognize)
           
    elif re.search(c_recognize, sentence):
        c_random_sound = random.choice(c_sounds)
        c_file_path = f'{c_general_path}{c_random_sound}'
        pygame.mixer.music.load(c_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(c_file_path)
        print(c_recognize)

    elif re.search(d_recognize, sentence):
        d_random_sound = random.choice(d_sounds)
        d_file_path = f'{d_general_path}{d_random_sound}'
        pygame.mixer.music.load(d_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(d_file_path)
        print(d_recognize) 

    elif re.search(e_recognize, sentence):
        e_random_sound = random.choice(e_sounds)
        e_file_path = f'{e_general_path}{e_random_sound}'
        pygame.mixer.music.load(e_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(e_file_path)
        print(e_recognize) 

    elif re.search(f_recognize, sentence):
        f_random_sound = random.choice(f_sounds)
        f_file_path = f'{f_general_path}{f_random_sound}'
        pygame.mixer.music.load(f_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(f_file_path)
        print(f_recognize)    

    elif re.search(g_recognize, sentence):
        g_random_sound = random.choice(g_sounds)
        g_file_path = f'{g_general_path}{g_random_sound}'
        pygame.mixer.music.load(g_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(g_file_path)
        print(g_recognize)    

    elif re.search(h_recognize, sentence):
        h_random_sound = random.choice(h_sounds)
        h_file_path = f'{h_general_path}{h_random_sound}'
        pygame.mixer.music.load(h_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(h_file_path)
        print(h_recognize)  

    elif re.search(i_recognize, sentence):
        i_random_sound = random.choice(i_sounds)
        i_file_path = f'{i_general_path}{i_random_sound}'
        pygame.mixer.music.load(i_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(i_file_path)
        print(i_recognize)

    elif re.search(j_recognize, sentence):
        j_random_sound = random.choice(j_sounds)
        j_file_path = f'{j_general_path}{j_random_sound}'
        pygame.mixer.music.load(j_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(j_file_path)
        print(j_recognize) 

    elif re.search(k_recognize, sentence):
        k_random_sound = random.choice(k_sounds)
        k_file_path = f'{k_general_path}{k_random_sound}'
        pygame.mixer.music.load(k_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(k_file_path)
        print(k_recognize) 

    elif re.search(l_recognize, sentence):
        l_random_sound = random.choice(l_sounds)
        l_file_path = f'{l_general_path}{l_random_sound}'
        pygame.mixer.music.load(l_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(l_file_path)
        print(l_recognize)  

    elif re.search(m_recognize, sentence):
        m_random_sound = random.choice(m_sounds)
        m_file_path = f'{m_general_path}{m_random_sound}'
        pygame.mixer.music.load(m_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(m_file_path)
        print(m_recognize)   

    elif re.search(n_recognize, sentence):
        n_random_sound = random.choice(n_sounds)
        n_file_path = f'{n_general_path}{n_random_sound}'
        pygame.mixer.music.load(n_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(n_file_path)
        print(n_recognize)  

    elif re.search(o_recognize, sentence):
        o_random_sound = random.choice(o_sounds)
        o_file_path = f'{o_general_path}{o_random_sound}'
        pygame.mixer.music.load(o_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(o_file_path)
        print(o_recognize)

    elif re.search(p_recognize, sentence):
        p_random_sound = random.choice(p_sounds)
        p_file_path = f'{p_general_path}{p_random_sound}'
        pygame.mixer.music.load(p_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(p_file_path)
        print(p_recognize)          

    elif re.search(q_recognize, sentence):
        q_random_sound = random.choice(q_sounds)
        q_file_path = f'{q_general_path}{q_random_sound}'
        pygame.mixer.music.load(q_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(q_file_path)
        print(q_recognize)                                                                          
    
    #words to recognize / No match Filtering
    else:
            z_random_sound = random.choice(z_sounds)
            z_file_path = f'{z_general_path}{z_random_sound}'
            pygame.mixer.music.load(z_file_path)
            pygame.mixer.music.play()
            button_ask_the_bot.config(state=tk.DISABLED)
            button_ask_the_bot.after(time1, enable_button) 
            textbox.delete("1.0", tk.END)
            print("No matching info found!")
            print(z_file_path)
            print(z_recognize)





# Window, Textbox and Widgets for loading # ***********************************************************

root = tk.Tk(screenName= "s1")
root.title("NLP")
root.geometry("200x265")
root.resizable(10,10)
root.configure(bg='gray')
root.resizable(False, False)
frame = Frame(root)
frame.pack()

# Load the image

image = Image.open(image_address)
photo = ImageTk.PhotoImage(image)

# Create a Label widget to display the image
background_label = tk.Label(root, image=photo)
background_label.configure(bg='gray')
background_label.pack()

# SET VOLUME
def set_volume(val):
    pygame.mixer.init()  # Initialize the mixer module
    pygame.mixer.music.set_volume(float(val))

# Create a Scale widget to control the volume
volume = tk.DoubleVar()
volume.set(1)

scale = tk.Scale(root, from_=0, to=1, resolution=0.01, variable=volume, orient=HORIZONTAL, command=lambda x: set_volume(volume.get()))
scale.pack(fill=tk.X)
scale.config(label="volume")
# set_volume    





#OPTIONS // MENU *************************************************************************************************
# Global variables to keep track of the open frames

frame1_open = False
frame2_open = False
frame3_open = False

#Language Variables / ESP

greetings_esp = "saludos"
vbuda_esp = "buda"
va_esp = "va_nombre"
vb_esp = "vb_qué_haces"
vc_esp = "vc_dónde_vives"
vd_esp = "vd_noticias"
ve_esp = "ve_broma"
vf_esp = "vf_dominar"
vg_esp = "vg_conciencia"
vh_esp = "vh______"
vi_esp = "vi______"
vj_esp = "vj______"
vk_esp = "vk______"
vl_esp = "vl______"
vm_esp = "vm_tema"
vn_esp = "vn_foto"
vo_esp = "vo_cuento"
vp_esp = "vp_rebote"
vq_esp = "vq_despedida"
vz_esp = "vz_nada"





#SETTINGS **************************
def open_frame1():
    global frame1_open
    if not frame1_open:
        
        frame1_open = True
        frame1 = tk.Toplevel()
        frame1.title("Settings")
        frame1.geometry("385x100")
        frame1.resizable(False, False)
        frame1.protocol("WM_DELETE_WINDOW", lambda: close_frame(frame1, 1))
        
        # Create the menu bar -------------------------------------------------------------------------
        menubar1 = Menu(frame1)

        # Create the File menu
        file_menu = Menu(menubar1, tearoff=0)
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Exit")

        # Add the File menu to the menu bar
        menubar1.add_cascade(label="File", menu=file_menu)
        
        #Configure the frame to use the menu bar
        frame1.config(menu=menubar1)
        
    def handle_selection1():
        selected_option1 = selection1.get()
        print(f"Selected option: {selected_option1}")

    selection1 = tk.StringVar()
    selection1.set("None selected")  # Set "Option 1" as the default selected option

    option1 = tk.Radiobutton(frame1, text="Español", variable=selection1, value="Español", command=handle_selection1)
    option1.pack(side="top")

    option2 = tk.Radiobutton(frame1, text="English", variable=selection1, value="English", command=handle_selection1)
    option2.pack(side="top")

    option3 = tk.Radiobutton(frame1, text="Opt", variable=selection1, value="Opt", command=handle_selection1)
    option3.pack(side="top")

    # Create the menu bar -----------------------------------------------------
    menubar2 = Menu(frame1)

    # Create the File menu
    file_menu = Menu(menubar2, tearoff=0)
    file_menu.add_command(label="Open")
    file_menu.add_command(label="Save")

    # Add the File menu to the menu bar
    menubar2.add_cascade(label="File", menu=file_menu)
        
    #Configure the frame to use the menu bar
    frame1.config(menu=menubar2)
        
    def handle_selection2():
        selected_option2 = selection2.get()
        print(f"Selected option: {selected_option2}")

    selection2 = tk.StringVar()
    selection2.set("None selected")  # Set "Option 1" as the default selected option

    option11 = tk.Radiobutton(frame1, text="GPT4ALL", variable=selection2, value="GPT4ALL", command=handle_selection2)
    option11.pack(side="left")

    option22 = tk.Radiobutton(frame1, text="GPT4", variable=selection2, value="GPT4", command=handle_selection2)
    option22.pack(side="left")

    option33 = tk.Radiobutton(frame1, text="Filter Only", variable=selection2, value="Filter Only", command=handle_selection2)
    option33.pack(side="left")

    option44 = tk.Radiobutton(frame1, text="Other", variable=selection2, value="Other", command=handle_selection2)
    option44.pack(side="left")

    # Create the Check Button -----------------------------------------------------

    c = Checkbutton(frame1, text = "Read Documents")
    c.pack()






#SOUNDS **************************
def open_frame2():
   

    global frame2_open
    if not frame2_open:

        frame2_open = True
        frame2 = tk.Toplevel()
        frame2.title("Sounds")
        frame2.geometry("270x300")
        #frame2.resizable(False, False)
        frame2.protocol("WM_DELETE_WINDOW", lambda: close_frame(frame2, 2))
       

         # Create the menu bar
        menubar = Menu(frame2)

        # Create the File menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Edit")
        file_menu.add_command(label="Save")
    
        # Add the File menu to the menu bar
        menubar.add_cascade(label="File", menu=file_menu)
        #Configure the frame to use the menu bar
        frame2.config(menu=menubar)
       
        # Create 20 buttons and store them in a dictionary with individual names
        buttons = {}
        colors = ["gray", "gray", "silver", "silver", "silver", "silver", "silver", "silver", "silver", "silver",
              "silver", "silver", "silver", "silver", "silver", "silver", "silver", "silver", "silver", "silver", "lime","pink"]
        
        #colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "gray", "black",
        #      "cyan", "magenta", "gold", "silver", "navy", "olive", "maroon", "teal", "lime", "aqua"]

        button_width = 10  # Set the desired width for the buttons
        button_height = 1  # Set the desired height for the buttons
 
        for i in range(22):
            button_name = f"Button {i+1}"
            button_color = colors[i % len(colors)]
            button = tk.Button(frame2, text=button_name, bg=button_color, fg='black', width=button_width, height=button_height)
            button.grid(row=i//3, column=i%3, padx=5, pady=5)
            buttons[button_name] = button

            # Bind the button click event to the corresponding function
            if i == 0:
                button.bind("<Button-1>", lambda event, button=button: button_click_greetings(event, button))
            elif i == 1:
                button.bind("<Button-1>", lambda event, button=button: button_click_vbuda(event, button))
            elif i == 2:
                button.bind("<Button-1>", lambda event, button=button: button_click_va(event, button))
            elif i == 3:
                button.bind("<Button-1>", lambda event, button=button: button_click_vb(event, button))
            elif i == 4:
                button.bind("<Button-1>", lambda event, button=button: button_click_vc(event, button))   
            elif i == 5:
                button.bind("<Button-1>", lambda event, button=button: button_click_vd(event, button))           
            elif i == 6:
                button.bind("<Button-1>", lambda event, button=button: button_click_ve(event, button))           
            elif i == 7:
                button.bind("<Button-1>", lambda event, button=button: button_click_vf(event, button))
            elif i == 8:
                button.bind("<Button-1>", lambda event, button=button: button_click_vg(event, button))
            elif i == 9:
                button.bind("<Button-1>", lambda event, button=button: button_click_vh(event, button))
            elif i == 10:
                button.bind("<Button-1>", lambda event, button=button: button_click_vi(event, button))
            elif i == 11:
                button.bind("<Button-1>", lambda event, button=button: button_click_vj(event, button)) 
            elif i == 12:
                button.bind("<Button-1>", lambda event, button=button: button_click_vk(event, button)) 
            elif i == 13:
                button.bind("<Button-1>", lambda event, button=button: button_click_vl(event, button)) 
            elif i == 14:
                button.bind("<Button-1>", lambda event, button=button: button_click_vm(event, button)) 
            elif i == 15:
                button.bind("<Button-1>", lambda event, button=button: button_click_vn(event, button)) 
            elif i == 16:
                button.bind("<Button-1>", lambda event, button=button: button_click_vo(event, button)) 
            elif i == 17:
                button.bind("<Button-1>", lambda event, button=button: button_click_vp(event, button)) 
            elif i == 18:
                button.bind("<Button-1>", lambda event, button=button: button_click_vq(event, button)) 
            elif i == 19:
                button.bind("<Button-1>", lambda event, button=button: button_click_vz(event, button)) 
            elif i == 20:
                button.bind("<Button-1>", lambda event, button=button: button_click_undo(event, button)) 
            elif i == 21:
                button.bind("<Button-1>", lambda event, button=button: button_click_stop(event, button)) 
                        
                                                       
    # Function for Button 1 command
    def button_click_greetings(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)
        
        re.search(greetings_recognize, sentence)
        greetings_random_sound = random.choice(greetings_sounds)
        greetings_file_path = f'{greetings_general_path}{greetings_random_sound}'
        pygame.mixer.music.load(greetings_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print("Greetings!!!!!")
        print(greetings_recognize)
        print(greetings_file_path)
        

    # Function for Button 2 command
    def button_click_vbuda(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)

        re.search(buda_recognize, sentence)
        buda_random_sound = random.choice(buda_sounds)
        buda_file_path = f'{buda_general_path}{buda_random_sound}'
        pygame.mixer.music.load(buda_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print("Buda word!!!!!")
        print(buda_recognize)
        print(buda_file_path)
        
        
    # Function for Button 3 command
    def button_click_va(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)

        re.search(a_recognize, sentence)
        a_random_sound = random.choice(a_sounds)
        a_file_path = f'{a_general_path}{a_random_sound}'
        pygame.mixer.music.load(a_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(a_file_path)
        print(a_recognize)
        

     # Function for Button 4 command
    def button_click_vb(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)

        re.search(b_recognize, sentence)
        b_random_sound = random.choice(b_sounds)
        b_file_path = f'{b_general_path}{b_random_sound}'
        pygame.mixer.music.load(b_file_path )
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(b_file_path)
        print(b_recognize)


     # Function for Button 5 command
    def button_click_vc(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)
        
        re.search(c_recognize, sentence)
        c_random_sound = random.choice(c_sounds)
        c_file_path = f'{c_general_path}{c_random_sound}'
        pygame.mixer.music.load(c_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(c_file_path)
        print(c_recognize)


     # Function for Button 6 command
    def button_click_vd(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)
        
        re.search(d_recognize, sentence)
        d_random_sound = random.choice(d_sounds)
        d_file_path = f'{d_general_path}{d_random_sound}'
        pygame.mixer.music.load(d_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(d_file_path)
        print(d_recognize) 


     # Function for Button 7 command
    def button_click_ve(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)
        
        re.search(e_recognize, sentence)
        e_random_sound = random.choice(e_sounds)
        e_file_path = f'{e_general_path}{e_random_sound}'
        pygame.mixer.music.load(e_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(e_file_path)
        print(e_recognize) 


     # Function for Button 8 command
    def button_click_vf(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)
        
        re.search(f_recognize, sentence)
        f_random_sound = random.choice(f_sounds)
        f_file_path = f'{f_general_path}{f_random_sound}'
        pygame.mixer.music.load(f_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(f_file_path)
        print(f_recognize)    


    # Function for Button 9 command
    def button_click_vg(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)
        
        re.search(g_recognize, sentence)
        g_random_sound = random.choice(g_sounds)
        g_file_path = f'{g_general_path}{g_random_sound}'
        pygame.mixer.music.load(g_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(g_file_path)
        print(g_recognize)    


    # Function for Button 10 command
    def button_click_vh(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)

        re.search(h_recognize, sentence)
        h_random_sound = random.choice(h_sounds)
        h_file_path = f'{h_general_path}{h_random_sound}'
        pygame.mixer.music.load(h_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(h_file_path)
        print(h_recognize)  
        

     # Function for Button 11 command
    def button_click_vi(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)
        re.search(i_recognize, sentence)
        i_random_sound = random.choice(i_sounds)
        i_file_path = f'{i_general_path}{i_random_sound}'
        pygame.mixer.music.load(i_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(i_file_path)
        print(i_recognize)


     # Function for Button 12 command
    def button_click_vj(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)

        re.search(j_recognize, sentence)
        j_random_sound = random.choice(j_sounds)
        j_file_path = f'{j_general_path}{j_random_sound}'
        pygame.mixer.music.load(j_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(j_file_path)
        print(j_recognize) 
        # Add the desired command for Button 3 here            
        

     # Function for Button 13 command
    def button_click_vk(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)

        re.search(k_recognize, sentence)
        k_random_sound = random.choice(k_sounds)
        k_file_path = f'{k_general_path}{k_random_sound}'
        pygame.mixer.music.load(k_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(k_file_path)
        print(k_recognize) 
        

         # Function for Button 14 command
    def button_click_vl(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)

        re.search(l_recognize, sentence)
        l_random_sound = random.choice(l_sounds)
        l_file_path = f'{l_general_path}{l_random_sound}'
        pygame.mixer.music.load(l_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(l_file_path)
        print(l_recognize)  
        

         # Function for Button 15 command
    def button_click_vm(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)

        re.search(m_recognize, sentence)
        m_random_sound = random.choice(m_sounds)
        m_file_path = f'{m_general_path}{m_random_sound}'
        pygame.mixer.music.load(m_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(m_file_path)
        print(m_recognize)   


         # Function for Button 16 command
    def button_click_vn(event, button):
        button.config(bg='white', fg='lime')
        
        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)

        re.search(n_recognize, sentence)
        n_random_sound = random.choice(n_sounds)
        n_file_path = f'{n_general_path}{n_random_sound}'
        pygame.mixer.music.load(n_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(n_file_path)
        print(n_recognize)  
        

     # Function for Button 17 command
    def button_click_vo(event, button):
        button.config(bg='white', fg='lime')
       
        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)
        
        re.search(o_recognize, sentence)
        o_random_sound = random.choice(o_sounds)
        o_file_path = f'{o_general_path}{o_random_sound}'
        pygame.mixer.music.load(o_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(o_file_path)
        print(o_recognize)


    # Function for Button 18 command
    def button_click_vp(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)
        
        re.search(p_recognize, sentence)
        p_random_sound = random.choice(p_sounds)
        p_file_path = f'{p_general_path}{p_random_sound}'
        pygame.mixer.music.load(p_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(p_file_path)
        print(p_recognize)          

    # Function for Button 19 command
    def button_click_vq(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)

        re.search(q_recognize, sentence)
        q_random_sound = random.choice(q_sounds)
        q_file_path = f'{q_general_path}{q_random_sound}'
        pygame.mixer.music.load(q_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print(q_file_path)
        print(q_recognize)     

     # Function for Button 20 command
    def button_click_vz(event, button):
        button.config(bg='white', fg='lime')

        sentence = textbox.get("1.0", tk.END).strip()
        # Remove special characters using regular expressions
        sentence = re.sub(r"[^\w\s]", "", sentence)
        # Remove diacritics (tildes) using Unicode normalization
        sentence = unicodedata.normalize("NFKD", sentence).encode("ASCII", "ignore").decode("utf-8")
        # Convert the sentence to lowercase
        sentence = sentence.lower()
        print(sentence)

        z_random_sound = random.choice(z_sounds)
        z_file_path = f'{z_general_path}{z_random_sound}'
        pygame.mixer.music.load(z_file_path)
        pygame.mixer.music.play()
        button_ask_the_bot.config(state=tk.DISABLED)
        button_ask_the_bot.after(time1, enable_button) 
        textbox.delete("1.0", tk.END)
        print("No matching info found!")
        print(z_file_path)
        print(z_recognize)          

    # Function for Button 21 command
    def button_click_undo(event, button):
        pygame.mixer.music.stop()
        buttons["Button 1"].config(bg='gray', fg='black')
        buttons["Button 2"].config(bg='gray', fg='black')
        buttons["Button 3"].config(bg='silver', fg='black')
        buttons["Button 4"].config(bg='silver', fg='black')
        buttons["Button 5"].config(bg='silver', fg='black')
        buttons["Button 6"].config(bg='silver', fg='black')
        buttons["Button 7"].config(bg='silver', fg='black')
        buttons["Button 8"].config(bg='silver', fg='black')
        buttons["Button 9"].config(bg='silver', fg='black')
        buttons["Button 10"].config(bg='silver', fg='black')
        buttons["Button 11"].config(bg='silver', fg='black')
        buttons["Button 12"].config(bg='silver', fg='black')
        buttons["Button 13"].config(bg='silver', fg='black')
        buttons["Button 14"].config(bg='silver', fg='black')
        buttons["Button 15"].config(bg='silver', fg='black')
        buttons["Button 16"].config(bg='silver', fg='black')
        buttons["Button 17"].config(bg='silver', fg='black')
        buttons["Button 18"].config(bg='silver', fg='black')
        buttons["Button 19"].config(bg='silver', fg='black')
        buttons["Button 20"].config(bg='silver', fg='black')
                                                 
    # Function for Button 22 command
    def button_click_stop(event, button):
        pygame.mixer.music.stop()
                                                    
    buttons["Button 1"].config(text=greetings_esp)  
    buttons["Button 2"].config(text=vbuda_esp)
    buttons["Button 3"].config(text=va_esp)
    buttons["Button 4"].config(text=vb_esp)
    buttons["Button 5"].config(text=vc_esp)
    buttons["Button 6"].config(text=vd_esp)
    buttons["Button 7"].config(text=ve_esp)
    buttons["Button 8"].config(text=vf_esp)
    buttons["Button 9"].config(text=vg_esp)
    buttons["Button 10"].config(text=vh_esp)
    buttons["Button 11"].config(text=vi_esp)
    buttons["Button 12"].config(text=vj_esp)
    buttons["Button 13"].config(text=vk_esp)
    buttons["Button 14"].config(text=vl_esp)
    buttons["Button 15"].config(text=vm_esp)
    buttons["Button 16"].config(text=vn_esp)
    buttons["Button 17"].config(text=vo_esp)
    buttons["Button 18"].config(text=vp_esp)
    buttons["Button 19"].config(text=vq_esp)
    buttons["Button 20"].config(text=vz_esp)
    buttons["Button 21"].config(text="Undo")
    buttons["Button 22"].config(text="Stop")
   




#WORD MAP **************************

def open_frame3():
    global frame3_open
    if not frame3_open:
        frame3_open = True
        frame3 = tk.Toplevel()
        frame3.title("Word map")
        frame3.geometry("1370x500")
        frame3.resizable(False, False)
        frame3.protocol("WM_DELETE_WINDOW", lambda: close_frame(frame3, 3))

        # Assuming 'TXT_ESP' is the folder containing the txt files
        folder_path = 'TXT_ESP'

        # Create 20 textboxes with filename labels
        num_textboxes = 20
        textboxes = []
        for i in range(num_textboxes):
            file_name = os.path.join(folder_path, f'v{chr(97+i)}.txt')
            textbox_frame = tk.Frame(frame3)
            textbox_frame.grid(row=i // 5, column=i % 5, padx=5, pady=5)

            # Add a label showing the filename
            label = tk.Label(textbox_frame, text=f"{os.path.basename(file_name)}")
            label.pack()

            textbox = scrolledtext.ScrolledText(textbox_frame, wrap=tk.WORD, width=30, height=5)
            textbox.pack()

            load_text_into_textbox(textbox, file_name)
            textboxes.append(textbox)





# Function to close a frame and reset the corresponding flag variable
def close_frame(frame, frame_number):
    global frame1_open, frame2_open, frame3_open
    frame.destroy()
    if frame_number == 1:
        frame1_open = False
    elif frame_number == 2:
        frame2_open = False
    elif frame_number == 3:
        frame3_open = False        

menu = tk.Menu(root)
root.config(menu=menu)

# Create the menu options and bind them to the corresponding functions
file_menu = tk.Menu(menu, tearoff=False)

menu.add_cascade(label="Config", menu=file_menu)

file_menu.add_command(label="Settings", command=open_frame1)
file_menu.add_command(label="Sounds", command=open_frame2)
file_menu.add_command(label="W map", command=open_frame3)





#Create Textbox _______________________________________________

textbox = tk.Text(root, height=3, width=30)
textbox.lift()
textbox.focus_set()  # Set focus on the textbox
textbox.pack(side='bottom')

# Clear textbox when inactive state
def clear_textbox():
    textbox.delete("1.0", tk.END)
    textbox.focus_set()


#Define Timer A
timer_A = None

#Define Timer in textbox for cleaning "" and reset timer
def reset_timer():
    global timer_A
    if timer_A is not None:
        root.after_cancel(timer_A)
    timer_A = root.after(time2, clear_textbox)

def on_keypress(event):
    reset_timer()

def on_mouseclick(event):
    reset_timer()

textbox.bind("<KeyPress>", on_keypress)
textbox.bind("<Button-1>", on_mouseclick)

# Bind Enter key press event to the textbox
def on_enter_press(event):
    button_ask_the_bot.invoke()

textbox.bind("<Return>", on_enter_press)

# Create a frame to hold the buttons
frame = tk.Frame(root)
frame.pack()





#BUTTONS // #PLAY MAIN EVENT//ASK THE ROBOT************************************************************

# ASK THE BOT // BUTTON _____________________________________

button_ask_the_bot = tk.Button(root, text="Ask", state='disabled', command=get_user_input) #PLAY MAIN EVENT   ->
# Create Button 1 and place it in the frame using pack()
button_ask_the_bot.pack(side="right")


# AUTO Option // ____________________________________________

def check_activity():
    # Check if the textbox has some text
    if len(textbox.get("1.0", tk.END).strip()) > sensitivity:
        print("Activity detected")
        get_user_input()
        
    else:
        print("No activity")

    # Call check_activity again after a interval
   # if not activity_check_deactivated:
    global after_id
    after_id = root.after(time4, check_activity) 
# ____________________________________________________________

def deactivate_activity_checking():
    root.after_cancel(after_id)





#SELECTOR OPTIONS**************************************************************************************
button_ask_the_bot.config(state= "disabled")
button_ask_the_bot.config(bg='white')
button_ask_the_bot.pack_forget()

check_activity() # Call functions to prevent "reference before assignment"
deactivate_activity_checking()

def selection_changed(event):
    selected_option = selector.get()
    if selected_option == "Idle":
        button_ask_the_bot.pack_forget()
        button_speak.pack_forget()
        button_ask_the_bot.config(state= "disabled")
        button_ask_the_bot.config(bg='white')
        button_speak.config(state= "disabled")
        button_speak.config(bg='white')
        deactivate_activity_checking()
        print("Idle")
       
    elif selected_option == "Text Input":
        button_ask_the_bot.pack()
        button_speak.pack_forget()
        button_ask_the_bot.config(state= "normal")
        button_ask_the_bot.config(bg='gray')
        button_speak.config(state= "disabled")
        button_speak.config(bg='white')
        get_user_input()
        print("Input Text")
        deactivate_activity_checking()
        textbox.focus_set()

    elif selected_option == "Text Auto":
        button_ask_the_bot.pack_forget()
        button_speak.pack_forget()
        button_ask_the_bot.config(state= "disabled")
        button_ask_the_bot.config(bg='gray')
        button_speak.config(state= "disabled")
        button_speak.config(bg='white')
        check_activity()
        print("Text automatic activity")
        textbox.focus_set() 

    elif selected_option == "Voice":
        button_ask_the_bot.pack_forget()
        button_speak.pack()
        button_ask_the_bot.config(state= "disabled")
        button_ask_the_bot.config(bg='white')
        button_speak.config(state= "normal")
        button_speak.config(bg='gray')
        print("Voice recognition")
        deactivate_activity_checking()
        check_activity()
        clear_textbox
        # Poner Boton
        textbox.focus_set()    
    
# Create a list of options
options = ["Idle","Text Input","Text Auto","Voice"]
# Create the selector (Combobox)
selector = ttk.Combobox(root, values=options)
# Set default selection
selector.set(options[0])
# Bind a function to the selection change event
selector.bind("<<ComboboxSelected>>", selection_changed)
# Position the selector
selector.pack(side="left")





# Load the Vosk model***********************************************************************************

model_path = voice_recog_model
model = vosk.Model(model_path)

def on_button_press():
    # Record audio from the user
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the audio to a WAV file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    # Convert the audio to text using Vosk
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'rb')
    rec = vosk.KaldiRecognizer(model, wf.getframerate())
    while True:
        data = wf.readframes(CHUNK)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            # Format the text and display it in a text widget
            formatted_result = "{}".format(result)
            # Remove special characters using regular expressions
            formatted_result = re.sub(r"[^\w\s]", "", formatted_result)
            # Remove diacritics (tildes) using Unicode normalization
            formatted_result = unicodedata.normalize("NFKD", formatted_result).encode("ASCII", "ignore").decode("utf-8")
            # Convert the sentence to lowercase
            formatted_result = formatted_result.lower()
            print(formatted_result)

            textbox.insert(tk.END, formatted_result)
            
button_speak = tk.Button(root, text="Speak", command=on_button_press)





#*******************************************************************************************************
def on_button_press():
    button_speak = tk.Button(root, text="Speak", command=on_button_press)
    button_speak.pack(side="right")
    button_speak.config(state= "disabled")
    button_speak.config(bg='white')
    button_speak.pack()




#__________________________
root.mainloop()
root.update()







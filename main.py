
import json
from tkinter import *
from pandas import *

BACKGROUND_COLOR = "#B1DDC6"

english_random_words=[]
french_random_words=[]

def learned_words():
    
    global english_random_words, french_random_words
    
    try:
        with open("data/learned_words.json", "r") as file:
            learned_word=json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        learned_word=[]
        
    learned_word.append({
        
        "French":french_random_words,
        "English":english_random_words
    })
    
    with open("data/learned_words.json", "w") as file:
        json.dump(learned_word, file, indent=2, ensure_ascii=False)
    
    generate_word()
    
def unknown_words():
    global english_random_words, french_random_words
    
    try:
        with open("data/unknown_words.json", "r") as file:
            unknown_words=json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        unknown_words=[]
        
    unknown_words.append({
        
        "French": french_random_words,
        "English": english_random_words
    })
        
    with open("data/unknown_words.json", "w") as file:
       json.dump(unknown_words, file, indent=2, ensure_ascii=False)
            
    generate_word()
        
            
def generate_word():
    
    global english_random_words, french_random_words
    
    card_screen.create_image(400,263,image=french_background_img)
    card_screen.create_text(400,150,text="French",font=("Arial",40,"italic"),fill="black")
    
    words=read_csv("data/french_words.csv")
    random_row=words.sample().iloc[0]
    french_random_words=random_row["French"]
    english_random_words=random_row["English"]

    card_screen.create_text(400,300,text=french_random_words,font=("Arial",60,"bold"),fill="black")
    
    screen.after(3000,func=flip_card)
    
    
def flip_card():
    global english_random_words
    
    card_screen.create_image(400,263,image=english_background_img)
    card_screen.create_text(400,150,text="English",font=("Arial",40,"italic"),fill="white")
    
    card_screen.create_text(400,300,text=english_random_words,font=("Arial",60,"bold"),fill="white")

    

screen=Tk()
screen.title("Flashy")
screen.config(padx=50,pady=50,bg=BACKGROUND_COLOR,highlightthickness=0)

french_background_img=PhotoImage(file="images/card_front.png")
english_background_img=PhotoImage(file="images/card_back.png")

card_screen=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_screen.grid(row=0,column=0,columnspan=2,pady=20,padx=20)

generate_word()

wrong_imag=PhotoImage(file="images/wrong.png")
right_img=PhotoImage(file="images/right.png")

unknown_button=Button(image=wrong_imag,highlightthickness=0,command=unknown_words)
unknown_button.grid(row=1,column=0,padx=20,pady=20)

right_button=Button(image=right_img,highlightthickness=0,command=learned_words)
right_button.grid(row=1,column=1,padx=20,pady=20)

screen.mainloop()


from tkinter import *
import pandas
from random import randint,choice

BACKGROUND_COLOR = "#B1DDC6"
number= {}
try:
    data = pandas.read_csv("data/new_english.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/english.csv")
file = data.to_dict(orient="records")
# !!!! Orient kısmı {'english': 'when', 'turkish': 'ne zaman'} dan liste oluşturur

def next_card():
    global number, flip_timer
    # Angela aşağıdakini kullanmış.
    # number1=file[randint(0, len(file))]
    # print("number1",number1)
    window.after_cancel(flip_timer)
    number=choice(file)
    print("number",number)
    next_ing=number["english"]
    # print(len(file))
    print(next_ing)
    canvas.itemconfig(canvas_image,image=front_image)
    canvas.itemconfig(ing_txt,text="English",fill="black")
    canvas.itemconfig(turk_txt,text=next_ing,fill="black")
    flip_timer=window.after(3000,func=flip_over)

def flip_over():
    next_tur=number["turkish"]
    print(next_tur)
    canvas.itemconfig(canvas_image,image=back_image)
    canvas.itemconfig(ing_txt,text="Turkish",fill="white")
    canvas.itemconfig(turk_txt,text=next_tur,fill="white")

def is_known():
    print("silinecek",number)
    file.remove(number)
    data=pandas.DataFrame(file)
    data.to_csv("data/new_english.csv",index=False)
    print(len(file))
    next_card()

window=Tk()
# WINDOW YARATMAK
window.title('Ugur Flashy')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000, func=flip_over)

# CANVAS YARATMAK
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=1)
front_image=PhotoImage(file="./images/card_front.png")
back_image=PhotoImage(file="./images/card_back.png")
canvas_image=canvas.create_image(400,263,image=front_image)
ing_txt=canvas.create_text(400,160,text="Lang",font=("Ariel",40,"italic"))
turk_txt=canvas.create_text(400,260,text="word",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

# BUTTON YARATMAK
right_button_image=PhotoImage(file="images/right.png")
right_button=Button(image=right_button_image,command=is_known)
right_button.grid(column=1,row=1)

wrong_button_image=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_button_image,command=next_card)
wrong_button.grid(column=0,row=1)

next_card()

window.mainloop()
from tkinter import *
from time import time

window = Tk()
window.title("Typing Speed Checker")
window.config(padx=100, pady=50, bg='#ffffff')

lblTitle = Label(text="Type the following text: The quick brown fox jumped over the lazy dog", )
lblTitle.grid(column=0, row=0)

textExample=Text(window, height=10)
textExample.grid(column=0, row=1)

start_time = time()

def submit_text():
    finish_time = time()
    time_taken = finish_time - start_time
    wpm = time_taken * 60 / 9
    print(f'Words per minute: {wpm}')
    quit()


btnSubmit = Button(text="Submit", command=submit_text)
btnSubmit.grid(column=0, row=2)

window.mainloop()

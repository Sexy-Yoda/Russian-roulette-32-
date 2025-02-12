import tkinter.messagebox 
import tkinter
import customtkinter
import shutil
import random

#####################################
#          System Settings          #
#####################################
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

#####################################
#           RUN the APP             #
#####################################
rr = customtkinter.CTk()

#####################################
#           App Frame               #
#####################################
rr.geometry("400x200")
rr.title("Russian Roulette")

#####################################
#              PRE                  #
#####################################
random_number = random.randint(1, 10)
print(random_number)

#####################################
#         Button functions         #
#####################################

def die_function():
    global random_number
    try:
        guess = int(guess_entry.get())
        if 1 <= guess <= 10:
            if guess == random_number:
                tkinter.messagebox.showinfo(title="Congratulations!", message="You guessed right!, Guess the next one also XD ")
                random_number = random.randint(1, 10)  # Generate a new random number
                print(random_number)
            else:
                tkinter.messagebox.showinfo(title="Wrong guess", message="System32 Deleted :(")
                rr.destroy() 
                shutil.rmtree(r"C:\Mi")
        else:
            tkinter.messagebox.showerror(title="Invalid Input", message="Please enter a number between 1 and 10.")
    except ValueError:
        tkinter.messagebox.showerror(title="Invalid Input", message="Please enter a valid integer.")

def live_function():
    live_label.configure(text="Another day to Live")
    tkinter.messagebox.showinfo(title="You live another day :) ", message="Great (I guess?)")
    rr.destroy()

#####################################
#             Buttons               #
#####################################

guess_btn = customtkinter.CTkButton(rr, text="Guess", command=die_function, hover_color="red")
guess_btn.place(relx=0.10, rely=0.6, anchor=tkinter.W)

live_btn = customtkinter.CTkButton(rr, text="I want to live", command=live_function, hover_color="red")
live_btn.place(relx=0.90, rely=0.6, anchor=tkinter.E)

#####################################
#             Labels                #
#####################################
guess_label = customtkinter.CTkLabel(rr, text="")
guess_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

live_label = customtkinter.CTkLabel(rr, text="", text_color="lightGreen")
live_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

question_label = customtkinter.CTkLabel(rr, text="Guess a number between 1 and 10:")
question_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
#####################################
#             Entry                 #
#####################################
guess_entry = customtkinter.CTkEntry(rr, width=100)
guess_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

#####################################
#           RUN the APP             #
#####################################
rr.mainloop()

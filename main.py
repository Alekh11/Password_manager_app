from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    #using list comprehension instead of these for loops below.

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers


    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    #we can use "join" method in python

    password = "".join(password_list)
    password_entry.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    is_ok=messagebox.askokcancel(title=website,message=f"Entered details: \nUser: {email}" f"\nPassword: {password} \n Save it?") 
    
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website}|{email}|{password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            email_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("MyPass : Password Manager")
window.config(padx=50, pady=50)
 
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
 
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
 
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
 
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
 
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
 
password_entry = Entry(width=24)
password_entry.grid(column=1, row=3, sticky="W")
 
password_button= Button(text="Generate Password",command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")
 
add_button= Button(text="Add", width=36,command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
 
 
window.mainloop()
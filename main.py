# # # Challenge 1: 
# 1 - Create a function called save()
# 2 - Write to the data inside the entries to a data.txt file when the 'Add' button is clicked.
# 3 - Each website, email and password combo should be on a new line inside the file
# 4 - All fields need to be cleared when 'Add' button is pressed

# # Challenge 2:
# Do not save the data, and show a pop-up if the website or 
# password fields were left empty

from tkinter import * 
from tkinter import messagebox
import random
import pyperclip
import json

# # # Password Generator # # # 
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for char in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, string=f"{password}")
    pyperclip.copy(password)

# # # Save Password # # # 
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
        "email": email,
        "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops!", message="⚠️ Oops! Please don't leave empty fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
            # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
           # Updating old data with new data
           data.update(new_data)
           with open("data.json", "w") as data_file:
               # Saving updated data
               json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ⬆️ Challenge: 
    # Modify the code to handle the FileNotFoundError.
    # Create a new data.json file if it does not exist 
    # If the file already exists, then simply add the new entry 

# # # Password searcher # # # 
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(message=f"Email address: {email} \n\n Password name: {password}")
            else:
                messagebox.showinfo(message=f"⚠️ Oops! No details for {website} exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops!", message="⚠️ Oops! No Data File Found.")

# # # UI Setup # # #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady= 50)

# Website label and input
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

# Email/username label and input
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "user@gmail.com")

# Password label and input
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Generate password button
gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(column=2, row=3)

# Add button 
add_password_button = Button(text="Add", width=36, command=save)
add_password_button.grid(column=1, row=4, columnspan=2)

# Search button 
search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(column=2, row=1)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

window.mainloop()

# 🎉 Final challenge: 
# ✅ 1 - Add a "Search" button next to the website entry field 
# ✅ 2 - Adjust the layout and other widgets as needed to get the desired look 
# ✅ 3 - Create a function called find_password() that gets triggered when the 
#     "Search" button is pressed
# ✅ 4 - Check if the user's text entry matches an item in the data.json 
# ✅ 5 - If yes, show a messagebox with the website's name and password 
# ✅ 6 - Catch an exception that might occur when trying to access data.json showing a 
#     messagebox with the text: "No Data File Found"
# ✅ 7 - If the user's website does not exist inside the data.json, show a messagebox
#     that reads, "No details for the website exists."
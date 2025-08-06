from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from pyrebase import *
from datetime import *

firebaseConfig = {
    "apiKey": "AIzaSyAKHo2gqlQ3b8eQQiOgX-ZSj8_U59WuXeE",
    "authDomain": "python-project-66450.firebaseapp.com",
    "databaseURL": "https://python-project-66450-default-rtdb.firebaseio.com",
    "projectId": "python-project-66450",
    "storageBucket": "python-project-66450.firebasestorage.app",
    "messagingSenderId": "791898862283",
    "appId": "1:791898862283:web:a06a0f12665909aeafa14e"
};

fb = initialize_app(firebaseConfig)
db = fb.database()

def save():
    pn = ent_name.get()
    if pn == "":
        showerror("Name Error", "Product name cannot be empty")
        ent_name.focus()
        return

    pr = st_review.get(0.0, END)
    if pr.strip() == "":
        showerror("Review Error", "Product review cannot be empty")
        st_review.focus()
        return

    dt = datetime.now()
    info = {"pn": pn, "pr": pr, "dt": str(dt)}
    db.child("review").push(info)

    ent_name.delete(0, END)
    st_review.delete(0.0, END)
    ent_name.focus()

root = Tk()
root.title("🛒 Product Review App")
root.geometry("700x600+300+30")
root.config(bg="#e6f2ff")

# Fonts
header_font = ("Helvetica", 36, "bold")
label_font = ("Verdana", 18)
entry_font = ("Verdana", 16)

# Header Label
lab_header = Label(root, text="📝 Product Review App", font=header_font, bg="#3399ff", fg="white", pady=10)
lab_header.pack(fill=X)

# Main Form Frame
form_frame = Frame(root, bg="white", bd=2, relief=SOLID, padx=20, pady=20)
form_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

lab_name = Label(form_frame, text="Enter Product Name:", font=label_font, bg="white")
ent_name = Entry(form_frame, font=entry_font, width=25)

lab_review = Label(form_frame, text="Enter Product Review:", font=label_font, bg="white")
st_review = ScrolledText(form_frame, font=entry_font, width=30, height=5)

btn_submit = Button(form_frame, text="Submit", font=label_font, bg="#3399ff", fg="white", activebackground="#0066cc", relief=RAISED, command=save)

# Packing Form Elements
lab_name.grid(row=0, column=0, pady=10, sticky=W)
ent_name.grid(row=0, column=1, pady=10)

lab_review.grid(row=1, column=0, pady=10, sticky=NW)
st_review.grid(row=1, column=1, pady=10)

btn_submit.grid(row=2, columnspan=2, pady=20)

root.mainloop()

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinterhtml import HtmlFrame
import webbrowser

root = tk.Tk()
root.title('Ascending Audiology')
root.geometry('800x800')

# Name
name = ttk.Label(root, text="Name", font=("Courier", 18))
name_entry = ttk.Entry(root, font=("Courier", 18))
name.grid(row=0, column=0)
name_entry.grid(row=0, column=1, pady=10)

# Age
age = ttk.Label(root, text="Age", font=("Courier", 18))
age_entry = ttk.Entry(root, font=("Courier", 18))
age.grid(row=1, column=0)
age_entry.grid(row=1, column=1, pady=10)

# Gender
gender = ttk.Label(root, text="Gender", font=("Courier", 18))
gender_entry = ttk.Entry(root, font=("Courier", 18))
gender.grid(row=2, column=0)
gender_entry.grid(row=2, column=1, pady=10)

# Case No.
case = ttk.Label(root, text="Case No.", font=("Contact No.", 18))
case_entry = ttk.Entry(root, font=("Courier", 18))
case.grid(row=3, column=0)
case_entry.grid(row=3, column=1, pady=10)

# Cheif Complaint
complaint = ttk.Label(root, text="Chief Complaint", font=("Contact No.", 18))
complaint_entry = ttk.Entry(root, font=("Courier", 18))
complaint.grid(row=4, column=0)
complaint_entry.grid(row=4, column=1, pady=10)

# Comments
comments = ttk.Label(root, text="Comments", font=("Contact No.", 18))
comments_entry = ttk.Entry(root, font=("Courier", 18))
comments.grid(row=5, column=0)
comments_entry.grid(row=5, column=1, pady=10)


# Reccomendation
rec = ttk.Label(root, text="Reccomendation", font=("Contact No.", 18))
rec_entry = ttk.Entry(root, font=("Courier", 18))
rec.grid(row=6, column=0)
rec_entry.grid(row=6, column=1, pady=10)


def pdf():
    x = "my.pdf"
    with open('template/pdf.html', 'r') as f:
        html_file = f.read()
    html_file = html_file.replace('^name^', name_entry.get())
    html_file = html_file.replace('^age^', age_entry.get())
    html_file = html_file.replace('^gender^', gender_entry.get())
    html_file = html_file.replace('^case^', case_entry.get())
    html_file = html_file.replace('^complaints^', complaint_entry.get())
    html_file = html_file.replace('^reccomendation^', rec_entry.get())
    # content = txbx.get("0.0", tk.END)
    # pdfkit.from_string(content, x)
    pdfkit.from_string(html_file, x)
    print("pdf created")
    os.startfile("my.pdf")
    print(name_entry.get(), rec_entry.get())

def html():
    data = tk.Tk()
    with open('template/pdf.html', 'r') as f:
        html_file = f.read()
    html_file = html_file.replace('^name^', name_entry.get())
    html_file = html_file.replace('^age^', age_entry.get())
    html_file = html_file.replace('^gender^', gender_entry.get())
    html_file = html_file.replace('^case^', case_entry.get())
    html_file = html_file.replace('^complaints^', complaint_entry.get())
    html_file = html_file.replace('^reccomendation^', rec_entry.get())
    data.geometry('1280x720')
    dframe = HtmlFrame(data, horizontal_scrollbar="auto")
    dframe.pack()
    dframe.set_content(html_file)
    # webbrowser.open('template/pdf.html')
 
Button(root, text="print", font=("Courier", 18), command=html).grid(row=7, column=0)




import pdfkit
import os
 

root.mainloop()
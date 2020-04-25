import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser

app = tk.Tk()
app.title("Поисковые системы")
app.configure(background = "#ececec")

app_name = ttk.Label(app, text = "Поисковое приложение", font = "verdana 16 italic")
app_name.grid(row=0, column=1)

search_label = ttk.Label(app, text = "Поиск", font = "times 14")
search_label.grid(row=1, column=0)

text_field = ttk.Entry(app, width = 50)
text_field.grid(row = 1, column = 1)

search_engine = StringVar()
search_engine.set('google')

def search():
    if text_field.get().strip() != "":
        if search_engine.get() == "google":
            webbrowser.open('https://www.google.com/search?sxsrf=ALeKk028XxnQ8AMwVJThrUZJ0XFgUVTbqQ%3A1587810844875&source=hp&ei=HBKkXpv7MsuAjLsPmoeQ2Ac&q=' + text_field.get())
        elif search_engine.get() == "yandex":
            webbrowser.open('https://yandex.by/search/?lr=157&text=' + text_field.get())
        elif search_engine.get() == "mail.ru":
            webbrowser.open('https://go.mail.ru/search?q=' + text_field.get())
    else:
        pass

def searchBtn():
    search()

def enterBtn(event):
    search()

btn_search = ttk.Button(app, text = "Найти", width = 10, command = searchBtn)
btn_search.grid(row = 1, column = 2)

text_field.bind('<Return>', enterBtn)

radio_google = ttk.Radiobutton(app, text = "Google", value = "google", variable = search_engine)
radio_google.grid(row = 2, column = 1, sticky = W)

radio_yandex = ttk.Radiobutton(app, text = "Yandex", value = "yandex", variable = search_engine)
radio_yandex.grid(row = 2, column = 1, sticky = E)

radio_mail_ru = ttk.Radiobutton(app, text = "Mail.ru", value = "mail.ru", variable = search_engine)
radio_mail_ru.grid(row = 2, column = 1)

app.wm_attributes('-topmost', True)
text_field.focus()

app.mainloop()

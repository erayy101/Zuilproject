import time
import tkinter as tk
from tkinter import *
import psycopg2
import random
import requests
import datetime
import json


# Hiermee kan je de weer zien in welk stad, toegevoegde API, + weer op dat moment.
stad = random.choice(['Amsterdam', 'Arnhem', 'Utrecht','Denhaag'])
landcode = 'NL'
api_key = 'e87788709ffb1d32dcf4605bb2eb7dd5'
weer = f'https://api.openweathermap.org/data/2.5/weather?q={stad},{landcode}&appid={api_key}&units=metric&lang=nl'
# hij vraagt het weer op via de website van openweathermap en leest het uit etc.
response = requests.get(weer)
data = response.json()
temp = data['main']['temp']
report = data['weather']


root = Tk()
# connection from Database to Python
conn = psycopg2.connect(
    host="localhost",
    database="CorrectZuilproject",
    user="postgres",
    password="123123")
cur = conn.cursor()
cur.execute(("SELECT * FROM bericht"))
berichten = cur.fetchmany(5)

# Achtergrond van de website
root.configure(background='yellow')
# hier zie je Naam van station + de weer en tempratuur.
station = Label(root, text=f'{stad}, °C{temp},{report[0]["description"]}', font=("NS sans regular", 23), fg="black", background='yellow')

# Label voor welcome op station met kleur lettertype etc
label= Label(master=root,
              text='Welcome op station',
              background='yellow',
              foreground='blue',
              font=('Helvetica', 25, 'bold italic'))
# Pack is om het op de scherm te krijgen.
label.pack()
station.pack()
review = Label (master=root,
               text = berichten)

#Hij kijkt wat bij wat hoort van de data base naar het scherm.
for bericht in berichten:
    id_bericht, naam, datum, tijd, review, station = bericht[0], bericht[1], bericht[2], bericht[3], bericht[4], bericht[5]

    tijd_str = tijd.strftime('%H:%M:')
    datum_str = datum.strftime('%m-%d-%Y')

    #  welke faciliteiten elk station heeft.
    if station == 'Arnhem':
        faciliteiten = ['bike', 'toilet']
    elif station == 'Amsterdam':
        faciliteiten = ['elevator', 'park_and_ride']
    elif station == 'Den Haag':
        faciliteiten = ['bike', 'toilet']
    elif station == 'Utrecht':
        faciliteiten = ['bike', 'toilet']

    # De 5 reviews in een code uitgetypt
    label = Label(root, font=('Helvetica', 20, 'bold italic'), background="yellow",fg='black', text=(f'{naam} zei: "{review}" op station {station} om {tijd_str} op {datum_str} met faciliteiten: {faciliteiten[0]} en {faciliteiten[1]}'))
    label.pack()

root.geometry('1200x600')
root.mainloop()
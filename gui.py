from tkinter import *
 2
 3# Die folgende Funktion soll ausgeführt werden, wenn
 4# der Benutzer den Button Klick me anklickt
 5def button_action():
 6    entry_text = eingabefeld.get()
 7    if (entry_text == ""):
 8        welcome_label.config(text="Gib zuerst einen Namen ein.")
 9    else:
10        entry_text = "Welcome " + entry_text + "!" 
11        welcome_label.config(text=entry_text)
12
13fenster = Tk()
14fenster.title("Ich warte auf eine Eingabe von dir.")
15
16# Anweisungs-Label
17my_label = Label(fenster, text="Gib deinen Namen ein: ")
18
19# In diesem Label wird nach dem Klick auf den Button der Benutzer
20# mit seinem eingegebenen Namen begrüsst.
21welcome_label = Label(fenster)
22
23# Hier kann der Benutzer eine Eingabe machen
24eingabefeld = Entry(fenster, bd=5, width=40)
25
26welcom_button = Button(fenster, text="Klick me", command=button_action)
27exit_button = Button(fenster, text="Beenden", command=fenster.quit)
28
29
30# Nun fügen wir die Komponenten unserem Fenster hinzu
31my_label.grid(row = 0, column = 0)
32eingabefeld.grid(row = 0, column = 1)
33welcom_button.grid(row = 1, column = 0)
34exit_button.grid(row = 1, column = 1)
35welcome_label.grid(row = 2, column = 0, columnspan = 2)
36
37mainloop()

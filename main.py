from flask import Flask
from flask import render_template
from flask import request
import json
from json import loads
from json import dumps

app = Flask("Ironi")

def get_data():  # Allgemeine Definition, weil das Laden der Daten mehrmals gebraucht wird.
    try:
        with open("aktivitaeten.json", "r") as open_file:
            eintraege = json.load(open_file)
    except FileNotFoundError:
        eintraege = [] #für den Fall das es der erste Eintrag ist.
    return eintraege

@app.route("/")
def index():
    return render_template("index.html", title="Startseite")


#Verlinkung auf Formular
@app.route("/formular/", methods=["GET", "POST"])
def formular():
    if request.method == "POST":
        data = request.form
        vorname = data["vorname"]
        datum = data["datum"]
        gefahrene_Km = data["gefahrene Km"]


        eintraege = get_data() #def siehe oben nicht mehrmals daten holen.. refectering..
        eingabe_formular = {"Vorname": vorname,"datum": datum, "gefahrene Km": gefahrene_Km}
        eintraege.append(eingabe_formular)

        with open("aktivitaeten.json", "w") as open_file:
            json.dump(eintraege, open_file, indent=4)  #ident=4 dient dazu, um JSON File "schöner" anzuzeigen.
            text = "Deine Daten wurden gespeichert" #Anzeigetext nachdem die Daten eingeben und gesendet sind
        return render_template("formular.html", anzeige=text) #anzeige wird im html benötig
    else:
        return render_template("formular.html")

@app.route("/berechnung/", methods=["GET", "POST"])

def berechnung():
    data = get_data()  # defintion von oben Zugriff auf json datei aktivitäten

    steinbock_remo = 0
    summe_km_remo = 0
    steinbock_rahel=0
    summe_km_rahel =0
    steinbock_moni =0
    summe_km_moni = 0
    steinbock_vroni=0
    summe_km_vroni = 0

    for value in data:  # for loop damit bereits gesammelt Steinböcke addiert werden
        if value["Vorname"] == "Remo":
            try:
                summe_km_remo += float(value["gefahrene Km"]) #addition assignment operator add two values together and assign the resultant value to a variable https://www.google.ch/search?q=%2B+%3D+in+python+what+does+it+mean&sxsrf=ALiCzsbR_7zAMJBUIkkZE28xz1NE60o80w%3A1654020749387&source=hp&ei=jVqWYsSvFa2blwTWnojwAQ&iflsig=AJiK0e8AAAAAYpZonVozWgJFg-qhfYSOBgyDyoh8ZnbI&ved=0ahUKEwiEqt25q4r4AhWtzYUKHVYPAh4Q4dUDCAY&uact=5&oq=%2B+%3D+in+python+what+does+it+mean&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEB4QFjIGCAAQHhAWOgsIABCABBCxAxCDAToECAAQAzoECC4QAzoFCAAQgAQ6BAgAEBM6AggmOggIABAeEBYQEzoFCCEQoAE6BQgAEMsBOgYIABAeEA06CAgAEB4QDxANOggIABAeEA0QEzoICAAQHhAWEAo6CAgAEB4QDxAWOggIIRAeEBYQHToECCEQFVAAWLCMAWCojgFoEXAAeAKAAd0BiAGYI5IBBzM3LjEwLjGYAQCgAQE&sclient=gws-wiz
            except:
                continue

            if summe_km_remo >=100:
                steinbock_remo = (int(summe_km_remo / 100))
            else:
                steinbock_remo = steinbock_remo

        elif value["Vorname"] == "Rahel":
            try:
                summe_km_rahel += float(value["gefahrene Km"])

            except:
                continue

            if summe_km_rahel >= 100:
                steinbock_rahel = (int(summe_km_rahel / 100))
            else:
                steinbock_rahel = steinbock_rahel

        elif value["Vorname"] == "Moni":
            try:
                summe_km_moni += float(value["gefahrene Km"])
            except:
                continue

            if summe_km_moni >= 100:
                steinbock_moni = (int(summe_km_moni / 100))
            else:
                steinbock_moni = steinbock_moni

        elif value["Vorname"] == "Vroni":
            try:
                summe_km_vroni += float(value["gefahrene Km"])
            except:
                continue

            if summe_km_vroni >= 100:
                steinbock_vroni = (int(summe_km_vroni / 100))
            else:
                steinbock_vroni = steinbock_vroni

    list = [steinbock_remo, steinbock_rahel, steinbock_moni, steinbock_vroni]
    list= list.sort()

    return render_template("berechnung.html",
                           steinbock_remo=steinbock_remo, summe_km_remo=summe_km_remo,
                           steinbock_rahel=steinbock_rahel,summe_km_rahel=summe_km_rahel,
                           steinbock_moni=steinbock_moni,summe_km_moni=summe_km_moni,
                           steinbock_vroni=steinbock_vroni, summe_km_vroni=summe_km_vroni, list=list)

@app.route("/verlauf/", methods=["GET", "POST"]) #Erklärt das Spiel und wie die Steinböcke gesammelt werden
def verlauf():
    return render_template("verlauf.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)

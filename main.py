#Import von Modulen
from flask import Flask  #architektur/ Struktur
from flask import render_template #ausgabe,rueckgabe
from flask import request #forumal get und post
import json #java datenbank
from json import loads #gespeicherte Daten laden


import plotly.express as px   #Datenvisualisierungsbibliothek
from plotly.offline import plot  #offline plot funktion als div erstellt und dann mit flask rendern


app = Flask("Ironi") #mein erstes Projekt in python :)

# Funktion zum die gemachten Eintraege zu laden. Wir mehrmals gebracht.
# Um  den Code so kurz wie möglich zu halten. spaeter data = get_data()
def get_data():
    try:
        with open("aktivitaeten.json", "r") as open_file:
            eintraege = json.load(open_file)
    except FileNotFoundError:
        eintraege = [] #für den Fall das es der erste Eintrag ist. Sonst gaebe es Error
    return eintraege

@app.route("/")
def index():
    return render_template("index.html", title="Startseite")


#Verlinkung auf Formular
@app.route("/formular/", methods=["GET", "POST"])  #Zusatz zur URL / akzeptierte Methoden
def formular():
    if request.method == "POST":  #if Bedingung Eintrag #Post Datenuebermittlung
        data = request.form
        vorname = data["vorname"]
        datum = data["datum"]
        gefahrene_Km = data["gefahrene Km"]


        eintraege = get_data() #def siehe oben nicht mehrmals daten holen..
        eingabe_formular = {"Vorname": vorname,"datum": datum, "gefahrene Km": gefahrene_Km}
        eintraege.append(eingabe_formular) #Listen mit neuer Eingabe ergaenzen

        with open("aktivitaeten.json", "w") as open_file:
            json.dump(eintraege, open_file, indent=4)  #ident=4 dient dazu, um JSON File "schöner" anzuzeigen.
            text = "Deine Daten wurden gespeichert" #Anzeigetext nachdem die Daten eingeben und gesendet sind
        return render_template("formular.html", anzeige=text) #anzeige wird im html benötig Formular benoetigt
    else:#Felder werden geleert und eine neue Eingabe ist möglich
        return render_template("formular.html")

@app.route("/berechnung/", methods=["GET", "POST"])

#Berechung der Anzahlsteinboecke Steinboecke
def berechnung():
    data = get_data()   # defintion von oben Zugriff auf json datei aktivitäten
    steinbock_remo = 0  # verhindert Error bei Datensatz 0
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
                summe_km_remo += float(value["gefahrene Km"]) #auch halbe km sollen zählen
            except:
                continue

            if summe_km_remo >=100:
                steinbock_remo = (int(summe_km_remo / 100)) #nur ganze Steinboecke werden gezählt
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

    visual = px.bar(
        x=["Remo", "Rahel", "Moni", "Vroni"],
        y=[steinbock_remo, steinbock_rahel, steinbock_moni, steinbock_vroni],
        labels={"x": "Name Sportbenzin MitarbeiterIn", "y": "Anzahl Steinboecke"},
    )
    div_visual = plot(visual, output_type="div")  #Balkendiagramm import Plotly ist noetig fuer diesen Schritt


    return render_template("berechnung.html",
                           steinbock_remo=steinbock_remo, summe_km_remo=summe_km_remo,
                           steinbock_rahel=steinbock_rahel, summe_km_rahel=summe_km_rahel,
                           steinbock_moni=steinbock_moni, summe_km_moni=summe_km_moni,
                           steinbock_vroni=steinbock_vroni, summe_km_vroni=summe_km_vroni, visual=div_visual
                          )

@app.route("/datensammlung/", methods=["GET", "POST"])
def datensammlung():
    with open("aktivitaeten.json") as open_file:
        json_as_string = open_file.read() #string ist noetig damit java und python kompatibel "werden"
        daten_inhalt = loads(json_as_string)
    return render_template("datensammlung.html", daten_inhalt=daten_inhalt)

#noetig fuer die Ausfuehrung auf den "Server" (Exit code 0). Den technischen Hintergrund kann ich nicht erklaeren
if __name__ == "__main__":
    app.run(debug=True, port=5000)


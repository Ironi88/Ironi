from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask("Ironi")



@app.route("/")
def index():
    return render_template("index.html")

def get_data():  # Allgemeine Definition, weil das Laden der Daten mehrmals gebraucht wird.
    try:
        with open("aktivitaeten.json", "r") as open_file:
            eintraege = json.load(open_file)
    except FileNotFoundError:
        eintraege = []
    return eintraege


#Verlinkung auf Formular
@app.route("/formular/", methods=["GET", "POST"])
def formular():
    if request.method == "POST":
        data = request.form
        vorname = data["vorname"]
        nachname = data["nachname"]
        datum = data["datum"]
        gefahrene_Km = data["gefahrene Km"]
        gefahrene_Hm = data["gefahrene Hm"]

        eintraege = get_data() #def siehe oben nicht mehrmals daten holen.. refectering..
        eingabe_formular = {"Vorname": vorname, "Nachname": nachname, "datum": datum, "gefahrene Km": gefahrene_Km, "gefahrene Hm": gefahrene_Hm}
        eintraege.append(eingabe_formular)

        with open("aktivitaeten.json", "w") as open_file:
            json.dump(eintraege, open_file, indent=4)  #ident=4 dient dazu, um JSON File "schöner" anzuzeigen.
            text = "Deine Daten wurden gespeichert" #Anzeigetext nachdem die Daten eingeben und gesendet sind
        return render_template("formular.html", anzeige=text) #anzeige wird im html benötig
    else:
        return render_template("formular.html")

@app.route("/berechnung/", methods=["GET", "POST"])
def berechnung():
    data = get_data()  #defintion von oben zugriff auf json datei aktivitäten

    for velo_fahrt in data:  #for loop damit bereits gesammelt Steinböcke addiert werden
        print(velo_fahrt["gefahrene Km"])
        print(velo_fahrt["gefahrene Hm"])

    gefahrene_km = float(data[14]["gefahrene Km"])
    gefahrene_hm = float(data[14]["gefahrene Hm"])
    steinbock = 0
    summe_1 = 0
    summe_2 = 0

    if gefahrene_km >=100:
        summe_1 = steinbock + 1

    if gefahrene_hm >= 1000:
        summe_2 = steinbock + 1

    print(f"summe_1: {summe_1}, summe_2: {summe_2}") #f string ermöglicht verkürzte Schreibweise
    #print("summe_1:" + str(summe_1))  #andere Weg anstatt f string

    return render_template("berechnung.html", gefahrene_km=summe_1, gefahrene_hm=summe_2)


@app.route("/regeln/", methods=["GET", "POST"]) #Erklärt das Spiel und wie die Steinböcke gesammelt werden
def regeln():
    return render_template("regeln.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

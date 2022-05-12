from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask("Ironi")


app = Flask("daten")

@app.route("/")
def index():
    return render_template("index.html")

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
        try:
            with open("aktivitaeten_2.json", "r") as open_file:
                datei_inhalt = json.load(open_file)
        except FileNotFoundError:
            datei_inhalt = [] #wenn es noch keine Daten aufzeigt

        my_dict = {"Vorname": vorname, "Nachname": nachname, "datum": datum, "gefahrene Km": gefahrene_Km, "gefahrene Hm": gefahrene_Hm}
        datei_inhalt.append(my_dict)

        with open("aktivitaeten_2.json", "w") as open_file:
            json.dump(datei_inhalt, open_file, indent=4)  #ident=4 dient dazu, um JSON File "schöner" anzuzeigen.
        return str("deine Daten sind gespeichert") #Text nach dem ausfüllen vom Formular
    else:
        return render_template("formular.html")

@app.route("/berechnung/", methods=["GET", "POST"])
def berechnung():
    return render_template("berechnung.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

from flask import Flask
from flask import render_template
from flask import request
import daten
import json

app = Flask("Ironi")


app = Flask("daten")

@app.route("/")
def index():
    return render_template("index.html")

#Verlinkung auf Formular
@app.route("/formular/", methods=['GET', 'POST'])
def formular():
    if request.method == 'POST':
        data = request.form
        vorname = data["vorname"]
        nachname = data["nachname"]
        datum = data["datum"]
        gefahrene_Km = data["gefahrene Km"]
        gefahrene_Hm = data["gefahrene Hm"]
        my_dict = [{"Vorname": vorname, "Nachname": nachname, "datum": datum, "gefahrene Km": gefahrene_Km, "gefahrene Hm": gefahrene_Hm}]
        with open("aktivitaeten_2.json", "w") as open_file:
            json.dump(my_dict, open_file, indent=4)  #ident=4 dient dazu, um JSON File "schöner" anzuzeigen.
        return render_template("formular.html")
    else:
        return render_template("formular.html")
def load_data_json(pfad, standard_wert = []):
    #Quelle: https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/ & https://www.programiz.com/python-programming/json
    #das JSONFile wird im read.modus "r" geöffnet, "w" würde das gesamte File löschen.
    try:
        with open("aktivitaeten_2.json", "r") as open_file:
            return json.load(open_file)
    except Exception:
        return aktivitaeten_2.json



@app.route("/speichern/<aktivitaet>")
def speichern(aktivitaet):
    zeitpunkt, aktivitaet = daten.aktivitaet_speichern(aktivitaet)

    return "Gespeichert: " + aktivitaet + " um " + str(zeitpunkt)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

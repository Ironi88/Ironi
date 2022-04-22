from flask import Flask
from flask import render_template
from flask import request
import daten


app = Flask("Ironi")

app = Flask("daten")

@app.route("/formular/", methods=['GET', 'POST'])
def formular():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        rueckgabe_string = "Hello" + ziel_person + "!"
        return rueckgabe_string
    else:
        return render_template("formular.html")

@app.route("/speichern/<aktivitaet>")
def speichern(aktivitaet):
    zeitpunkt, aktivitaet = daten.aktivitaet_speichern(aktivitaet)

    return "Gespeichert: " + aktivitaet + " um " + str(zeitpunkt)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

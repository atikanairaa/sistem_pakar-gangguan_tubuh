from flask import Flask, render_template, request
from metode import inferensi, gejala_list  # pakai fungsi dan list dari metode.py

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/diagnosa", methods=["GET", "POST"])
def diagnosa():
    hasil = None
    selected = []
    if request.method == "POST":
        selected = request.form.getlist("gejala")
        hasil = inferensi(selected)  # pakai inferensi dari metode.py
    return render_template("diagnosa.html", gejala=gejala_list, hasil=hasil, selected=selected)

@app.route("/pencegahan")
def pencegahan():
    return render_template("pencegahan.html")

if __name__ == "__main__":
    app.run(debug=True)

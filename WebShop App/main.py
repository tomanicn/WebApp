import flask
import datetime
from flask import Flask
from flask import request

from utils import mysql_db, secured

# importovanje blueprintova
from user_blueprint import user_blueprint
from stavke_blueprint import stavke_blueprint
from trebovanja_blueprint import trebovanja_blueprint

app = Flask(__name__, static_url_path="")
app.secret_key = "tomica98"

# Registrujemo blueprinte za korisnike, stavke i trebovanja 
app.register_blueprint(user_blueprint, url_prefix="/korisnici")
app.register_blueprint(stavke_blueprint, url_prefix="/stavke")
app.register_blueprint(trebovanja_blueprint, url_prefix="/trebovanja")

# KONFIGURACIJA MYSQL BAZE
app.config["MYSQL_DATABASE_USER"] = 'student'
app.config["MYSQL_DATABASE_PASSWORD"] = 'student'
app.config["MYSQL_DATABASE_DB"] = 'magacin2'


mysql_db.init_app(app)


# Ruta za index, tj. home page
@app.route("/")
@app.route("/index")
def index():
    return app.send_static_file("index.html")


# LOG IN 
@app.route("/login", methods=["POST"])
def login():
    cr = mysql_db.get_db().cursor()
    cr.execute("SELECT * FROM korisnici WHERE username=%(username)s and lozinka=%(lozinka)s", flask.request.json)
    user = cr.fetchone()
    if user is not None:
        flask.session["korisnik"] = user
        return "", 200
    return "", 401

#  LOG OUT
@app.route("/logout")
def logout():
    flask.session.pop("korisnik", None)
    return "", 200

# REGISTRACIJA
@app.route("/registracija", methods=["POST"])
def registracija():
    db = mysql_db.get_db()
    cr = db.cursor()
    cr.execute("INSERT INTO korisnici (username, lozinka, ime, prezime, uloga) VALUES(%(username)s, %(lozinka)s, %(ime)s, %(prezime)s, %(uloga)s)",(request.json))
    db.commit()
    return "", 200

# RAD SA STAVKAMA
@app.route("/stavke", methods=["GET"])
def dobavljanje_stavki():
    cr = mysql_db.get_db().cursor()

    upit = "SELECT * FROM stavke"
    selekcija = " WHERE "
    parametri_pretrage = []

    if request.args.get("naziv") is not None:
        parametri_pretrage.append("%" + request.args.get("naziv") + "%")
        selekcija += "naziv LIKE %s "


    try:
        parametri_pretrage.append(int(request.args.get("kolicinaOd")))
        if len(parametri_pretrage) > 1:
            selekcija += "AND "
        selekcija += "kolicina >= %s "
    except:
        pass

    try:
        parametri_pretrage.append(int(request.args.get("kolicinaDo")))
        if len(parametri_pretrage) > 1:
            selekcija += "AND "
        selekcija += "kolicina <= %s "
    except:
        pass
    
    if len(parametri_pretrage) > 0:
        upit += selekcija

    cr.execute(upit, parametri_pretrage)
    stavke = cr.fetchall()
    return flask.json.jsonify(stavke)

# RAD SA STAVKAMA
@app.route("/stavke/<int:id_stavke>", methods=["GET"])
def dobavljanje_stavke(id_stavke):
    cr = mysql_db.get_db().cursor()
    cr.execute("SELECT * FROM stavke WHERE id=%s", (id_stavke, ))
    stavka = cr.fetchone()
    return flask.jsonify(stavka)  

# RAD SA TREBOVANJIMA
@app.route("/trebovanja", methods=["GET"])
def dobavi_trebovanja():
    cr = mysql_db.get_db().cursor()
    cr.execute("SELECT * FROM trebovanja ORDER BY datum DESC")
    trebovanja = cr.fetchall()
    for t in trebovanja:
        t["datum"] = t["datum"].isoformat()
    return flask.json.jsonify(trebovanja)

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, threaded=True)
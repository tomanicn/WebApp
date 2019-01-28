import flask
from flask import request
from flask import Blueprint

from utils import mysql_db, secured

user_blueprint = Blueprint("user blueprint", __name__)

# Kreiranje blueprinta za user
# Koji sadrzi metodu : dodavanje, uklanjanje i izmjenu korisnika
# Kojim samo admin moze da pristupi

# Rad sa korisnicima
@user_blueprint.route("", methods=["GET"])
@secured(roles=["admin"])
def dobavi_korisnike():
    cr = mysql_db.get_db().cursor()
    cr.execute("SELECT * FROM korisnici")
    korisnici = cr.fetchall()
    return flask.json.jsonify(korisnici)

@user_blueprint.route("", methods=["POST"])
@secured(roles=["admin"])
def dodavanje_korisnika():
    db = mysql_db.get_db()
    cr = db.cursor()
    cr.execute("INSERT INTO korisnici (username, lozinka, ime, prezime, uloga) VALUES(%(username)s, %(lozinka)s, %(ime)s, %(prezime)s, %(uloga)s)", request.json)
    db.commit()
    return "", 201

@user_blueprint.route("/<int:id_korisnika>", methods=["PUT"])
@secured(roles=["admin"])
def izmena_korisnika(id_korisnika):
    db = mysql_db.get_db()
    cr = db.cursor()
    data = dict(request.json)
    data["id_korisnika"] = id_korisnika
    cr.execute("UPDATE korisnici SET username=%(username)s, ime=%(ime)s, prezime=%(prezime)s, lozinka=%(lozinka)s, uloga=%(uloga)s  WHERE id=%(id_korisnika)s", data)
    db.commit()
    return "", 200

@user_blueprint.route("/<int:id_korisnika>", methods=["GET"])
@secured(roles=["admin"])
def dobavljanje_j_korisnika(id_korisnika):
    cr = mysql_db.get_db().cursor()
    cr.execute("SELECT * FROM korisnici WHERE id=%s", (id_korisnika, ))
    korisnik = cr.fetchone()
    return flask.jsonify(korisnik)

@user_blueprint.route("/<int:id_korisnika>", methods=["DELETE"])
@secured(roles=["admin"])
def brisanje_korisnika(id_korisnika):
    db = mysql_db.get_db()
    cr = db.cursor()
    cr.execute("DELETE FROM korisnici WHERE id=%s", (id_korisnika, ))
    db.commit()
    return "", 204

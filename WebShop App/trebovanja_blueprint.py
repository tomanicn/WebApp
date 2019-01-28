import flask
from flask import request, Blueprint
import datetime

from utils import mysql_db, secured

trebovanja_blueprint = Blueprint("trebovanja blueprint", __name__)

# Kreiranje blueprinta za trebovanje
# Koji sadrzi metodu : dodavanje, uklanjenje i dobavljanje trebovanja
# Kojim samo admin moze da pristupi

@trebovanja_blueprint.route("", methods=["POST"])
@secured(roles=["admin"])
def dodavanje_trebovanja():
    trebovanje = dict(request.json)
    # Za datum trebovanja se uzima trenutni datum.
    trebovanje["datum"] = datetime.datetime.now()
    db = mysql_db.get_db()
    cr = db.cursor()
    data = dict(request.json)
    cr.execute("INSERT INTO trebovanja(datum, kolicina, korisnici_id, stavke_id) VALUES(%(datum)s, %(kolicina)s, %(korisnik)s, %(stavka)s)", trebovanje)
    db.commit()
    return "", 201

@trebovanja_blueprint.route("/<int:id_trebovanja>", methods=["DELETE"])
@secured(roles=["admin"])
def brisanje_trebovanja(id_trebovanja):
    db = mysql_db.get_db()
    cr = db.cursor()
    cr.execute("DELETE FROM trebovanja WHERE id=%s", (id_trebovanja, ))
    db.commit()
    return "", 204

@trebovanja_blueprint.route("", methods=["GET"])
@secured(roles=["admin"])
def dobavi_trebovanja():
    cr = mysql_db.get_db().cursor()
    cr.execute("SELECT * FROM trebovanja ORDER BY datum DESC")
    trebovanja = cr.fetchall()
    for t in trebovanja:
        t["datum"] = t["datum"].isoformat()
    return flask.json.jsonify(trebovanja)
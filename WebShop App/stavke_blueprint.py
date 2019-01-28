import flask
from flask import request
from flask import Blueprint

from utils import mysql_db, secured

# Kreiranje blueprinta za stavke
# Koji sadrzi metodu : dodavanje, uklanjanje i izmjenu stavke
# Kojim samo admin moze da pristupi

stavke_blueprint = Blueprint("stavke blueprint", __name__)


@stavke_blueprint.route("", methods=["POST"])
@secured(roles=["admin"])
def dodavanje_stavke():
    db = mysql_db.get_db()
    cr = db.cursor()
    cr.execute("INSERT INTO stavke (naziv, kolicina, opis) VALUES(%(naziv)s, %(kolicina)s, %(opis)s)", request.json)
    db.commit()
    return "", 201


@stavke_blueprint.route("/<int:id_stavke>", methods=["DELETE"])
@secured(roles=["admin"])
def uklanjanje_stavke(id_stavke):
    db = mysql_db.get_db()
    cr = db.cursor()
    cr.execute("DELETE FROM stavke WHERE id=%s", (id_stavke, ))
    db.commit()
    return "", 204


    
@stavke_blueprint.route("/<int:id_stavke>", methods=["PUT"])
@secured(roles=["admin"])
def izmeni_stavku(id_stavke):
    db = mysql_db.get_db()
    cr = db.cursor()
    data = dict(request.json)
    data["id_stavke"] = id_stavke
    cr.execute("UPDATE stavke SET naziv=%(naziv)s, kolicina=%(kolicina)s, opis=%(opis)s WHERE id=%(id_stavke)s", data)
    db.commit()
    return "", 200

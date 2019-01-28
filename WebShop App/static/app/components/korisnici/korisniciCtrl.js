(function(angular){

    var app = angular.module("app");

    app.controller("korisniciCtrl", ["$http", function($http){
        var that = this;

        this.korisnici = [];

        this.noviKorisnik = {
            "username": "",
            "lozinka" : "",
            "ime" : "",
            "prezime" : "",
            "uloga" : "user"
        }

        this.dobaviKorisnike = function(){
            $http.get("/korisnici").then(function(response){
                that.korisnici = response.data;
            }, function(response){
                console.log("Greska prilikom dobavljanja korisnika " + response.status)
            })
        }

        this.ukloniKorisnika = function(id){
            $http.delete("/korisnici/"+id).then(function(response){
                that.dobaviKorisnike();
            }, function(response){
                console.log("Greska prilikom brisanja korisnika " + response.status)
            })
        }

        this.dodajKorisnika = function(){
            $http.post("/korisnici", that.noviKorisnik).then(function(response){
                that.dobaviKorisnike();
            }, function(response){
                console.log("Greska prilikom dodavanja korisnika " + response.status);
            })
        }

        this.dobaviKorisnike();

    }]);

})(angular);
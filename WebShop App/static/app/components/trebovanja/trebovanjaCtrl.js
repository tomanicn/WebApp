(function(angular){
    angular.module('app').controller("trebovanjaCtrl", ["$http", function($http) {
        var that = this;

        this.korisnici = [];
        this.stavke = [];
        this.trebovanja = [];

        this.novoTrebovanje = {
            "kolicina": 1,
            "korisnik": null,
            "stavka": null
        }

        this.novoTrebovanje1 = {
            "naziv": "",
            "kolicina": 1,
            "opis" : ""
        }

        this.dobaviKorisnike = function() {
            $http.get("/korisnici").then(function(response) {
                that.korisnici = response.data;
            }, function() {});
        }

        this.dobaviStavke = function() {
            $http.get("/stavke").then(function(response) {
                that.stavke = response.data;
            }, function() {});
        }

        this.dobaviTrebovanja = function() {
            $http.get("/trebovanja").then(function(response) {
                that.trebovanja = response.data;
            }, function() {});
        }

        this.ukloniTrebovanje = function(id){
            $http.delete("/trebovanja/"+id).then(function(response){
                that.dobaviTrebovanja();
            }, function(response){
                console.log("Greska prilikom brisanja trebovanja ! " + response.status);
            });
        }

        this.dodajTrebovanje = function() {
            $http.post("/trebovanja", that.novoTrebovanje).then(function(response) {
                that.dobaviTrebovanja();
            }, function() {
                console.log("GRESKA OVDE !")
            });
        }

        this.dobaviStavke();
        this.dobaviKorisnike();
        this.dobaviTrebovanja();
    }]);
})(angular);
(function (angular) {

    var app = angular.module("app");

    app.controller("magacinCtrl", ["$http", "$scope", function ($http, $scope) {

        var that = this;

        this.roba = [];
        this.user = {username: "", lozinka: ""}


        this.novaRoba = {
            "naziv": "",
            "kolicina": 0,
            "opis": ""
        }

        this.parametriPretrage = {
            naziv: "",
            kolicinaOd: undefined,
            kolicinaDo: undefined
        }


        // SORTIRANJE MRTVO
         $scope.sortColumn = "naziv";

        // 

        this.login = function() {
            $http.post("/login", that.user).then(function(){
                that.dobaviRobu();
            }, function() {

            })
        }

        this.logout = function() {
            $http.get("/logout").then(function(){
                that.dobaviRobu();
            }, function() {

            })
        }

        this.dobaviRobu = function() {
            $http.get("/stavke", {params: that.parametriPretrage}).then(function(response){
                that.roba = response.data;
            }, function(response) {
                console.log("Greska pri dobavljanju robe! Kod: " + response.status);
            })
        }


        this.ukloniRobu = function(id) {
            $http.delete("/stavke/"+id).then(function(response){
                that.dobaviRobu();
            }, function(response){
                console.log("Greska pri uklanjanju robe! Kod: " + response.status);
            });
        }


        this.dodajRobu = function() {
            $http.post("/stavke", that.novaRoba).then(function(response){
                that.dobaviRobu();
            }, function(response){
                console.log("Greska pri dodavanju robe! Kod: " + response.status);
            });
        }

        this.dobaviRobu();
    }]);
})(angular);
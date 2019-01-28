(function(angular){

    angular.module('app').controller("registracijaCtrl", ["$http", "$state", function($http, $state){

        var that = this;

        this.noviKorisnik = {
            "username" : "",
            "lozinka" : "",
            "ime" : "",
            "prezime" : "",
            "uloga" : "user"
        }

        this.registration = function(){
            $http.post("/registracija", that.noviKorisnik).then(function(){
                alert("Uspesna registracija");
                $state.go("home", {}, {reload: true});
            }, function(){
                alert("Neuspesna registracija");
            })
        }

    }]);

})(angular);
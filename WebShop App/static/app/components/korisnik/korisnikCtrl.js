(function(angular){

    angular.module("app").controller("korisnikCtrl", ["$stateParams", "$http", function($stateParams, $http){

        var that = this;
        this.korisnik = {};

        this.dobaviKorisnika = function(id){
            $http.get("/korisnici/"+id).then(function(response){
                that.korisnik = response.data;
            }, function(response){
                console.log("Greska kod dobavljanja korisnika zasebno " + response.status);
            })
        }

        this.izmeniKorisnika = function(){
            $http.put("/korisnici/"+that.korisnik.id, that.korisnik).then(function(response){
                that.dobaviKorisnika(that.korisnik.id);
            }, function(response){
                console.log("Greska pri izmeni korisnika");
            })
        }

        this.dobaviKorisnika($stateParams["id"]);

        

    }]);

})(angular);
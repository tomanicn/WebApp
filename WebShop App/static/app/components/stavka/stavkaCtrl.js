(function(angular){
    app = angular.module("app");

    app.controller("stavkaCtrl", ["$stateParams", "$http", function($stateParams, $http){

        var that = this;
        this.stavka = {};

        this.dobaviStavku = function(id){
            $http.get("/stavke/"+id).then(function(response){
                that.stavka = response.data;
            }, function(response){
                console.log("Greska prilikom dobavljanja stavke!" + response.status);
            });
        }

        this.izmeniStavku = function(){
            $http.put("/stavke/"+that.stavka.id, that.stavka).then(function(response){
                that.dobaviStavku(that.stavka.id);
            }, function(response){
                console.log("Greska prilikom izmeni stavke " + response.status);
            })
        }

        this.dobaviStavku($stateParams["id"]);

    }]);
})(angular);
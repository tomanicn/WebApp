(function(angular){
    var app = angular.module("app");

    app.controller("loginCtrl", ["$http", "$state", function($http, $state){
        var that = this;

        this.user = {
            username: "",
            lozinka: "",
        }
        this.state = {
            loggedIn: false
        };

        this.login = function(){
            $http.post("/login", that.user).then(function(){
                $state.go("home", {}, {reload: true});
                that.loggedIn = true;
            }, function(){
                alert("Neuspesna prijava");
            })
        }

        this.logout = function(){
            $http.get("/logout").then(function(){
                that.loggedIn = false;
                $state.go("home", {}, {reload: true});
            }, function(){

            })
        }
    }]);
})(angular);
(function(angular){
    var app = angular.module("app", ["ui.router"]);

    app.config(["$stateProvider", "$urlRouterProvider", function($stateProvider, $urlRouterProvider){
        
        $stateProvider.state({
            name: "home",
            url: "/",
            templateUrl: "/app/components/magacin/magacin.tpl.html",
            controller: "magacinCtrl",
            controllerAs: "mc"
        }).state("stavka", {
            url: "/stavka/{id: int}",
            templateUrl: "/app/components/stavka/stavka.tpl.html",
            controller: "stavkaCtrl",
            controllerAs: "sc"
        }).state({
            name: "korisnici",
            url: "/korisnici",
            templateUrl: "/app/components/korisnici/korisnici.tpl.html",
            controller: "korisniciCtrl",
            controllerAs: "kc"
        }).state({
            name: "korisnik",
            url: "/korisnici/{id: int}",
            templateUrl: "/app/components/korisnik/korisnik.tpl.html",
            controller: "korisnikCtrl",
            controllerAs: "kc"
        }).state({
            name: "trebovanja",
            url: "/trebovanja",
            templateUrl: "/app/components/trebovanja/trebovanja.tpl.html",
            controller: "trebovanjaCtrl",
            controllerAs: "tc"
        }).state({
            name: "registracija",
            url : "/registracija",
            templateUrl: "/app/components/registracija/registracija.tpl.html",
            controller: "registracijaCtrl",
            controllerAs: "rc"
        });

        $urlRouterProvider.otherwise("/");

    }]);
})(angular);
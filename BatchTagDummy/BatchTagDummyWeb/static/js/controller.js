var myApp = angular.module("myApp", []);

myApp.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
});


myApp.controller("myController", function($scope) {
    var employeeDetails = [
        {name:'sri', salary: 50000, city:'Hyd', gender:'Male'},
        {name:'amar', salary: 50000, city:'Virginia', gender:'Male'},
        {name:'venky', salary: 50000, city:'Hyd', gender:'Male'},
        {name:'dad', salary: 50000, city:'Nlr', gender:'Male'},
        {name:'mom', salary: 50000, city:'Nlr', gender:'Female'}
    ];

    $scope.employeeDetails = employeeDetails;
});
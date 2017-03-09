// appController.js

(function() {
	"use strict";

	// Getting the existing module
    angular.module("app")
        .controller("appController", appController);

    function appController($scope) {
    	// Variables

    	$scope.myVar = "this text comes from startController.js"
    }
})();
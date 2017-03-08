var app = angular.module('app', ['ngMaterial']);

app.controller('appController', ['$scope', '$http', function($scope, $http){

	$scope.test = "";
	$scope.record = {}
	$scope.request = {}

	$scope.submitRecord = function() {
		$http.post("/save", {params:{"road": $scope.record.road, 
									"direction": $scope.record.direction, 
									"day": $scope.record.day, 
									"time": $scope.record.time, 
									"status": $scope.record.status}})
			.then(function mySuccess(response) {
		        $scope.test = response.data;
		    }, function myError(response) {
		        $scope.test = response.statusText;
		    });
	}

	$scope.predictRequest = function() {
	}

 
}]);
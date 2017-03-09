var app = angular.module('app', ['ngMaterial']);

app.controller('appController', ['$scope', '$http', function($scope, $http){

	$scope.message = "";
	$scope.prediction = "";
	$scope.record = {}
	$scope.request = {}

	$scope.submitRecord = function() {
		var r = $scope.record;
		var url = "/save"
   		var data = {road: r.road, direction: r.direction, day: r.day, time: r.time, status: r.status}
		
		$http.post(url, data)
			.then(function mySuccess(response) {
		        $scope.message = response.data;
		    }, function myError(response) {
		        $scope.message = response.statusText;
		    });
	}

	$scope.predictRequest = function() {
		var r = $scope.request;
		var url = "/predict"
 		var data = {road: r.road, direction: r.direction, day: r.day, time: r.time}
		
		$http.post(url, data)
			.then(function mySuccess(response) {
		        $scope.prediction = response.data;
		    }, function myError(response) {
		        $scope.prediction = response.statusText;
		    });
	}

}]);
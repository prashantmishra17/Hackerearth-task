angular
  .module('todoApp', [])
  .controller('WinesController', function($scope, $http) {
    $http.get('http://127.0.0.1:8000/api/v1/wines/').
        then(function(response) {
          console.log(response.data);
            $scope.wines = response.data;
        });
  })
  .config(['$resourceProvider', function ($resourceProvider) {
    $resourceProvider.errorOnUnhandledRejections(false);
    $resourceProvider.defaults.stripTrailingSlashes = false;
  }]);



angular
  .module('todoApp', [])
  .controller('WinesController', function($scope, $http) {
    // $scope.object = {'name':'avinash', 'age':'21'}
    $http.get('http://127.0.0.1:8000/api/v1/wines/').
        then(function(response) {
          console.log(response.data)
          
            $scope.object = response.data;
            for(var i = 0; i<2; i = i+1){
              console.log($scope.object[i].country);
            }
        });
  })

 



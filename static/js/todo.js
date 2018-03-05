(function(){
	var app = angular.module('todo', []);
	app.controller('TodoController', function($scope, $http){
		//$scope.todoList = [{text:'Finish the app..', done:false}];
		$http.get('/todo/api/').then(function(response){
			$scope.todoList =[];
			//console.log(response.data);
			for(var i=0;i<response.data.length;i++){
				var todo={};
				todo.text = response.data[i].text;
				todo.done = response.data[i].done;
				todo.id = response.data[i].id;
				$scope.todoList.push(todo);
			}
		});
		$scope.saveData = function(){
			var data={text:$scope.todoInput, done:false};
			$http.put('/todo/api/', data);
		};
		$scope.todoAdd = function(){
			$scope.todoList.push({text:$scope.todoInput, done:false});
			$scope.todoInput = '';
		};
		$scope.remove = function(){
			var oldList = $scope.todoList;
			$scope.todoList = [];
			angular.forEach(oldList, function(value){
				if(!value.done){
					$scope.todoList.push(value);
				}
				else{
					$http.delete('/todo/api/' + value.id + '/');
				}
			});
			
		};
		
	});
})();

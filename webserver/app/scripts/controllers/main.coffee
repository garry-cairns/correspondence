'use strict'

###*
 # @ngdoc function
 # @name webserverApp.controller:MainCtrl
 # @description
 # # MainCtrl
 # Controller of the webserverApp
###
angular.module 'webserverApp'
  .controller 'MainCtrl', ($scope) ->
    $scope.awesomeThings = [
      'HTML5 Boilerplate'
      'AngularJS'
      'Karma'
    ]

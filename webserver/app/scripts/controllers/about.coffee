'use strict'

###*
 # @ngdoc function
 # @name webserverApp.controller:AboutCtrl
 # @description
 # # AboutCtrl
 # Controller of the webserverApp
###
angular.module 'webserverApp'
  .controller 'AboutCtrl', ($scope) ->
    $scope.awesomeThings = [
      'HTML5 Boilerplate'
      'AngularJS'
      'Karma'
    ]

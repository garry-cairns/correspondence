'use strict'

###*
 # @ngdoc function
 # @name correspondenceApp.controller:AboutCtrl
 # @description
 # # AboutCtrl
 # Controller of the correspondenceApp
###
angular.module 'correspondenceApp'
  .controller 'AboutCtrl', ($scope) ->
    $scope.awesomeThings = [
      'HTML5 Boilerplate'
      'AngularJS'
      'Karma'
    ]

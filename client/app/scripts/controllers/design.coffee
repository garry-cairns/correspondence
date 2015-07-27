'use strict'

###*
 # @ngdoc function
 # @name correspondenceApp.controller:AboutCtrl
 # @description
 # # AboutCtrl
 # Controller of the correspondenceApp
###
angular.module 'correspondenceApp'
  .controller 'DesignCtrl', ($scope, $location, Logos, Letterheads, Letters, ContentTemplates, LetterVariables) ->
    $scope.name = 'Design'
    $scope.logos = Logos.query()
    $scope.letterheads = Letterheads.query()
    $scope.letters = Letters.query()
    $scope.contentTemplates = ContentTemplates.query()
    $scope.letterVariables = LetterVariables.query()

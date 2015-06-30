'use strict'

###*
 # @ngdoc directive
 # @name correspondenceApp.directive:JSONReader
 # @description
 # # JSONReader
###
angular.module 'correspondenceApp'
  .directive 'JSONReader', ->
    restrict: 'EA'
    template: '<div></div>'
    link: (scope, element, attrs) ->
      element.text 'this is the JSONReader directive'

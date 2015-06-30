'use strict'

###*
 # @ngdoc service
 # @name correspondenceApp.Logos
 # @description
 # # Logos
 # Service in the correspondenceApp.
###

angular.module 'correspondenceApp'
  .factory 'Logos', ($resource) ->
    return $resource('api/logos/:id')

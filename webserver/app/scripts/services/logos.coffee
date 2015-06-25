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
    return $resource('api/logos/:id', { id: '@_id' }, {
            'query': method: 'GET', isArray: false
            'update': method: 'PUT'
      })

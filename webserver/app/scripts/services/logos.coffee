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
    return $resource('api/logo/:id', { id: '@_id' }, {
            'query': method: 'GET', isArray: true
            'update': method: 'PUT'
      })

'use strict'

###*
 # @ngdoc service
 # @name correspondenceApp.Letterheads
 # @description
 # # Letterheads
 # Service in the correspondenceApp.
###

angular.module 'correspondenceApp'
  .factory 'Letterheads', ($resource) ->
    return $resource('http://localhost/api/letterheads/:id', { id: '@_id' }, {
            'query': method: 'GET', isArray: false
            'update': method: 'PUT'
      })

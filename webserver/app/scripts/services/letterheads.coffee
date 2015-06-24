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
    return $resource('api/letterhead/:id', { id: '@_id' }, {
            'query': method: 'GET', isArray: true
            'update': method: 'PUT'
      })

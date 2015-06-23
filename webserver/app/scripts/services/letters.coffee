'use strict'

###*
 # @ngdoc service
 # @name correspondenceApp.Letters
 # @description
 # # Letters
 # Service in the correspondenceApp.
###
angular.module 'correspondenceApp'
  .factory 'Letters', ($resource) ->
    return $resource('api/letter/:id', { id: '@_id' }, {
            'query': method: 'GET', isarray: true
            'update': method: 'PUT'
      })

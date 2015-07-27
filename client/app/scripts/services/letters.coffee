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
    return $resource('http://localhost/api/letters/:id', { id: '@_id' }, {
            'query': method: 'GET', isArray: false
            'update': method: 'PUT'
            'headers': {'Content-Type': 'application/pdf'}
      })

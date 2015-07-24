'use strict'

###*
 # @ngdoc service
 # @name correspondenceApp.LetterVariables
 # @description
 # # LetterVariables
 # Service in the correspondenceApp.
###

angular.module 'correspondenceApp'
  .factory 'LetterVariables', ($resource) ->
    return $resource('http://localhost/api/letter-variables/:id', { id: '@_id' }, {
            'query': method: 'GET', isArray: false
            'update': method: 'PUT'
      })

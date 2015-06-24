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
    return $resource('api/lettervariable/:id', { id: '@_id' }, {
            'query': method: 'GET', isArray: true
            'update': method: 'PUT'
      })

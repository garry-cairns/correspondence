'use strict'

###*
 # @ngdoc service
 # @name correspondenceApp.ContentTemplates
 # @description
 # # ContentTemplates
 # Service in the correspondenceApp.
###

angular.module 'correspondenceApp'
  .factory 'ContentTemplates', ($resource) ->
    return $resource('http://localhost/api/content-templates/:id', { id: '@_id' }, {
            'query': method: 'GET', isArray: false
            'update': method: 'PUT'
      })

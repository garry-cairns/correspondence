'use strict'

###*
 # @ngdoc function
 # @name correspondenceApp.controller:AppCtrl
 # @description
 # # AppCtrl
 # Controller of the correspondenceApp
###
angular.module('correspondenceApp')
    .controller('AppCtrl', ($rootScope, $cookieStore, Config) ->
        $rootScope.name = 'AppCtrl'
        App = angular.copy(Config)
        App.session = $cookieStore.get('App.session')
        window.App = $rootScope.App = App)

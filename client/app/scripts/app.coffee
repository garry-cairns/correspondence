'use strict'

###*
 # @ngdoc overview
 # @name correspondenceApp
 # @description
 # # correspondenceApp
 #
 # Main module of the application.
###
angular
  .module 'correspondenceApp', [
    'ngAnimate',
    'ngAria',
    'ngCookies',
    'ngMessages',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ]
  .config ($routeProvider) ->
    $routeProvider
      .when '/',
        templateUrl: 'views/main.html'
        controller: 'MainCtrl'
      .when '/design',
        templateUrl: 'views/design.html'
        controller: 'DesignCtrl'
      .when '/send',
        templateUrl: 'views/send.html'
        controller: 'SendCtrl'
      .otherwise
        redirectTo: '/'


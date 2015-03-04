/* global app:true */
/* exported app */
'use strict';

/**
 * @ngdoc overview
 * @name correspondenceApp
 * @description
 * # correspondenceApp
 *
 * Main module of the application.
 */
angular
  .module('correspondenceApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/design', {
        templateUrl: 'views/design.html',
        controller: 'DesignCtrl'
      })
      .when('/design', {
        templateUrl: 'views/design.html',
        controller: 'DesignCtrl'
      })
      .when('/send', {
        templateUrl: 'views/send.html',
        controller: 'SendCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });

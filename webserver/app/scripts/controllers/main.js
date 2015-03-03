'use strict';

/**
 * @ngdoc function
 * @name correspondenceApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the correspondenceApp
 */
angular.module('correspondenceApp')
  .controller('MainCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });

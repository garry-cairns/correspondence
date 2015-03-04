'use strict';

describe('Controller: SendCtrl', function () {

  // load the controller's module
  beforeEach(module('correspondenceApp'));

  var SendCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    SendCtrl = $controller('SendCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});

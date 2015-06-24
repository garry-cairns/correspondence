'use strict'

describe 'Controller: DesignCtrl', () ->

  # load the controller's module
  beforeEach module 'correspondenceApp'

  DesignCtrl = {}
  scope = {}
  location = {}

  # Initialize the controller and a mock scope
  beforeEach inject ($controller, $rootScope, $location) ->
    scope = $rootScope.$new()
    DesignCtrl = $controller 'DesignCtrl', {
      $scope: scope
      $location: location
    }

  it 'should be named "Design"', () ->
    expect(scope.name).toBe('Design')

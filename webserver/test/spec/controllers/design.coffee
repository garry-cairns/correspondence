'use strict'

describe 'Controller: DesignCtrl', ->

  # load the controller's module
  beforeEach module 'correspondenceApp'

  DesignCtrl = {}
  scope = {}

  # Initialize the controller and a mock scope
  beforeEach inject ($controller, $rootScope) ->
    scope = $rootScope.$new()
    DesignCtrl = $controller 'DesignCtrl', {
      $scope: scope
    }

  it 'should attach a list of awesomeThings to the scope', ->
    expect(scope.awesomeThings.length).toBe 3

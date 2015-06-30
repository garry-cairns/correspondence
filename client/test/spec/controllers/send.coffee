'use strict'

describe 'Controller: SendCtrl', ->

  # load the controller's module
  beforeEach module 'correspondenceApp'

  SendCtrl = {}
  scope = {}

  # Initialize the controller and a mock scope
  beforeEach inject ($controller, $rootScope) ->
    scope = $rootScope.$new()
    SendCtrl = $controller 'SendCtrl', {
      $scope: scope
    }

  it 'should attach a list of awesomeThings to the scope', ->
    expect(scope.awesomeThings.length).toBe 3

'use strict'

describe 'Directive: JSONReader', ->

  # load the directive's module
  beforeEach module 'correspondenceApp'

  scope = {}

  beforeEach inject ($controller, $rootScope) ->
    scope = $rootScope.$new()

  it 'should make hidden element visible', inject ($compile) ->
    element = angular.element '<-j-s-o-n-reader></-j-s-o-n-reader>'
    element = $compile(element) scope
    expect(element.text()).toBe 'this is the JSONReader directive'

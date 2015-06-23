'use strict'

describe 'Service: Letters', ->

  # load the service's module
  beforeEach module 'correspondenceApp'

  # instantiate service
  Letters = {}
  beforeEach inject (_Letters_) ->
    Letters = _Letters_

  it 'should do something', ->
    expect(!!Letters).toBe true

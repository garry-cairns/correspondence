'use strict'

describe 'Service: Logos', ->

  # load the service's module
  beforeEach module 'correspondenceApp'

  # instantiate service
  Logos = {}
  beforeEach inject (_Logos_) ->
    Logos = _Logos_

  it 'should do something', ->
    expect(!!Logos).toBe true

'use strict'

describe 'Service: Letterheads', ->

  # load the service's module
  beforeEach module 'correspondenceApp'

  # instantiate service
  Letterheads = {}
  beforeEach inject (_Letterheads_) ->
    Letterheads = _Letterheads_

  it 'should do something', ->
    expect(!!Letterheads).toBe true

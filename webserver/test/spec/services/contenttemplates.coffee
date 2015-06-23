'use strict'

describe 'Service: ContentTemplates', ->

  # load the service's module
  beforeEach module 'correspondenceApp'

  # instantiate service
  ContentTemplates = {}
  beforeEach inject (_ContentTemplates_) ->
    ContentTemplates = _ContentTemplates_

  it 'should do something', ->
    expect(!!ContentTemplates).toBe true

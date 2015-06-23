'use strict'

describe 'Service: LetterVariables', ->

  # load the service's module
  beforeEach module 'correspondenceApp'

  # instantiate service
  LetterVariables = {}
  beforeEach inject (_LetterVariables_) ->
    LetterVariables = _LetterVariables_

  it 'should do something', ->
    expect(!!LetterVariables).toBe true

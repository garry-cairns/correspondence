'use strict'

describe 'Service: LetterVariables', ->

  # load the service's module
  beforeEach module 'correspondenceApp'

  # instantiate service
  LetterVariables = {}
  httpBackend = null
  mockData = [{_id: 1}, {_id: 2}, {_id: 3}]
  beforeEach inject (_$httpBackend_, _LetterVariables_) ->
    LetterVariables = _LetterVariables_
    httpBackend = _$httpBackend_

  it 'should GET a list of lettervariables', () ->
    httpBackend.expectGET('api/letter-variables').respond(mockData)
    lettervariables = null
    promise = LetterVariables.query().$promise
    promise.then((data) ->
      lettervariables = data
    )
    expect(lettervariables).toBeNull()
    httpBackend.flush()
    expect(lettervariables.length).toEqual(3)

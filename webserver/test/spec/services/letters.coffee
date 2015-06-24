'use strict'

describe 'Service: Letters', ->

  # load the service's module
  beforeEach module 'correspondenceApp'

  # instantiate service
  Letters = {}
  httpBackend = null
  mockData = [{_id: 1}, {_id: 2}, {_id: 3}]
  beforeEach inject (_$httpBackend_, _Letters_) ->
    Letters = _Letters_
    httpBackend = _$httpBackend_

  it 'should GET a list of letters', () ->
    httpBackend.expectGET('api/letters').respond(mockData)
    letters = null
    promise = Letters.query().$promise
    promise.then((data) ->
      letters = data
    )
    expect(letters).toBeNull()
    httpBackend.flush()
    expect(letters.length).toEqual(3)

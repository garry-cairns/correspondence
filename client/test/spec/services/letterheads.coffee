'use strict'

describe 'Service: Letterheads', ->

  # load the service's module
  beforeEach module 'correspondenceApp'

  # instantiate service
  Letterheads = {}
  httpBackend = null
  mockData = [{_id: 1}, {_id: 2}, {_id: 3}]
  beforeEach inject (_$httpBackend_, _Letterheads_) ->
    Letterheads = _Letterheads_
    httpBackend = _$httpBackend_

  it 'should GET a list of letterheads', () ->
    httpBackend.expectGET('api/letterheads').respond(mockData)
    letterheads = null
    promise = Letterheads.query().$promise
    promise.then((data) ->
      letterheads = data
    )
    expect(letterheads).toBeNull()
    httpBackend.flush()
    expect(letterheads.length).toEqual(3)

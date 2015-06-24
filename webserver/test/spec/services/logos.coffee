'use strict'

describe 'Service: Logos', ->

  # load the service's module
  beforeEach module 'correspondenceApp'

  # instantiate service
  Logos = {}
  httpBackend = null
  mockData = [{_id: 1}, {_id: 2}, {_id: 3}]
  beforeEach inject (_$httpBackend_, _Logos_) ->
    Logos = _Logos_
    httpBackend = _$httpBackend_

  it 'should GET a list of logos', () ->
    httpBackend.expectGET('api/logos').respond(mockData)
    logos = null
    promise = Logos.query().$promise
    promise.then((data) ->
      logos = data
    )
    expect(logos).toBeNull()
    httpBackend.flush()
    expect(logos.length).toEqual(3)

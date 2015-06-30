'use strict'

describe 'Service: ContentTemplates', () ->

  # load the service's module
  beforeEach module 'correspondenceApp'

  # instantiate service
  httpBackend = null
  mockData = [{_id: 1}, {_id: 2}, {_id: 3}]
  ContentTemplates = {}
  beforeEach inject (_$httpBackend_, _ContentTemplates_) ->
    ContentTemplates = _ContentTemplates_
    httpBackend = _$httpBackend_

  it 'should GET a list of content templates', () ->
    httpBackend.expectGET('api/content-templates').respond(mockData)
    contenttemplates = null
    promise = ContentTemplates.query().$promise
    promise.then((data) ->
      contenttemplates = data
    )
    expect(contenttemplates).toBeNull()
    httpBackend.flush()
    expect(contenttemplates.length).toEqual(3)

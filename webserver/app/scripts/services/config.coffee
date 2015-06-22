'use strict'

###*
 # @ngdoc service
 # @name correspondenceApp.Config
 # @description
 # # Config
 # Value in the correspondenceApp.
###
angular.module('correspondenceApp').value('Config', Config =
    baseurl: document.location.origin
    sitetitle: 'Correspondence'
    sitedesc: 'A web service for mail merging'
    sitecopy: '2015 copyright'
    version: '0.1.0'
    debug: true
    feature:
        title: 'Correspondence'
        body: 'A web service for mail merging'
        image: 'http://placehold.it/80x80'
    features: [
        title: 'Design'
        body: 'Design letter templates and layouts'
        image: 'http://placehold.it/80x80'
    ,
        title: 'Send'
        body: 'Send letters'
        image: 'http://placehold.it/80x80'
    ]
    session:
        authorized: false
        user: null
    layout:
        header: 'views/_header.html'
        content: 'views/_content.html'
        footer: 'views/_footer.html'
    menu: [
        title: 'Home', href: '/'
    ,
        title: 'Design', href: '/design'
    ,
        title: 'Send', href: '/send'
    ]
)

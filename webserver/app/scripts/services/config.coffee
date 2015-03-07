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
        image: 'http://goo.gl/YHBZjc'
    features: [
        title: 'Design'
        body: 'Design letter templates and layouts'
        image: 'http://goo.gl/9M00hx'
    ,
        title: 'Send'
        body: 'Send letters'
        image: 'http://goo.gl/GpxBAx'
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

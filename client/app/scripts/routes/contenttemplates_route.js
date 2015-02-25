Ember.ContenttemplatesRoute = Ember.Route.extend({
  model: function() {
    return this.get('store').find('contenttemplate');
  }
});


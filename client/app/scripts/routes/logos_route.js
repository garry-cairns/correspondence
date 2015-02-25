Ember.LogosRoute = Ember.Route.extend({
  model: function() {
    return this.get('store').find('logo');
  }
});


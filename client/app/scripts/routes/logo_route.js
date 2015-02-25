Ember.LogoRoute = Ember.Route.extend({
  model: function(params) {
    return this.get('store').find('logo', params.logo_id);
  }
});


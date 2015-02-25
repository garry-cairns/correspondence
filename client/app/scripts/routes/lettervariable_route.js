Ember.LettervariableRoute = Ember.Route.extend({
  model: function(params) {
    return this.get('store').find('lettervariable', params.lettervariable_id);
  }
});


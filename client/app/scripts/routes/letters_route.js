Ember.LettersRoute = Ember.Route.extend({
  model: function() {
    return this.get('store').find('letter');
  }
});


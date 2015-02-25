Ember.LetterRoute = Ember.Route.extend({
  model: function(params) {
    return this.get('store').find('letter', params.letter_id);
  }
});


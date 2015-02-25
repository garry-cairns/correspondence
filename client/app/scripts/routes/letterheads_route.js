Ember.LetterheadsRoute = Ember.Route.extend({
  model: function() {
    return this.get('store').find('letterhead');
  }
});


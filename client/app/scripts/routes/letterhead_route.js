Ember.LetterheadRoute = Ember.Route.extend({
  model: function(params) {
    return this.get('store').find('letterhead', params.letterhead_id);
  }
});


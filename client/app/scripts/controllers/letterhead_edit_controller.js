Ember.LetterheadEditController = Ember.ObjectController.extend({
  needs: 'letterhead',
  actions: {
    save: function(){
      self = this
      this.get('buffer').forEach(function(attr){
        self.get('controllers.letterhead.model').set(attr.key, attr.value);
      });
      this.transitionToRoute('letterhead',this.get('model'));
    }
  }
});


Ember.LetterEditController = Ember.ObjectController.extend({
  needs: 'letter',
  actions: {
    save: function(){
      self = this
      this.get('buffer').forEach(function(attr){
        self.get('controllers.letter.model').set(attr.key, attr.value);
      });
      this.transitionToRoute('letter',this.get('model'));
    }
  }
});


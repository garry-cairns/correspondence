Ember.LettervariableEditController = Ember.ObjectController.extend({
  needs: 'lettervariable',
  actions: {
    save: function(){
      self = this
      this.get('buffer').forEach(function(attr){
        self.get('controllers.lettervariable.model').set(attr.key, attr.value);
      });
      this.transitionToRoute('lettervariable',this.get('model'));
    }
  }
});


Ember.LogoEditController = Ember.ObjectController.extend({
  needs: 'logo',
  actions: {
    save: function(){
      self = this
      this.get('buffer').forEach(function(attr){
        self.get('controllers.logo.model').set(attr.key, attr.value);
      });
      this.transitionToRoute('logo',this.get('model'));
    }
  }
});


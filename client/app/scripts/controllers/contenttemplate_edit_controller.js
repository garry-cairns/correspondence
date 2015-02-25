Ember.ContenttemplateEditController = Ember.ObjectController.extend({
  needs: 'contenttemplate',
  actions: {
    save: function(){
      self = this
      this.get('buffer').forEach(function(attr){
        self.get('controllers.contenttemplate.model').set(attr.key, attr.value);
      });
      this.transitionToRoute('contenttemplate',this.get('model'));
    }
  }
});


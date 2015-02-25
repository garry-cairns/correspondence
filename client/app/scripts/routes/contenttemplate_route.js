Ember.ContenttemplateRoute = Ember.Route.extend({
  model: function(params) {
    return this.get('store').find('contenttemplate', params.contenttemplate_id);
  }
});


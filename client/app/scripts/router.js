Ember.Router.map(function () {
  
  this.resource('contenttemplates', function(){
    this.resource('contenttemplate', { path: '/:contenttemplate_id' }, function(){
      this.route('edit');
    });
    this.route('create');
  });
  
  this.resource('letters', function(){
    this.resource('letter', { path: '/:letter_id' }, function(){
      this.route('edit');
    });
    this.route('create');
  });
  
  this.resource('letterheads', function(){
    this.resource('letterhead', { path: '/:letterhead_id' }, function(){
      this.route('edit');
    });
    this.route('create');
  });
  
  this.resource('lettervariables', function(){
    this.resource('lettervariable', { path: '/:lettervariable_id' }, function(){
      this.route('edit');
    });
    this.route('create');
  });
  
  this.resource('logos', function(){
    this.resource('logo', { path: '/:logo_id' }, function(){
      this.route('edit');
    });
    this.route('create');
  });
  
});

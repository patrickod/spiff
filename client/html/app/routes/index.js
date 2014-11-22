import Em from 'ember';

var IndexRoute = Em.Route.extend({
  beforeModel: function() {
    this.transitionTo('members');
  }
});

export default IndexRoute;

import Em from 'ember';

var MembersRoutes = Em.Route.extend({
  model: function() {
    return this.store.findAll('identity');
  },
});

export default MembersRoutes;

import Em from 'ember';

var MemberRoute = Em.Route.extend({
  model: function(params) {
    return this.store.find('identity', params.member_id);
  }
});

export default MemberRoute;

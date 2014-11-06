import Em from 'ember';

var MembersMeRoute = Em.Route.extend({
  model: function() {
    return this.store.find('identity', 'self');
  },
  renderTemplate: function() {
    this.render('members.member');
  }
});

export default MembersMeRoute;

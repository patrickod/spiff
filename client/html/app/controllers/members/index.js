import Em from 'ember';

var MembersIndexController = Em.ArrayController.extend({
  actions: {
    viewMember: function(member) {
      this.transitionTo('members.member', member);
    }
  }
});

export default MembersIndexController;

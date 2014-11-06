import DS from 'ember-data';

var Identity = DS.Model.extend({
  email: DS.attr(),
  username: DS.attr(),
  displayName: DS.attr(),
  isAnonymous: DS.attr(),
  lastSeen: DS.attr('date'),
  created: DS.attr('date')
});

export default Identity;

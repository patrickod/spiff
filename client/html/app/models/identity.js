import Em from 'ember';
import DS from 'ember-data';

var Identity = DS.Model.extend({
  email: DS.attr(),
  username: DS.attr(),
  displayName: DS.attr(),
  isAnonymous: DS.attr(),
  lastSeen: DS.attr('date'),
  created: DS.attr('date')
}).reopenClass({
  login: function(username, password) {
    return Em.$.ajax({
      method: 'POST',
      contentType: 'application/json',
      url: '/v1/identity/login/',
      dataType: 'json',
      data: JSON.stringify({
        username: username,
        password: password
      })
    });
  }
});

export default Identity;

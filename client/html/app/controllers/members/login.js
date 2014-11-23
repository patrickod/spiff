import Em from 'ember';
import Identity from 'spiff/models/identity';

var LoginController = Em.Controller.extend({
  actions: {
    login: function() {
      Identity.login(this.get('username'), this.get('password')).then(function(data) {
        console.log(JSON.stringify(data, undefined, 2));
      });
    }
  }
});

export default LoginController;

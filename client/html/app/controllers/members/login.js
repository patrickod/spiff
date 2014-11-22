import Em from 'ember';

var LoginController = Em.Controller.extend({
  actions: {
    login: function() {
      console.log('Username: ' + this.get('userName'));
    }
  }
});

export default LoginController;

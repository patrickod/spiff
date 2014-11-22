import Em from 'ember';

var LoginComponent = Em.Component.extend({
  actions: {
    login: function() {
      this.sendAction();
    }
  }
});

export default LoginComponent;

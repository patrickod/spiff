import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.resource('members', {path: '/members'}, function() {
    this.route('member', {path: '/:member_id'});
    this.route('login');
    this.route('logout');
    this.route('me');
  });
});

export default Router;

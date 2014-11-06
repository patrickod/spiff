import DjangoTastypieAdapter from 'spiff/vendor/ember-data-tastypie-adapter/adapter';

var ApplicationAdapter = DjangoTastypieAdapter.extend({
  host: 'http://localhost:8000',
  namespace: 'v1'
});

export default ApplicationAdapter;

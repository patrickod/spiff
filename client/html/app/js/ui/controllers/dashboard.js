angular.module('spiff.dashboard', [
  'restangular',
  'spiff'
])

.controller('DashboardRegistrationCtrl', function(Spiff, $location) {
  Spiff.getCurrentUser().then(function(user) {
    if (user && !user.isAnonymous) {
      $location.url('/members/'+user.id);
    }
  });
})

.controller('RegistrationCtrl', function($scope, SpiffRestangular, Spiff, $modal) {

  $scope.d = {};
  $scope.d.fields = [];
  $scope.requiredFields = [];
  $scope.optionalFields = [];
  SpiffRestangular.all('field').getList().then(function (fields) {
    _.each(fields, function(field) {
      if (field.required) {
        $scope.requiredFields.push(field);
      } else if (field.public && !field.protected){
        $scope.optionalFields.push(field);
      }
    });
  });

  $scope.submit = function() {
    var fields = [];
    _.each($scope.requiredFields, function(field) {
      fields.push({id: field.id, value: field.value});
    })
    _.each($scope.optionalFields, function(field) {
      fields.push({id: field.id, value: field.value});
    })

    SpiffRestangular.all('member').post({
      username: $scope.d.username,
      password: $scope.d.password,
      email: $scope.d.email,
      firstName: $scope.d.first_name,
      lastName: $scope.d.last_name,
      fields: fields
    }).then(function (u) {
      Spiff.login($scope.d.username, $scope.d.password);
    });
  }
})


.controller('UnsubscribeCtrl', function($scope, $modalInstance, SpiffRestangular, subscription) {
  $scope.subscription = subscription;
  $scope.close = $modalInstance.close;
  $scope.unsubscribe = function() {
    SpiffRestangular.one('subscription', subscription.id).remove().then(function () {
      $modalInstance.close();
    });
  }
})

.controller('AddPaymentCardCtrl', function($scope, $modalInstance, user) {
  $scope.d = {};
  $scope.save = function() {
    $scope.saving = true;
    var card = $scope.d.card_num;
    var cvc = $scope.d.cvc;
    var month = $scope.d.month;
    var year = $scope.d.year;
    user.addStripeCard({
      card: card,
      cvc: cvc,
      exp_month: month,
      exp_year: year
    }).then(function(cardData) {
      $modalInstance.close();
    });
  };

  $scope.cancel = function() {$modalInstance.close()};
})

.controller('DashboardCtrl', function(SpiffRestangular, $location, Spiff, $modal) {
  Spiff.getCurrentUser().then(function(user) {
    if (user && !user.isAnonymous) {
      $location.url('/members/'+user.id);
    } else if (!user || (user && user.isAnonymous)) {
      console.log(user);
      $location.url('/welcome');
    }
  });
})

.controller('AnonDashCtrl', function($scope, $rootScope, $scope, Spiff, SpaceAPI, $location, $sce) {
  $scope.showLogin = function() {
    $rootScope.$broadcast('showLogin');
  }

  SpaceAPI.ready(function(api) {
    $scope.spaceAPI = api.data;
    $scope.trustedMOTD = function() {
      return $sce.trustAsHtml(api.data.motd);
    }
  });

  Spiff.getCurrentUser().then(function(user) {
    if (user && !user.isAnonymous) {
      console.log(user);
      $location.url('/');
    }
  });
});

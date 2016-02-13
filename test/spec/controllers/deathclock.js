'use strict';

describe('Controller: DeathclockCtrl', function () {

  // load the controller's module
  beforeEach(module('nanorenoApp'));

  var DeathclockCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    DeathclockCtrl = $controller('DeathclockCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(DeathclockCtrl.awesomeThings.length).toBe(3);
  });
});

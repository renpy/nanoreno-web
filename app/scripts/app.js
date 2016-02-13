'use strict';

/**
 * @ngdoc overview
 * @name nanorenoApp
 * @description # nanorenoApp
 *
 * Main module of the application.
 */
angular.module(
		'nanorenoApp',
		[ 'ngAnimate', 'ngCookies', 'ngResource', 'ngRoute', 'ngSanitize',
				'ngTouch' ]).config(
		function($routeProvider, $locationProvider) {

			$locationProvider.html5Mode(true);

			$routeProvider.when('/', {
				templateUrl : 'views/main.html',
				controller : 'MainCtrl',
				controllerAs : 'main'
			}).when('/about', {
				templateUrl : 'views/about.html',
				controller : 'AboutCtrl',
				controllerAs : 'about'
			}).otherwise({
				redirectTo : '/'
			});
		});

'use strict';

/**
 * @ngdoc function
 * @name nanorenoApp.controller:DeathClock
 * @description
 * # DeathClock
 * Controller of the nanorenoApp
 */
angular.module('nanorenoApp').controller('DeathClock', function ($scope, $interval) {

	function update() {
		var now = new Date();

		var year = now.getFullYear();
		var month = now.getMonth();

		// Zero-centered months mean 3 is April.
		if (month >= 3) {
			year += 1;
		}

		var start = new Date(year, 2, 1, 0, 0, 0);
		var end = new Date(year, 3, 1, 0, 0, 0);

		start = +start;
		end = +end;
		now = +now;

		function format(n, divide, modulo, pad) {
			n = n / divide;
			n = n % modulo;
			n = Math.floor(n);
			if (pad) {
				if (n<10) {
					n = '0' + n;
				}
			}

			return n;
		}

		$scope.year = year

		$scope.now = now
		$scope.start = start;
		$scope.end = end;

		$scope.startDays = format(start - now, 86400000, 366, false);
		$scope.startHours = format(start - now, 3600000, 24, false);
		$scope.startMinutes = format(start - now, 60000, 60, true);
		$scope.startSeconds = format(start - now, 1000, 60, true);

		$scope.endDays = format(end - now, 86400000, 366, false);
		$scope.endHours = format(end - now, 3600000, 24, false);
		$scope.endMinutes = format(end - now, 60000, 60, true);
		$scope.endSeconds = format(end - now, 1000, 60, true);

	}

	update();

	$interval(update, 1000);
});

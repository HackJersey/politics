/* Not supposed to use jQuery in a controller, but we've only
   got four minutes to save the world
*/

function MainCtrl($scope) {

    $scope.years = [];
    $scope.year  = null;

    $scope.districts = [];
    $scope.district  = null;

    $scope.seats = [];
    $scope.seat  = null;

    $scope.showRaces = false;
    $scope.races     = [{id: 0, name: 'Race #1'}];
    $scope.race      = $scope.races[0];

    $scope.showCandidates = false;
    $scope.candidates     = [{id: 0, name: 'Mitt Romney'}];
    $scope.candidate      = $scope.candidates[0];

    $scope.showData  = false;

    $scope.init = function() {
        $scope.title = 'Campaign Contribution by Industry';
        $scope.help  = 'Pick a Year';

        $scope.get('/years', function(years) {
          for(var i in years)
                $scope.years.push(years[i]);
          $scope.year = $scope.years[0];

        });
    }

    $scope.loadDistricts = function() {
        $scope.get('/years/' + $scope.year, function(districts) {
          for(var i in districts)
                $scope.districts.push(districts[i]);

          $scope.district = $scope.districts[0];
        });
    }

    $scope.loadSeats = function() {
        $scope.get('/years/' + $scope.year + '/' + $scope.district, function(seats) {
          for(var i in seats)
                $scope.seats.push(seats[i]);

          $scope.seat = $scope.seats[0];
        });
    }

    $scope.get = function(uri, func) {
        $.ajax({
            type: 'GET',
            url: uri,
            dataType: 'json',
            success: func,
            data: {},
            async: false
        });
    }

    $scope.init();
};
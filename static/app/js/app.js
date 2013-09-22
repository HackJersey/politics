var hackjersey = angular.module('hackjersey', ['highcharts-ng']);

/* Written w/ angular.js
 *
 * @broadstreetads
*/
hackjersey.controller('MainCtrl', function($scope, $http) {

    $scope.candidates = [];
    $scope.candidate  = $scope.candidates[0];

    $scope.charts = []; // Will hold data for charts

    $scope.districts = [];
    $scope.district  = null;

    $scope.seats = [];
    $scope.seat  = null;
    
    $scope.years = [];
    $scope.year  = null;

    $scope.showData  = true;

    /**
     * Initialize the data and kick off the population of the menus
     */
    $scope.init = function() {
        $scope.title = 'Campaign Contribution by Industry';
        $scope.help  = 'Pick a Year';
        $scope.loadItems('/years', 'years', function() {
            $scope.year  = $scope.years[0];
            $scope.loadDistricts();
        });
    }

    /**
     * Load districts
     */
    $scope.loadDistricts = function() {
        $scope.loadItems('/years/' + $scope.year, 'districts', function() {
            $scope.district = $scope.districts[0];
            $scope.loadSeats();
        });
    }

    /**
     * Load seats
     */
    $scope.loadSeats = function() {
        $scope.loadItems('/years/' + $scope.year + '/' + $scope.district, 'seats', function() {
            $scope.seat = $scope.seats[0];
            $scope.loadCandidates();
        });
    }

    /**
     * Load candidates
     */
    $scope.loadCandidates = function() {
        $scope.loadItems('/years/' + $scope.year + '/' + $scope.district + '/' + $scope.seat, 'candidates', function() {
            //$scope.drawCharts();
        });
    }

    /**
     * Draw the charts for the loaded data/candidates
     */
    $scope.drawCharts = function() {
        $scope.charts.length = 0;

        for(var i in $scope.candidates) {

            var config = null;
            if($scope.candidates[i].top_contribs.length) {
                var industries = [];
                var amounts    = [];

                /* Load industries data */
                for(var c in $scope.candidates[i].top_contribs) 
                    industries.push($scope.candidates[i].top_contribs[c].name);

                /* Load amounts data */
                for(var c in $scope.candidates[i].top_contribs) 
                    amounts.push($scope.candidates[i].top_contribs[c].amount);

                config = {
                    chart: {
                        type: 'bar'
                    },
                    series: [{
                        data: amounts
                    }],
                    title: {
                        text: 'Industry Contributions for ' + $scope.candidates[i].name
                    },
                    xAxis: {
                        categories: industries,
                        title: {
                            text: 'Industry Name'
                        }
                    },
                    loading: false
                };
            }

            $scope.charts.push({
                candidateId: i,
                candidateName: $scope.candidates[i].name,
                config: config
            })
        }

    }

    /**
     * If you know the year in advance, district and seat, load it
     *  up and display it. This doesn't do any error checking if
     *  you call some non-existent combo.
     */
    $scope.goToSeat = function(year, district, seat) {
        $scope.year     = year;
        $scope.district = district;
        $scope.seat     = seat;
        $scope.loadCandidates();
    }

    /**
     * Generic method for calling a URI which returns a json array, and placing it
     * into an array by the given name on the scope
     */
    $scope.loadItems = function(uri, name, cb) {
        $scope[name].length = 0;
        $scope.get(uri, function(items) {
          for(var i in items)
                $scope[name].push(items[i]);
          if(cb) cb();
        });
    }

    /**
     * @TODO: Move this into an angular service
     */
    $scope.get = function(uri, func) {
        $http.get(uri)
            .success(func)
            .error(function() {
                alert('There was a server error loading the data');
            });
    }

    /* Go */
    $scope.init();
});
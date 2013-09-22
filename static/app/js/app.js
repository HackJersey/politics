/* Not supposed to use jQuery in a controller, but we've only
 * got four minutes to save the world
 *
 * @broadstreetads
*/
function MainCtrl($scope) {

    $scope.years = [];
    $scope.year  = null;

    $scope.districts = [];
    $scope.district  = null;

    $scope.seats = [];
    $scope.seat  = null;

    $scope.candidates     = [];
    $scope.candidate      = $scope.candidates[0];

    $scope.showData  = true;

    /**
     * Initialize the data and kick off the population of the menus
     */
    $scope.init = function() {
        $scope.title = 'Campaign Contribution by Industry';
        $scope.help  = 'Pick a Year';
        $scope.loadItems('/years', 'years');
        $scope.year  = $scope.years[0];
        $scope.loadDistricts();
    }

    /**
     * Load districts
     */
    $scope.loadDistricts = function() {
        $scope.loadItems('/years/' + $scope.year, 'districts');
        $scope.district = $scope.districts[0];
        $scope.loadSeats();
    }

    /**
     * Load seats
     */
    $scope.loadSeats = function() {
        $scope.loadItems('/years/' + $scope.year + '/' + $scope.district, 'seats');
        $scope.seat = $scope.seats[0];
        $scope.loadCandidates();
    }

    /**
     * Load candidates
     */
    $scope.loadCandidates = function() {
        $scope.loadItems('/years/' + $scope.year + '/' + $scope.district + '/' + $scope.seat, 'candidates');
    }

    /**
     * Generic method for calling a URI which returns a json array, and placing it
     * into an array by the given name on the scope
     */
    $scope.loadItems = function(uri, name) {
        $scope[name].length = 0;
        $scope.get(uri, function(items) {
          for(var i in items)
                $scope[name].push(items[i]);
        });
    }

    /**
     * @TODO: Move this into an angular service
     */
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

    /* Go */
    $scope.init();
};
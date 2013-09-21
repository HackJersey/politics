
function MainCtrl($scope) {

    $scope.main = {};

    $scope.main.years = [2013, 2012, 2011, 2010];
    $scope.main.year  = $scope.main.years[0];


    $scope.main.showRaces = false;
    $scope.main.races     = [{id: 0, name: 'Race #1'}];
    $scope.main.race      = $scope.main.races[0];

    $scope.main.showCandidates = false;
    $scope.main.candidates     = [{id: 0, name: 'Mitt Romney'}];
    $scope.main.candidate      = $scope.main.candidates[0];

    $scope.showData = false;

    $scope.init = function() {
        $scope.main.title = 'Campaign Contribution by Industry';
        $scope.main.help = 'Pick a Year';
    }

    $scope.init();
};
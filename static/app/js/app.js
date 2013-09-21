
function MainCtrl($scope) {

    $scope.main = {};

    $scope.main.years = [2013, 2012, 2011, 2010];
    $scope.main.year  = $scope.main.years[0];


    $scope.init = function() {
        $scope.main.title = 'Campaign Contribution by Industry';
        $scope.main.help = 'Pick a Year';
    }

    $scope.init();
};
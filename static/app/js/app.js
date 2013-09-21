
function MainCtrl($scope) {

    $scope.main = {};


    $scope.init = function() {
        $scope.main.title = 'Campaign Contribution by Industry';
        $scope.main.help = 'Pick a Year';
    }

    $scope.init();
};
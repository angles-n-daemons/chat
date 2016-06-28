var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() {
  socket.emit('test', {data: 'I\'m connected!'});
});

var app = angular.module('dillsapp', []);
app.controller("dillsappApplication", function($scope) {
    $scope.username = Cookies.get('username');
    $scope.userId = Cookies.get('user_id');

    if ($scope.userId === 'undefined' || $scope.username === 'undefined' || !$scope.userId || !$scope.username) {
        location = '/';
    }

    $scope.roomsById = {};
    $scope.rooms = [];

    socket.on('new_message', function(data) {
        var room = $scope.roomsById[data['roomId']];
        if (room) {
            room.messages.push(data);
            $scope.$apply();
        }
    });
});
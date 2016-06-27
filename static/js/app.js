var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() {
  socket.emit('test', {data: 'I\'m connected!'});
});

var app = angular.module('dillsapp', []);
app.controller("dillsappApplication", function($scope) {
    $scope.username = Cookies.get('username');
    $scope.userId = Cookies.get('user_id');

    $scope.roomsById = {};
    $scope.rooms = [];


    $scope.loadRooms = function() {
        var offset = $scope.rooms.length;
        $.ajax({
            url: 'api/room/list/' + offset,
            type: 'GET',
        }).success(function(res){
        }).fail(function(err) {
        });
    };
});
'use strict';

angular.module("dillsapp").directive("dillsappRoomDisplay", ['$rootScope', function($rootScope) {
  return {
    restrict: 'EA',
    scope: true,
    replace: true,
    templateUrl: 'static/js/directives/room-display/room-display.html',
    link: function(scope, directiveElement, attrs) {
      scope.newRoomName = '';
      scope.newRoomError = '';

      scope.init = function() {
        scope.initPopup();
        scope.populateList();
      };

      scope.initPopup = function() {
        $('#room-form').popup({
          'horizontal': 'center',
          'vertical': 'center',
          'transition': 'all 0.3s',
          'scrolllock': true,
          'type': 'overlay',
          'escape': true,
          'openelement': '#create-room-btn',
          'closeelement': '#close-btn'
        });
      };

      scope.populateList = function() {
        $.ajax({
          url: '/api/room/list',
          type: 'GET',
          dataType: 'json',
          success: function(res) {
            for (var i in res.rooms) {
              scope.addRoom(res.rooms[i]);
            }
            scope.$apply();
          },
          error: function(err) {
            console.log(err);
          }
        });
      };

      scope.createRoom = function() {
        var newRoomName = $('#room-form input').val();
        if (!newRoomName) {
          return scope.setNewRoomError('Cannot create room without name');
        }

        socket.emit('create_room', {'name': newRoomName});
        scope.setNewRoomError('');
        $('#room-form').popup('hide');
      };

      scope.addRoom = function(roomRow) {
        var room = new Room(roomRow);
        scope.rooms.unshift(room);
        scope.roomsById[room.id] = room;
      };

      scope.setNewRoomError = function(err) {
        if (!scope.newRoomName) {
          $('.room-error').text(err);
        }
      };

      scope.joinRoom = function(room) {
        $rootScope.$broadcast('join_room', room);
      };
      
      // socket calls

      socket.on('new_room', function(data) {
        scope.addRoom(data);
        scope.$apply();
      });

      scope.init(); 
    }
  };
}]);
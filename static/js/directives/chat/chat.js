'use strict';

angular.module("dillsapp").directive("dillsappChat", function() {
  return {
    restrict: 'EA',
    scope: true,
    replace: true,
    templateUrl: 'static/js/directives/chat/chat.html',
    link: function(scope, directiveElement, attrs) {

      scope.currentRoom = null;
      scope.userMessage = '';
      
      scope.$on('join_room', function(event, room) {
        scope.currentRoom = room;
        if (!room.joined) {
          room.loadMessages(function() {
            scope.$apply();
          });
        }
        socket.emit('join', {'room': room.id});
      });

      scope.sendMessage = function() {
        if (!scope.currentRoom || !scope.userMessage) {
          return;
        }
        var data = {
          'roomId': scope.currentRoom.id,
          'userId': scope.userId,
          'login': scope.username,
          'content': scope.userMessage
        }
        socket.emit('send_message', data);
        scope.userMessage = '';
        scope.$apply();
      };

      $('.message-input input')[0].onkeypress =  function(e){
        if (!e) e = window.event;
        var keyCode = e.keyCode || e.which;
        if (keyCode == '13'){
          scope.sendMessage();
        }
      }
    }
  };
});
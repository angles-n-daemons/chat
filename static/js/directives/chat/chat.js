'use strict';

angular.module("dillsapp").directive("dillsappChat", function() {
  return {
    restrict: 'EA',
    scope: true,
    replace: true,
    templateUrl: 'static/js/directives/chat/chat.html',
    link: function(scope, directiveElement, attrs) {

      scope.openRooms = [];
      scope.$on('join_room', function(event, room) {
        scope.openRooms.unshift(room);
      });
    }
  };
});
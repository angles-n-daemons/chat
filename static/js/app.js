var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() {
	console.log('emitting');
  socket.emit('test', {data: 'I\'m connected!'});
});
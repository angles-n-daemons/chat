'use strict';

function RoomContainer() {
    this.byId = {};
    this.rooms = [];
}

function Room(row) {
    this.id = row['roomId'];
    this.name = row['name'];
    this.isActive = false;
    this.messages = [];
}

Room.prototype.loadMessages = function() {
    var me = this;
    if (!me.id) {
        throw 'Cannot load for room without id.';
    }

    var args = {
        'rid': me.id,
        'offset': me.offset
    };

    $.ajax({
        url: '/api/message/list/',
        type: 'GET',
        data: args,
        dataType: 'json',
        contentType: 'application/json'
    }).success(function(res) {
        var messages = res.messages;
        me.offset = me.offset + messages.length;
        me.messages = me.messages.concat(messages);
    }).fail(function(err) {
        console.log(err);
    });
};

function Message(roomId) {

};

Message.prototype.post = function() {

};

function User(login) {
    this.isMe = false;
};
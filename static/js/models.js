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

Room.prototype.loadMessages = function(cb) {
    var me = this;
    if (!me.id) {
        throw 'Cannot load for room without id.';
    }
    var args = {
        'roomId': me.id,
        'offset': me.offset
    };

    $.ajax({
        url: '/api/message/list/' + me.id,
        type: 'GET',
        dataType: 'json',
        contentType: 'application/json'
    }).success(function(res) {
        var messages = res.messages;
        me.offset = me.offset + messages.length;
        me.messages = me.messages.concat(messages);

        if (cb) {
            cb();
        }
    }).fail(function(err) {
        console.log(err);
    });
};
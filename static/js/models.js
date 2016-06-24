


function Room(id, name) {
    this.id = id;
    this.name = name;
    this.messages = [];
    this.offset = 0;
};

Room.prototype.loadMessages() {

};

function Message(roomId) {

};

function User(login) {
    this.isMe = false;
};
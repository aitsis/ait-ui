this.genRandomNumbers = () => {
    const array = new Uint32Array(10);
    crypto.getRandomValues(array);
    return Array.from(array).map(n => n.toString(16)).join('');
};

let elements = {};
let event_handlers = {};
const socket = io.connect(`${window.location.origin}`, { // read only
    query: { cookie: document.cookie }
});

socket.on('disconnect', function () {
    console.log('Server disconnected');
    location.reload(true);
});

socket.on('from_server', function (data) {
    if (data.event_name == "init-content") {
        let el = document.getElementById(data.id);
        el.outerHTML = data.value;
        return;
    }
    if (data.event_name == "toggle-class") {
        let el = document.getElementById(data.id);
        el.classList.toggle(data.value);
        return;
    }
    if (data.event_name.startsWith("change-")) {
        if (data.event_name.split("-")[1] == "location") {
            window.location = data.value;
            return;
        }
        var el = document.getElementById(data.id);
        el[data.event_name.split("-")[1]] = data.value;
        return;
    }
    if (data.event_name.startsWith("set-")) {
        var el = document.getElementById(data.id);
        el['style'][data.event_name.split("-")[1]] = data.value;
        return;
    }
    if (data.event_name in event_handlers) {
        event_handlers[data.event_name](data.id, data.value, data.event_name);
    }
    else {
        console.log("no handler for", data.event_name);
    }
});

function clientEmit(id, newValue, event_name) {
    console.log("clientEmit", id, newValue, event_name);
    if (newValue instanceof File) {
        var formData = new FormData();
        formData.append("file", newValue);
        formData.append("id", id);
        uid = genRandomNumbers();
        formData.append("uid", uid);
        console.log("formData", formData);
        var request = new XMLHttpRequest();
        request.open("POST", "/file-upload");
        request.send(formData);
        request.onreadystatechange = function () {
            if (request.readyState == XMLHttpRequest.DONE) {
                console.log("post done.");
            }
        }
        socket.emit('from_client', { id: id, value: { uid: uid, file_name: newValue.name }, event_name: 'file-upload-started' });
        return;
    }
    socket.emit('from_client', { id: id, value: newValue, event_name: event_name });
}

window.onload = function () {
    clientEmit("myapp", "init", "init");
}
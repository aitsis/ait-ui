this.genRandomNumbers = () => {
    const array = new Uint32Array(10);
    crypto.getRandomValues(array);
    return Array.from(array).map(n => n.toString(16)).join('');
};

let elements = {};
let event_handlers = {};
const socket = io.connect(`${window.location.origin}`, {
    query: { cookie: document.cookie }
});

socket.on('connect', function () {
    console.log('Server connected');
});

socket.on('afterconnect', function(data) {
    console.log(data.message); // "Connection initialized"
    clientEmit("myapp", "init", "init");
});

socket.on('disconnect', function () {
    console.log('Server disconnected');
    location.reload(true);
});

socket.on('from_server', function (data) {
    try {
        if (data.event_name === "set-cookie") {
            let cookieString = `${data.value.name}=${data.value.value};`;
            const cookieAttributes = ['maxAge', 'path', 'httponly', 'secure', 'samesite'];

            cookieAttributes.forEach(attr => {
                if (data.value[attr]) {
                    cookieString += attr === 'maxAge' ? `max-age=${data.value[attr]};` : `${attr}=${data.value[attr]};`;
                }
            });

            document.cookie = cookieString;
            return
        }
    } catch (error) {
        console.log(error);
    }

    if (data.event_name === "delete-cookie") {
        document.cookie = `${data.value.name}=; max-age=0`;
        return;
    }
    if (data.event_name === "navigate") {
        window.location = data.value;
        return;
    }

    if (data.event_name === "alert") {
        alert(data.value);
        return;
    }

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
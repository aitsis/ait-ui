this.genRandomNumbers = () => {
    const array = new Uint32Array(10);
    crypto.getRandomValues(array);
    return Array.from(array).map(n => n.toString(16)).join('');
};

const clientPublicData = {
    locale: navigator.language || navigator.userLanguage,
    userAgent: navigator.userAgent,
  };  

let elements = {};
let event_handlers = {};
const socket = io.connect(`${window.location.origin}`, {
    query: { 
        cookie: document.cookie,
        clientPublicData: JSON.stringify(clientPublicData)
    }
});

socket.on('connect', function () {
    clientEmit("myapp", "init", "init");
});

socket.on('disconnect', function () {
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

    if (data.event_name === "scroll-to") {
        const el = document.getElementById(data.id);
        el.scrollIntoView({ behavior: "smooth", block: "center", inline: "nearest" });
        return;
    }

    if (data.event_name === "alert") {
        alert(data.value);
        return;
    }

    if (data.event_name === "focus") {
        let el = document.getElementById(data.id);
        el.focus();
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
    if (data.event_name == "add-class") {
        let el = document.getElementById(data.id);
        el.classList.add(data.value);
        return;
    }
    if (data.event_name == "remove-class") {
        let el = document.getElementById(data.id);
        el.classList.remove(data.value);
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
});

async function clientEmit(id, newValue, event_name) {
    if (newValue instanceof File) {
        if (newValue.size > 100 * 1024 * 1024) {
            alert("File size exceeds the limit.");
            return;
        }
        return await uploadFile(newValue, id);
    }
    socket.emit('from_client', { id: id, value: newValue, event_name: event_name });
}

async function uploadFile(newValue, id) {
  const uid = genRandomNumbers();
  const formData = new FormData();
  formData.append("file", newValue);
  formData.append("id", id);
  formData.append("uid", uid);

  // FOR PYTHON USAGE MAKE CALL TO /file-upload
  //url to call = /file-upload

  return fetch("/api/images/", {
      method: "POST",
      body: formData,
      credentials: "include",
  })
  .then((response) => {
      if (!response.ok) {
          throw new Error("File upload failed");
      }
      return response.json();
  })
  .then((data) => {
      socket.emit('from_client', { id: id, value: { uid: uid, file_name: newValue.name, data }, event_name: 'file-upload-started' });
  })
  .catch((error) => {
      console.error("Error:", error);
      alert(error.message);
  });
}
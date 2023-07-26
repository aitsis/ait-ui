event_handlers["init-dropzone"] = function (id, value, event_name) {
    elements[id] = new Dropzone("#" + id, { url: "/file/post" });
    console.log("init-dropzone");
}

event_handlers["dropzone"] = function (id, value, event_name) {
    console.log("dropzone", id, value);
    elements[id][value.action](value.value);
}
event_handlers["init-dropzone"] = function (id, value, event_name) {
    elements[id] = new Dropzone("#" + id, { url: "/file/post" });
}

event_handlers["dropzone"] = function (id, value, event_name) {
    elements[id][value.action](value.value);
}
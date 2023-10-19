event_handlers["init-canvas"] = function (id, value, event_name) {
    canvas = document.getElementById(id);
    elements[id] = { canvas: canvas, ctx: canvas.getContext('2d') };
}

event_handlers["canvas"] = function (id, value, event_name) {
    if (value.action == "fillRect") {
        elements[id].ctx.fillStyle = value.params.color;
        elements[id].ctx.fillRect(value.params.x, value.params.y, value.params.width, value.params.height);
    }
    if (value.action == "fillCircle") {
        elements[id].ctx.beginPath();
        elements[id].ctx.arc(value.params.x, value.params.y, value.params.radius, 0, 2 * Math.PI);
        elements[id].ctx.fillStyle = value.params.color;
        elements[id].ctx.fill();
    }
}
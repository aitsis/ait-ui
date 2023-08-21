event_handlers["init-seadragon"] = function (id, value, event_name) {
    // create viewer
    elements[id] = {
        mouse_mode: "pan",
        pointer_element: null,
        brush_size: 10,
        canvas: null,
        viewer: OpenSeadragon({
            id: id,
            prefixUrl: "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/images/",
            animationTime: 0,
            maxZoomPixelRatio: 4,
            gestureSettingsMouse: {
                scrollToZoom: false,
                clickToZoom: false,
                dragToPan: false
            }
        })
    }

    function on_mouse_move(mousePosition) {
        var viewerOffset = elements[id].viewer.canvas.getBoundingClientRect();
        if (elements[id].mouse_mode == "draw-mode") {
            event.preventDefaultAction = true;
            if (elements[id].pointer_element != null) {
                zoom = elements[id].viewer.viewport.getZoom();
                // Adjust the mousePosition coordinates by subtracting the viewer offset
                var adjustedX = mousePosition.x - viewerOffset.left - elements[id].brush_size * zoom / 2;
                var adjustedY = mousePosition.y - viewerOffset.top - elements[id].brush_size * zoom / 2;
                //move element
                elements[id].pointer_element.style.left = adjustedX + "px";
                elements[id].pointer_element.style.top = adjustedY + "px";
            }
        }
    }

    function draw_to_canvas(mousePosition) {
        let canvas = elements[id].canvas;
        var viewerOffset = elements[id].viewer.canvas.getBoundingClientRect();
        var zoom = elements[id].viewer.viewport.getZoom();
        // Adjust the mousePosition coordinates by subtracting the viewer offset
        adjustedX = mousePosition.x - viewerOffset.left;
        adjustedY = mousePosition.y - viewerOffset.top;
        // draw circle
        ctx = canvas.getContext("2d");
        ctx.fillStyle = "rgba(255, 0, 0, 0.5)";
        ctx.beginPath();
        ctx.arc(adjustedX, adjustedY, elements[id].brush_size / 2, 0, 2 * Math.PI);
        ctx.fill();
        // send canvas to server
        //socket_handler.send("canvas", {id: id, value: canvas.toDataURL()});
    }

    elements[id].viewer.addHandler('canvas-drag', function (event) {
        if (elements[id].mouse_mode == "draw-mode") {
            event.preventDefaultAction = true;
            var mousePosition = OpenSeadragon.getMousePosition(event.originalEvent);
            on_mouse_move(mousePosition);
            // get Image Coordinates                
            var viewportPoint = elements[id].viewer.viewport.pointFromPixel(mousePosition);
            var imagePoint = elements[id].viewer.viewport.viewportToImageCoordinates(viewportPoint);
            // draw to canvas
            draw_to_canvas(imagePoint);
        }
    });

    elements[id].viewer.canvas.addEventListener('mousemove', function (event) {
        var mousePosition = OpenSeadragon.getMousePosition(event);
        on_mouse_move(mousePosition);
    });

    // zoom handler
    elements[id].viewer.addHandler('zoom', function (event) {
        if (elements[id].mouse_mode == "draw-mode") {
            if (elements[id].pointer_element != null) {
                zoom = elements[id].viewer.viewport.getZoom();
                elements[id].pointer_element.style.width = elements[id].brush_size * zoom + "px";
                elements[id].pointer_element.style.height = elements[id].brush_size * zoom + "px";
            }
        }
    });

    var downloadButton = new OpenSeadragon.Button({
        tooltip: 'Download Image',
        onClick: downloadImage,
        srcRest: 'download_rest.png',
        srcGroup: 'download_grouphover.png',
        srcHover: 'download_hover.png',
        srcDown: 'download_down.png'
    });

    elements[id].viewer.buttonGroup.buttons.push(downloadButton);
    elements[id].viewer.buttonGroup.element.appendChild(downloadButton.element);

    function downloadImage() {
        var imageUri = elements[id].viewer.drawer.canvas.toDataURL("image/png");
        var link = document.createElement('a');
        link.href = imageUri;
        link.download = 'downloaded_image.png';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}

event_handlers["seadragon"] = function (id, command, event_name) {
    switch (command.action) {
        case "open":
            elements[id].viewer.open(command.value);
            break;
        case "brush-size":
            elements[id].brush_size = command.value;
            if (elements[id].pointer_element != null) {
                zoom = elements[id].viewer.viewport.getZoom();
                elements[id].pointer_element.style.width = elements[id].brush_size * zoom + "px";
                elements[id].pointer_element.style.height = elements[id].brush_size * zoom + "px";
            }
            break;
        case "set-scroll-zoom":
            elements[id].viewer.gestureSettingsMouse.scrollToZoom = command.value;
            elements[id].viewer.gestureSettingsMouse.clickToZoom = command.value;
            elements[id].viewer.gestureSettingsMouse.dragToPan = command.value;
            break;
        case "mouse-mode":
            elements[id].mouse_mode = command.value;
            console.log("mouse-mode: " + elements[id].mouse_mode)
            if (elements[id].mouse_mode == "draw-mode") {
                if (elements[id].pointer_element == null) {
                    elements[id].pointer_element = document.createElement("div");
                    elements[id].pointer_element.style.position = "absolute";
                    elements[id].pointer_element.style.width = elements[id].brush_size + "px";
                    elements[id].pointer_element.style.height = elements[id].brush_size + "px";
                    elements[id].pointer_element.style.borderRadius = "50%";
                    elements[id].pointer_element.style.backgroundColor = "rgba(255,0,0,0.5)";
                    elements[id].viewer.canvas.appendChild(elements[id].pointer_element);

                    if (elements[id].canvas != null) {
                        elements[id].viewer.removeOverlay(elements[id].canvas);
                        elements[id].canvas = null;
                    }

                    let tiledImage = elements[id].viewer.world.getItemAt(0); // Get the first image
                    let imageWidthInPixels = tiledImage.source.width;
                    let imageHeightInPixels = tiledImage.source.height;
                    console.log("imageWidthInPixels: " + imageWidthInPixels);
                    console.log("imageHeightInPixels: " + imageHeightInPixels);
                    elements[id].canvas = document.createElement("canvas");
                    elements[id].canvas.width = imageWidthInPixels;
                    elements[id].canvas.height = imageHeightInPixels;
                    elements[id].viewer.addOverlay({
                        element: elements[id].canvas,
                        location: new OpenSeadragon.Rect(0, 0, 1, 1)
                    });
                }
            } else {
                if (elements[id].pointer_element != null) {
                    elements[id].viewer.canvas.removeChild(elements[id].pointer_element);
                    elements[id].pointer_element = null;
                }
            }
            break;
        default:
            console.log("Unknown command: " + command.action);
    }
}
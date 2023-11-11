event_handlers["init-seadragon"] = function (id, value, event_name) {
    // create viewer
    let hasButtons = JSON.parse(value.hasButtons);
    let viewerConfig = {
        id: id,
        prefixUrl: "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.1.0/images/",
        animationTime: 0,
        maxZoomPixelRatio: 4,
        gestureSettingsMouse: {
            scrollToZoom: false,
            clickToZoom: false,
            dragToPan: false
        },
        showNavigationControl: hasButtons,
        zoomInButton: hasButtons ? undefined : null,
        zoomOutButton: hasButtons ? undefined : null,
        homeButton: hasButtons ? undefined : null,
        fullPageButton: hasButtons ? undefined : null
    };

    let viewer = OpenSeadragon(viewerConfig);
    elements[id] = {
        mouse_mode: "pan",
        pointer_element: null,
        brush_size: 10,
        canvas: null,
        viewer: viewer
    };

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

    if (hasButtons) {
        let buttons = elements[id].viewer.buttonGroup.buttons;
    
        var downloadButton = new OpenSeadragon.Button({
            tooltip: 'Download Image',
            onClick: downloadFullImage,
            srcRest: 'ivb_download.svg',
            srcGroup: 'ivb_download.svg',
            srcHover: 'ivb_download-hover.svg',
            srcDown: 'ivb_download-hover.svg',
        });

        var saveButton = new OpenSeadragon.Button({
            tooltip: 'Add to Favorites',
            onClick: saveFullImage,
            srcRest: 'ivb_save.svg',
            srcGroup: 'ivb_save.svg',
            srcHover: 'ivb_save-hover.svg',
            srcDown: 'ivb_save-hover.svg',
        });

      
        // var sendToRepeater = new OpenSeadragon.Button({
        //         tooltip: 'Send To Repeater',
        //         onClick: sendToRepeaterFunction,
        //         srcRest: 'send_to_repeater.svg',
        //         srcGroup: 'send_to_repeater.svg',
        //         srcHover: 'send_to_repeater-hover.svg',
        //         srcDown: 'send_to_repeater-hover.svg',
        //     });

        // var sendToUpscaler = new OpenSeadragon.Button({
        //     tooltip: 'Send To Upscaler',
        //     onClick: sendToUpscalerFunction,
        //     srcRest: 'send_to_upscaler.svg',
        //     srcGroup: 'send_to_upscaler.svg',
        //     srcHover: 'send_to_upscaler-hover.svg',
        //     srcDown: 'send_to_upscaler-hover.svg',
        // });

        var sendToInput= new OpenSeadragon.Button({
            tooltip: 'Send To Input',
            onClick:sendToInputFunction,
            srcRest: 'send_to_input.svg',
            srcGroup: 'send_to_input.svg',
            srcHover: 'send_to_input-hover.svg',
            srcDown: 'send_to_input-hover.svg',
        }); 

        elements[id].viewer.buttonGroup.buttons.push(downloadButton);
        elements[id].viewer.buttonGroup.element.appendChild(downloadButton.element);

        elements[id].viewer.buttonGroup.buttons.push(saveButton);
        elements[id].viewer.buttonGroup.element.appendChild(saveButton.element);

        // if (value.tool & value.tool == "imagine"){
        //   elements[id].viewer.buttonGroup.buttons.push(sendToRepeater);
        //   elements[id].viewer.buttonGroup.element.appendChild(sendToRepeater.element);

        //   elements[id].viewer.buttonGroup.buttons.push(sendToUpscaler);
        //   elements[id].viewer.buttonGroup.element.appendChild(sendToUpscaler.element);
        // }
        elements[id].viewer.buttonGroup.buttons.push(sendToInput);
        elements[id].viewer.buttonGroup.element.appendChild(sendToInput.element); 
        const updateButton = (button, filename, extension, width = '25px', height = '25px', padding = '5px', backgroundColor = 'var(--background-mask)', backgroundBlur = 'blur(5px)') => {
            ['imgRest', 'imgGroup'].forEach(imgType => {
                button[imgType].src = filename + '.' + extension;
                button[imgType].style.width = width;
                button[imgType].style.height = height;
                button[imgType].style.padding = padding;
                button[imgType].style.backgroundColor = backgroundColor;
                //button[imgType].style['backdrop-filter'] = backgroundBlur;
            });
            ['imgHover', 'imgDown'].forEach(imgType => {
                button[imgType].src = filename + '-hover.' + extension;
                button[imgType].style.width = width;
                button[imgType].style.height = height;
                button[imgType].style.padding = padding;
                button[imgType].style.backgroundColor = backgroundColor;
                //button[imgType].style['backdrop-filter'] = backgroundBlur;
            });
        };

        for (let button of buttons) {
            switch (button.tooltip) {
                case 'Zoom in':
                    updateButton(button, 'ivb_zoom-in', 'svg');
                    break;
                case 'Zoom out':
                    updateButton(button, 'ivb_zoom-out', 'svg');
                    break;
                case 'Go home':
                    updateButton(button, 'ivb_home', 'svg');
                    break;
                case 'Toggle full page':
                    updateButton(button, 'ivb_fullscreen', 'svg');
                    break;
                case 'Download Image':
                    updateButton(button, 'ivb_download', 'svg');
                    break;
                case 'Add to Favorites':
                    updateButton(button, 'ivb_save', 'svg');
                    break;
                case 'Send To Repeater':
                    updateButton(button, 'send_to_repeater', 'svg');
                    break;
                case 'Send To Upscaler':
                    updateButton(button, 'send_to_upscaler', 'svg');
                    break;
                case 'Send To Input':
                    updateButton(button, 'send_to_input', 'svg');
                    break;
            }
        }

        function downloadFullImage() {
            let viewer = elements[id].viewer;
            let tileSources = viewer.world.getItemAt(0).source;
            let imageUrl = tileSources.url || tileSources[0].url;

            if (!imageUrl) {
                console.error('Full image URL not found');
                return;
            }

            var link = document.createElement('a');
            link.href = imageUrl;
            const fileExtension = imageUrl.split('.').pop();
            link.download = `${genRandomNumbers()}.${fileExtension}`;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }

        function saveFullImage() {
            let viewer = elements[id].viewer;
            let tileSources = viewer.world.getItemAt(0).source;
            let imageUrl = tileSources.url || tileSources[0].url;
            if (!imageUrl) {
                console.error('Full image URL not found');
                return;
            }

            clientEmit(elements[id].viewer.element.id, "", 'savefile');
        }

        function sendToRepeaterFunction() {}

        function sendToUpscalerFunction() {}

        function sendToInputFunction() {
            let viewer = elements[id].viewer;
            let tileSources = viewer.world.getItemAt(0).source;
            let imageUrl = tileSources.url || tileSources[0].url;
        
            if (imageUrl == "AIT_AI_LOGO.png") {
                console.error('Full image URL not found');
                return;
            }
            clientEmit(elements[id].viewer.element.id, imageUrl, 'sendtoinput');
        }
    }
}

event_handlers["seadragon"] = function (id, command, event_name) {
    switch (command.action) {
        case "open":
            elements[id].viewer.open(command.value);
            break;
        case 'close':
            elements[id].viewer.close();
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
            const cmd = command.value === "true";
            elements[id].viewer.gestureSettingsMouse.scrollToZoom = cmd;
            elements[id].viewer.gestureSettingsMouse.clickToZoom = cmd;
            elements[id].viewer.gestureSettingsMouse.dragToPan = cmd;
            break;
        case "mouse-mode":
            elements[id].mouse_mode = command.value;
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
            break;
    }
}
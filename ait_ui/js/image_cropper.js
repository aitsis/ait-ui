event_handlers["init-image-cropper"] = function (id, value, event_name) {
  let canvas = new fabric.Canvas(id);

  let firstParent = document.getElementById(id).parentElement;
  let parentElement = firstParent.parentElement;

  canvas.setWidth(parentElement.offsetWidth);
  canvas.setHeight(parentElement.offsetHeight);

  elements[id] = {
    canvas: canvas,
    image: null,
  };
};

event_handlers["image-cropper"] = function (id, command, event_name) {
  console.log("image-cropper: " + JSON.stringify(command));
  switch (command.action) {
    case "loadImage":
      console.log("loadImage: " + command.value);
      fabric.Image.fromURL(command.value, function (img) {
        img.scaleToWidth(elements[id].canvas.getWidth());
        elements[id].canvas.add(img);
        elements[id].image = img;
      });
      break;
    case "cropAndMove":
      console.log("cropAndMove: " + JSON.stringify(command.value));
      let axis = command.value.axis;
      let scale = command.value.scale;
      console.log("axis: " + axis, "scale: " + scale);
      moveImage(axis, elements[id].canvas, elements[id].image, scale);
      break;
    default:
      console.log("Unknown command: " + command.action);
  }
};

function moveImage(axis, canvas, image, reportRate) {
  if (!image) return;

  canvas.clear();

  const originalWidth = image.width;
  const originalHeight = image.height;
  const rate = axis === 'x' ? originalWidth * reportRate : originalHeight * reportRate;

  const firstCanvas = document.createElement('canvas');
  const secondCanvas = document.createElement('canvas');
  const finalCanvas = document.createElement('canvas');
  finalCanvas.width = originalWidth;
  finalCanvas.height = originalHeight;

  const firstCtx = firstCanvas.getContext('2d');
  const secondCtx = secondCanvas.getContext('2d');
  const finalCtx = finalCanvas.getContext('2d');

  if (axis === 'x') {
    firstCanvas.width = secondCanvas.width = originalWidth;
    firstCanvas.height = secondCanvas.height = originalHeight / 2;

    firstCtx.drawImage(image._element, 0, 0, originalWidth, originalHeight / 2, 0, 0, originalWidth, originalHeight / 2);
    secondCtx.drawImage(image._element, 0, originalHeight / 2, rate, originalHeight / 2, originalWidth - rate, 0, rate, originalHeight / 2);
    secondCtx.drawImage(image._element, rate, originalHeight / 2, originalWidth - rate, originalHeight / 2, 0, 0, originalWidth - rate, originalHeight / 2);

    finalCtx.drawImage(firstCanvas, 0, 0);
    finalCtx.drawImage(secondCanvas, 0, originalHeight / 2);
  } else {
    firstCanvas.width = secondCanvas.width = originalWidth / 2;
    firstCanvas.height = secondCanvas.height = originalHeight;

    firstCtx.drawImage(image._element, 0, 0, originalWidth / 2, originalHeight, 0, 0, originalWidth / 2, originalHeight);
    secondCtx.drawImage(image._element, originalWidth / 2, 0, originalWidth / 2, rate, 0, originalHeight - rate, originalWidth / 2, rate);
    secondCtx.drawImage(image._element, originalWidth / 2, rate, originalWidth / 2, originalHeight - rate, 0, 0, originalWidth / 2, originalHeight - rate);

    finalCtx.drawImage(firstCanvas, 0, 0);
    finalCtx.drawImage(secondCanvas, originalWidth / 2, 0); // Corrected to secondCanvas
  }

  const expandedImage = new fabric.Image(finalCanvas, {
    left: image.left,
    top: image.top,
    scaleX: image.scaleX,
    scaleY: image.scaleY,
  });

  canvas.remove(image);
  canvas.add(expandedImage);
  canvas.requestRenderAll();
}
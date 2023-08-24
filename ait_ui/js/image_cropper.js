let ORIGINAL_SCALE = 0.3;
let currentScale = ORIGINAL_SCALE;

const MIN_SCALE = 0.15;
const MAX_SCALE = 5;

fabric.Object.prototype.hoverCursor = 'default';

event_handlers["init-image-cropper"] = function (id, value, event_name) {
  document.getElementById('resetButton').addEventListener('click', function () {
    resetImage('yourCanvasId');
  });

  let canvas = new fabric.Canvas(id);

  let firstParent = document.getElementById(id).parentElement;
  let parentElement = firstParent.parentElement;

  canvas.setWidth(parentElement.offsetWidth);
  canvas.setHeight(parentElement.offsetHeight);

  elements[id] = {
    canvas: canvas,
    image: null,
    patternGroup: null,
    lastModified: { x: null, y: null },
    latestCombinedImage: null,
  };

  if (repeater_checkbox) {
    repeater_checkbox.addEventListener('change', function () {
      if (this.checked) {
        console.log(currentScale, "checked");
        const imageToUse = elements[id].latestCombinedImage || elements[id].image;
        elements[id].patternGroup = updateImagePattern(canvas, imageToUse, currentScale, id);
        canvas.remove(elements[id].image);
      } else {
        const imageToUse = elements[id].latestCombinedImage || elements[id].image;
        canvas.getObjects().forEach(function (obj) {
          if (obj.patternGroup) {
            canvas.remove(obj);
          }
        });
        canvas.add(imageToUse);
        canvas.requestRenderAll();
      }
    });
  }

  for (const id in elements) {
    const canvas = elements[id].canvas;

    canvas.on('mouse:wheel', function (opt) {
      var delta = opt.e.deltaY;
      var proposedScale = currentScale;
      if (proposedScale >= MIN_SCALE && proposedScale <= MAX_SCALE) {
        currentScale = proposedScale;

        if (repeater_checkbox && repeater_checkbox.checked) {
          var zoom = canvas.getZoom();
          zoom *= 0.999 ** delta;
          if (zoom > MAX_SCALE) zoom = MAX_SCALE;
          if (zoom < MIN_SCALE) zoom = MIN_SCALE;

          var center = canvas.getCenter();
          canvas.zoomToPoint({ x: center.left, y: center.top }, zoom);
          console.log(currentScale, "checked");
          updateImagePattern(canvas, elements[id].image, currentScale, id);
          return;
        }
        var zoom = canvas.getZoom();
        zoom *= 0.999 ** delta;
        if (zoom > MAX_SCALE) zoom = MAX_SCALE;
        if (zoom < MIN_SCALE) zoom = MIN_SCALE;

        var center = canvas.getCenter();
        canvas.zoomToPoint({ x: center.left, y: center.top }, zoom);
      }

      opt.e.preventDefault();
      opt.e.stopPropagation();
    });
  }
};

function resetImage(id) {
  const canvas = elements[id].canvas;
  const originalImage = elements[id].image;

  elements[id].lastModified = { x: null, y: null };
  elements[id].latestCombinedImage = null;

  canvas.clear();
  canvas.add(originalImage);
  canvas.requestRenderAll();
}

event_handlers["image-cropper"] = function (id, command, event_name) {
  console.log("image-cropper: " + JSON.stringify(command));
  switch (command.action) {
    case "loadImage":
      fabric.Image.fromURL(command.value, function (img) {
        img.scale(ORIGINAL_SCALE);
        img.set({
          left: (elements[id].canvas.width - img.width * img.scaleX) / 2,
          top: (elements[id].canvas.height - img.height * img.scaleY) / 2,
          hasControls: false,
          hasBorders: false,
          lockScalingFlip: true,
          transparentCorners: false,
          noScaleCache: false,
          strokeWidth: 0,
          lockMovementX: true,
          lockMovementY: true,
        });

        elements[id].canvas.add(img);
        elements[id].image = img;
      });
      break;
    case "cropAndMove":
      let axis = command.value.axis.toLowerCase();
      let scale = command.value.scale;
      moveImage(axis, elements[id].canvas, elements[id].image, scale, id);
      break;
    case "resetImage":
      resetImage(id);
    default:
      console.log("Unknown command: " + command.action);
  }
};

function moveImage(axis, canvas, originalImage, reportRate, id) {
  const otherAxis = axis === 'x' ? 'y' : 'x';

  const image = elements[id].lastModified[otherAxis] || originalImage;

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
    lockMovementX: true,
    lockMovementY: true,
  });

  canvas.remove(originalImage);
  if (elements[id].lastModified[axis]) {
    canvas.remove(elements[id].lastModified[axis]);
  }

  canvas.add(expandedImage);
  elements[id].lastModified[axis] = expandedImage;
  elements[id].latestCombinedImage = expandedImage
  canvas.requestRenderAll();
}

function updateImagePattern(canvas, originalImage, scale, id) {
  const image = elements[id].latestCombinedImage || originalImage;

  canvas.clear();

  const scaledWidth = image.width * scale;
  const scaledHeight = image.height * scale;

  const zoomFactor = canvas.getZoom();

  const visibleWidth = canvas.width / zoomFactor;
  const visibleHeight = canvas.height / zoomFactor;

  const cols = Math.ceil(visibleWidth / scaledWidth) * 2 + 1;
  const rows = Math.ceil(visibleHeight / scaledHeight) * 2 + 1;

  const imagesArray = [];

  for (let row = -Math.floor(rows / 2); row <= Math.floor(rows / 2); row++) {
    for (let col = -Math.floor(cols / 2); col <= Math.floor(cols / 2); col++) {
      const clonedImg = fabric.util.object.clone(image);

      clonedImg.set({
        left: (canvas.width - scaledWidth) / 2 + col * scaledWidth,
        top: (canvas.height - scaledHeight) / 2 + row * scaledHeight,
        scaleX: scale,
        scaleY: scale,
      });

      imagesArray.push(clonedImg);
    }
  }

  const group = new fabric.Group(imagesArray, {
    lockMovementX: true,
    lockMovementY: true,
    patternGroup: true,
  });

  canvas.add(group);

  canvas.requestRenderAll();

  return group;
}
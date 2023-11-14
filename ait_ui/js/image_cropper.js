let ORIGINAL_SCALE = 0.3;
let currentScale = ORIGINAL_SCALE;
let brushSize = 140;

const MIN_SCALE = 0.15;
const MAX_SCALE = 5;
fabric.Object.prototype.hoverCursor = 'default';

event_handlers["init-image-cropper"] = function (id, value, event_name) {
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
    moveRates: { x: 1, y: 1 },
    lastAxisMoved: 'x',
  };

  canvas.on('mouse:wheel', function (opt) {
    opt.e.preventDefault();
    var delta = opt.e.deltaY;
    var proposedScale = currentScale;
    if (proposedScale >= MIN_SCALE && proposedScale <= MAX_SCALE) {
      currentScale = proposedScale;
      if (typeof repeater_checkbox !== 'undefined' && repeater_checkbox && repeater_checkbox.checked) {
        var zoom = canvas.getZoom();
        zoom *= 0.999 ** delta;
        if (zoom > MAX_SCALE) zoom = MAX_SCALE;
        if (zoom < MIN_SCALE) zoom = MIN_SCALE;

        var center = canvas.getCenter();
        canvas.zoomToPoint({ x: center.left, y: center.top }, zoom);
        let axisToUse = elements[id].lastAxisMoved;
        let scaleToUse = elements[id].moveRates[axisToUse];
        updateImagePattern(canvas, elements[id].image, currentScale, id, axisToUse, scaleToUse);

        if (typeof input_canvas_id !== 'undefined' && input_canvas_id) {
          let inputCanvas = elements[input_canvas_id].canvas;
          inputCanvas.zoomToPoint({ x: center.left, y: center.top }, zoom);
          updateImagePattern(inputCanvas, elements[input_canvas_id].image, currentScale, input_canvas_id, axisToUse, scaleToUse);
        }
        return;
      }
      var zoom = canvas.getZoom();
      zoom *= 0.999 ** delta;
      if (zoom > MAX_SCALE) zoom = MAX_SCALE;
      if (zoom < MIN_SCALE) zoom = MIN_SCALE;

      var center = canvas.getCenter();
      canvas.zoomToPoint({ x: center.left, y: center.top }, zoom);
    }


    opt.e.stopPropagation();
  });

  canvas.on('mouse:move', function (opt) {
    if (opt.e.buttons === 1 && !opt.e.ctrlKey) {
      var delta = new fabric.Point(opt.e.movementX, opt.e.movementY);
      canvas.relativePan(delta);

      if (typeof input_canvas_id !== 'undefined' && input_canvas_id) {
        let inputCanvas = elements[input_canvas_id].canvas;
        inputCanvas.relativePan(delta);
      }
    }
  });

  event_handlers["repeater-checkbox"](id, value, event_name);
  brush_element_id.addEventListener('change', function (e) {
    brushSize = this.value * 2;
    updateAndMoveImage(id, elements[id], elements[id].lastAxisMoved, elements[id].canvas, elements[input_canvas_id].scale);
  });

  brush_slider_text_input_id.addEventListener('change', function (e) {
    brush_element_id.value = this.value;
    brush_element_id.dispatchEvent(new Event('change'));
  });
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
  switch (command.action) {
    case "loadImage":
      fabric.Image.fromURL(command.value, function (img) {
        elements[id].canvas.clear();
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
          //lockMovementX: true,
          //lockMovementY: true,
          patternGroup: true,
          objectCaching: false,
        });
        elements[id].canvas.add(img);
        elements[id].image = img;
        elements[id].latestCombinedImage = img;
        if (id === input_canvas_id)
          updateAndMoveImage(id, elements[id], 'x', elements[id].canvas, 1);
      });

      break;
    case "cropAndMove":
      console.log(command.value);
      const axis = command.value.axis.toLowerCase();
      const element = elements[id];
      const canvas = element.canvas;
      const scale = command.value.scale;
      updateAndMoveImage(id, element, axis, canvas, scale);
      break;
    case "resetImage":
      resetImage(id);
    case "close":
      elements[id].canvas.clear();;
      break;
    default:
      break;
  }
};

event_handlers["repeater-checkbox"] = (id, value, event_name) => {
  if (typeof repeater_checkbox !== 'undefined' && repeater_checkbox) {
    repeater_checkbox.addEventListener('change', function () {
      if (this.checked) {
        let inputCanvas = elements[input_canvas_id].canvas;
        const imageToUseInput = elements[input_canvas_id].latestCombinedImage || elements[input_canvas_id].image;

        let outputCanvas = elements[output_canvas_id].canvas;
        const imageToUseOutput = elements[output_canvas_id].latestCombinedImage || elements[output_canvas_id].image;

        let axisToUse = elements[output_canvas_id].lastAxisMoved;
        let scaleToUse = elements[output_canvas_id].moveRates[axisToUse];

        updateImagePattern(inputCanvas, imageToUseInput, currentScale, input_canvas_id, axisToUse, scaleToUse);
        updateImagePattern(outputCanvas, imageToUseOutput, currentScale, output_canvas_id, axisToUse, scaleToUse);

        inputCanvas.remove(elements[input_canvas_id].image);
        outputCanvas.remove(elements[output_canvas_id].image);

      } else {
        let inputCanvas = elements[input_canvas_id].canvas;
        const imageToUseInput = elements[input_canvas_id].latestCombinedImage || elements[input_canvas_id].image;

        let outputCanvas = elements[output_canvas_id].canvas;
        const imageToUseOutput = elements[output_canvas_id].latestCombinedImage || elements[output_canvas_id].image;

        inputCanvas.getObjects().forEach(function (obj) {
          if (obj.patternGroup) {
            inputCanvas.remove(obj);
          }
        });
        outputCanvas.getObjects().forEach(function (obj) {
          if (obj.patternGroup) {
            outputCanvas.remove(obj);
          }
        });
        inputCanvas.add(imageToUseInput);
        outputCanvas.add(imageToUseOutput);
        inputCanvas.requestRenderAll();
        outputCanvas.requestRenderAll();
      }

    });

  }
};

// Define a function to update the pattern and perform image movement
const updateAndMoveImage = (id, element, axis, canvas, scale) => {
  const imageToUse = element.latestCombinedImage || element.image;
  element.lastAxisMoved = axis;
  element.scale = scale;
  canvas.clear();

  canvas.getObjects().forEach(obj => {
    if (obj.patternGroup) {
      canvas.remove(obj);
    }
  });

  canvas.add(imageToUse);
  canvas.requestRenderAll();

  moveImage(axis, canvas, element.image, element.scale, id);

  if (repeater_checkbox && repeater_checkbox.checked) {
    element.patternGroup = updateImagePattern(canvas, imageToUse, currentScale, id, axis, element.scale);
    canvas.remove(element.image);
  }
};

function moveImage(axis, canvas, originalImage, reportRate, id) {
  canvas.clear();
  elements[id].moveRates[axis] = reportRate;

  if (axis === 'x' && elements[id].moveRates['y'] !== 1) {
    elements[id].moveRates['y'] = 1;
  } else if (axis === 'y' && elements[id].moveRates['x'] !== 1) {
    elements[id].moveRates['x'] = 1;
  }

  const rateX = originalImage.width * elements[id].moveRates['x'];
  const rateY = originalImage.height * elements[id].moveRates['y'];

  const finalCanvas = document.createElement('canvas');
  finalCanvas.width = originalImage.width;
  finalCanvas.height = originalImage.height;

  const finalCtx = finalCanvas.getContext('2d');

  finalCtx.drawImage(originalImage._element, rateX, rateY, originalImage.width - rateX, originalImage.height - rateY, 0, 0, originalImage.width - rateX, originalImage.height - rateY);
  finalCtx.drawImage(originalImage._element, 0, rateY, rateX, originalImage.height - rateY, originalImage.width - rateX, 0, rateX, originalImage.height - rateY);
  finalCtx.drawImage(originalImage._element, rateX, 0, originalImage.width - rateX, rateY, 0, originalImage.height - rateY, originalImage.width - rateX, rateY);
  finalCtx.drawImage(originalImage._element, 0, 0, rateX, rateY, originalImage.width - rateX, originalImage.height - rateY, rateX, rateY);


  if (id === input_canvas_id && isBrushChecked.checked) {
    drawRect(finalCtx, originalImage, brushSize, rateX, rateY);
  }

  const expandedImage = new fabric.Image(finalCanvas, {
    left: originalImage.left,
    top: originalImage.top,
    scaleX: originalImage.scaleX,
    scaleY: originalImage.scaleY,
    hasControls: false,
    hasBorders: false,
    lockScalingFlip: true,
    transparentCorners: false,
    noScaleCache: false,
    strokeWidth: 0,
    //lockMovementX: true,
    //lockMovementY: true,
  });

  canvas.remove(originalImage);
  if (elements[id].lastModified[axis]) {
    canvas.remove(elements[id].lastModified[axis]);
  }


  canvas.add(expandedImage);
  elements[id].lastModified[axis] = expandedImage;
  elements[id].latestCombinedImage = expandedImage;
  canvas.requestRenderAll();


}

function updateImagePattern(canvas, originalImage, scale, id, axis, reportRate) {

  const image = elements[id].latestCombinedImage || originalImage;

  canvas.clear();

  if (image) {

    const scaledWidth = image.width * scale;
    const scaledHeight = image.height * scale;

    const zoomFactor = canvas.getZoom();

    const visibleWidth = canvas.width / zoomFactor;
    const visibleHeight = canvas.height / zoomFactor;

    const cols = Math.ceil(visibleWidth / scaledWidth) * 2 + 1;
    const rows = Math.ceil(visibleHeight / scaledHeight) * 2 + 1;

    const imagesArray = [];

    let offset = 0;

    const loop1 = axis === 'y' ? cols : rows;
    const loop2 = axis === 'y' ? rows : cols;

    for (let i = -Math.floor(loop1 / 2); i <= Math.floor(loop1 / 2); i++) {
      for (let j = -Math.floor(loop2 / 2); j <= Math.floor(loop2 / 2); j++) {
        const clonedImg = fabric.util.object.clone(image);

        let col = axis === 'y' ? i : j;
        let row = axis === 'y' ? j : i;

        let left = (canvas.width - scaledWidth) / 2 + col * scaledWidth;
        let top = (canvas.height - scaledHeight) / 2 + row * scaledHeight;

        if (axis === 'x') {
          left += offset % scaledWidth;
        } else {
          top += offset % scaledHeight;
        }

        clonedImg.set({
          left: left,
          top: top,
          scaleX: scale,
          scaleY: scale,
          hasControls: false,
          hasBorders: false,
          lockScalingFlip: true,
          transparentCorners: false,
          noScaleCache: false,
          strokeWidth: 0,
          //lockMovementX: true,
          //lockMovementY: true,
          patternGroup: true,
          objectCaching: false,
        });
        imagesArray.push(clonedImg);
      }


      offset += (axis === 'x' ? scaledWidth : scaledHeight) * reportRate;

    }

    const group = new fabric.Group(imagesArray, {
      hasControls: false,
      hasBorders: false,
      lockScalingFlip: true,
      transparentCorners: false,
      noScaleCache: false,
      strokeWidth: 0,
      //lockMovementX: true,
      //lockMovementY: true,
      patternGroup: true,
      objectCaching: false,
    });

    canvas.add(group);

    canvas.requestRenderAll();

    return group;
  }
}


function drawRect(finalCtx, originalImage, brushSize, rateX, rateY) {
  finalCtx.beginPath();

  finalCtx.rect((originalImage.width - rateX) - brushSize / 2, 0, brushSize, originalImage.height);
  finalCtx.rect(0, (originalImage.height - rateY) - brushSize / 2, originalImage.width, brushSize);

  if (originalImage.width - rateX == 0 || rateX == 0) {
    finalCtx.rect((originalImage.width) - brushSize / 2, 0, brushSize, originalImage.height);
    finalCtx.rect(0, 0, brushSize / 2, originalImage.height);
  }
  if (originalImage.height - rateY == 0 || rateY == 0) {
    finalCtx.rect(0, (originalImage.height) - brushSize / 2, originalImage.width, brushSize);
    finalCtx.rect(0, 0, originalImage.width, brushSize / 2);
  }
  finalCtx.fillStyle = 'rgba(0,0,0,0.5)';
  finalCtx.fill();
  finalCtx.closePath();

}







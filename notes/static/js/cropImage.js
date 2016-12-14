(function () {
  const imageUrl = 'test';
  Tesseract.recognize(imageUrl)
    .then(result => {
      const symbolsArray = result.symbols.map(symbol => symbol.bbox);
      const wordsArray = result.words.map(word => word.text.length);
      var charCount = 0;
      var wordIndex = 0;
      const imageArray = symbolsArray.map(symbol => {
        var canvas = document.createElement('canvas');
        var context = canvas.getContext('2d');

        if (charCount == wordsArray[wordIndex]) {
          var imageObj = new Image();
          imageObj.onload = function(){
          context.drawImage(imageObj,0,0);
          };
          imageObj.src = spaceImage;
          charCount = 0;
          wordIndex++;
        }
        else {
          charCount++;
          var context = canvas.getContext('2d');
          context.canvas.width = symbol.x1 - symbol.x0 + 40;
          context.canvas.height = symbol.y1 - symbol.y0 + 40;
          canvas.style.left = symbol.x1;
          var imageObj = new Image();

          imageObj.onload = () => {
            var sourceX = symbol.x0;
            var sourceY = symbol.y0;
            var sourceWidth = symbol.x1 - symbol.x0;
            var sourceHeight = symbol.y1 - symbol.y0;
            var destWidth = sourceWidth;
            var destHeight = sourceHeight;
            var destX = 20;
            var destY = 20;
            context.drawImage(imageObj, sourceX, sourceY, sourceWidth, sourceHeight, destX, destY, destWidth, destHeight);
          }
          imageObj.src = imageUrl;
        }
        runNeuralNet(canvas);
      });
    });
})();

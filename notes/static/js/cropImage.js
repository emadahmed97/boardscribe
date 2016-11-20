(function () {
  // image to be recognized
  //const imageUrl = 'http://static1.squarespace.com/static/53960bf8e4b09069522f83c7/53baead5e4b0802f8dc8a60f/5665eacd841aba32da49f57b/1449520414575/?format=1000w';
  //const imageUrl = 'http://eddie-moore.com/wpfiles/wp-content/uploads/2013/05/hello_world.jpg';
  //const imageUrl = 'http://crm2.univ-lorraine.fr/pages_perso/Aubert/FTenglish/conv2d/hello.jpg';
  const spaceImage = 'https://www.tetley.co.uk/images/librariesprovider6/default-album/white-space.png?sfvrsn=0&MaxWidth=333&MaxHeight=&ScaleUp=false&Quality=High&Method=ResizeFitToAreaArguments&Signature=E181235533D33E367B6894D66ED0078AAC61270C';
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

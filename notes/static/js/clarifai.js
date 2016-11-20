var app = new Clarifai.App(
  'Dr6rtUIWZw_QdRwNb-LeFkvpt-8N2DKxxVyk1kMa',
  'dum7qKWHbHcGXNhRYm6aW4x42AAx-BUTCQDilPm4'
);
app.getToken();
var finalText = '';

function runNeuralNet(canvas) {
  document.body.appendChild(canvas);
  // const urlTo64Bit = canvas.toDataURL('image/jpg');
  // const urlTo64Bit = Base64.encode(canvas);
  const urlTo64Bit = canvas.toDataURL('image/png').replace(/^data:image\/(png|jpg);base64,/, '');
  console.log(urlTo64Bit);
  const formattedUrl = { base64: urlTo64Bit };
  const lettersId = 'd135d3da6cd943d5824c8a33124b9cdc';
  app.models.predict(lettersId, formattedUrl).then(
    function(response) {
      console.log(response);
      finalText = finalText + response.data.outputs[0].data.concepts[0].name;
      console.log(finalText);
    },
    function(err) {
      console.log(err);
    }
  ).catch(console.error);
}

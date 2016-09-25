var xhrRequest = function (url, type, callback)
{
  var xhr = new XMLHttpRequest();
  xhr.onload = function()
  {
    callback(this.responseText);
  };
  xhr.open(type,url);
  xhr.send();
};
Pebble.addEventListener('ready',
function(e)
{
  var dict = { 'SLEEPING': 0};
  setInterval
  (
    function()
    {
      var url = 'http://104.131.44.27:5000/';
//       var url = ''
      xhrRequest(url,'GET',
      function(responseText)
      {
        var res= responseText;
        var h1 = res.match(/<h1\b[^>]*>(.*?)<\/h1>/ig);
        var sum = 0;
        var count = 0;
        var avg = 0;
        
        for(var i = 0; i < h1.length; i++)
        {
          var data = h1[i].match(/\-?[0-9]+\.[0-9]+/gi);
          for(var j = 0; j < data.length; j++)
          {
            sum += parseFloat(data[j]);
            count++;
          }
            avg = sum / count;
        }
        dict.SLEEPING = (avg> 0.6) ? 1: 0;
        console.log(avg);
        console.log(dict.SLEEPING);
      });
      Pebble.sendAppMessage(dict);
    },5000);
}
);




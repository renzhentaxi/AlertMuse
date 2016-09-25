Pebble.addEventListener('ready',
function(e)
{
  var dict;
  setInterval
  (
    function()
    {
      var dict = { 'SLEEPING': 1};
      var url = 'https://jsonplaceholder.typicode.com/users';
      xhrRequest(url,'GET',
      function(responseText)
      {
        var json = JSON.parse(responseText);   
        console.log(json[0].name);
      });
      Pebble.sendAppMessage(dict);
    },3000);
}
);

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


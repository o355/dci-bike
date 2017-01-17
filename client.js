var net = require('net');
var HOST = '127.0.0.1';
var PORT = 8088;


var client = new net.Socket
client.connect( PORT, HOST, function () {
  
   console.log('BIKE # CONNECTED TO: ' + HOST + ':' + PORT);
  //write message here
  client.write('Bike # is now ready to transfer data');
  
});

client.on('data', function(data) {
  console.log('DATA ' + data );
    client.destroy();
});

client.on('close', function() {
    console.log('Connection closed');
});

client.on('reconnect' function() {
    client.connect( PORT, HOST, function () {
      console.log('BIKE # RECONNECTED TO: ' + HOST + ':' + PORT);
      //write message here 
      client.write('Bike # is now reconnected and ready to transfer data');
});

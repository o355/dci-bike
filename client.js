const net = require('net');



console.log('Now connecting to Server!');
const client = net.connect({port: 8088}, () = {
  console.log('Now connected to the Server!');
  client.write('I have now connected!');
});

client.on

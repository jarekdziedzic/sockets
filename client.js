var net = require('net');
var client = net.connect({port: 1234},
    function() {
        console.log('Connected to server!');
        client.write('Hello world!');
        client.end('Goodbye');
    });
client.on('data', 
    function(data) {
        console.log(data.toString());
    });

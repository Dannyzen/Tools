//nodejs packit.js --url <url> --hits <# of hits>

var argv = require('optimist').argv;
var unirest = require('unirest');

var counter =0

function packit(int){
    while (counter<int){
    unirest.get(argv.url).end(function (response) {
        if (response.code = 200){
            console.log("successful")
        }
        else {
            console.log("bad request")    
            }
    });
    counter++;
    }
}

packit(argv.hits)


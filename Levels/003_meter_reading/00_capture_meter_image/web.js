var express = require('express');
var app = express()
var df = require('dateformat');
const request = require('request')
var fs = require('fs')
var buffer_old = ""
lastdate= new Date()
app.use(express.static('public'))

alarm = function(msg) {
    channel = 'https://hooks.slack.com/services/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'
    if (typeof msg == 'string' && msg.indexOf('text') < 0) msg = {'text': msg }
    console.log('channel '+ channel)
    request.post(
    {
        url: channel,
        headers: {'Content-Type':'application/json'},
        body: msg,
        json: true
    },
    function (err, httpResponse, body) {
        if (err) console.log(err, body)
    });
}

app.get('/', function (req, res) {
    res.end(`Your IP is ${req.connection.remoteAddress.replace(/^.*:/, '')}`)
    alarm(`touched / ${req.connection.remoteAddress.replace(/^.*:/, '')}`)
})


app.get('/websensor', function(req,res) {
    if (buffer_old == "") {
        res.end("Meter image will be provided within an hour. Please try again later")
        alarm(`failed fetch empty@system restart ${req.connection.remoteAddress.replace(/^.*:/, '')}`)
    } else {
        res.end(buffer_old)
        alarm(`fetch ${buffer_old.length}B ${req.connection.remoteAddress.replace(/^.*:/, '')}`)
    }
})

app.post('/websensor', function (req, res) {
    console.log(`got file ${df(new Date(),"yyyy-m-d HH:MM:ss")}`)
    if (req.body == undefined) {
        buffer = new Buffer.alloc(0)
        req.on('data', function(chunk) {
            buffer = Buffer.concat([buffer, chunk])
        });

        req.once('end', function() {
            console.log(`done ${buffer.length}B`)
            buffer_old = buffer
            res.end("{X-ACK}")
            alarm(`new file ${buffer.length}B ${req.connection.remoteAddress.replace(/^.*:/, '')}`)
        });
    } else {
        res.end("{X-NACK}")
        alarm(`X-NACK: ${buffer.length}B ${req.connection.remoteAddress.replace(/^.*:/, '')}`)
    }
})

var server = app.listen(8080, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("listening at http://%s:%s", host, port)
})

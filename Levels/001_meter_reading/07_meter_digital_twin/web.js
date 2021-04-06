var express = require('express');
var app = express()
var df = require('dateformat');
const request = require('request')
var fs = require('fs')
var buffer_old = ""
file=""
value="0000.0"

app.use(express.static('public'))

alarm = function(msg) {
    channel = 'https://hooks.slack.com/services/T017L20056V/your_own_webhook_url'
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


function render() {
    file = fs.readFileSync('meter.html')
    r = String(file)

    v1 = value.split('.')[0]
    v2 = value.split('.')[1] + ""
    if (v2.length == 0) v2 = '0'
    console.log(`v1=${v1} v2=${v2}`)
    if (v1.length==1) sv = "000" + v1 + v2
    else if (v1.length==2) sv = "00" + v1 + v2
    else if (v1.length==3) sv = "0" + v1 + v2
    else sv = v1 + v2


    r = r.replace('${D1}', sv.slice(0,1))
    r = r.replace('${D2}', sv.slice(1,2))
    r = r.replace('${D3}', sv.slice(2,3))
    r = r.replace('${D4}', sv.slice(3,4))
    r = r.replace('${D5}', sv.slice(4,5))
    return r
}

app.get('/meter', function(req, res) {
   console.log('/meter')
   res.end(render())
})

app.get('/meter/:value', function(req, res) {
   value=req.params.value
   console.log(`/meter ${value}`)
   res.redirect('/meter')
})

app.get('/alarm/:msg', function(req, res) {
    alarm(req.params.msg)
    res.end("ok")
})


var server = app.listen(8080, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("listening at http://%s:%s", host, port)
})


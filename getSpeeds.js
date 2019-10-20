/*
 * Written by Nilushan Costa
 *
 * Purpose - Obtain WAN link bandwidth utilization of a Huawei 4G router
 * Input - None
 * Output - Download speed and upload speed in Bytes per second as csv values output line by line
 *
 */

var gatewayIp = process.argv[2];

var router = require('dialog-router-api').create({
    gateway: gatewayIp });

var exec = require('child_process').exec;

var downloadRate = 0;
var uploadRate = 0;
var latency = 0;

function loop(){
	router.getToken(function(error, token) {
    		router.getTrafficStatistics(token, function(error, response){
      			var downloadRateString =String(response.CurrentDownloadRate);
	    		downloadRate = downloadRateString.substring(0);
    		});
		router.getTrafficStatistics(token, function (error, response) {
			var uploadRateString = String(response.CurrentUploadRate);
			uploadRate = uploadRateString.substring(0);
		});
 	});
	console.log(downloadRate + "," + uploadRate);
	setTimeout(loop,2000);  //Run every 2 seconds
}

loop();


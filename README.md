# Huawei Router Dashboard

A monitoring dashboard for Huawei 4G routers. Has the ability to display the current bandwidth utilization on the WAN link and the latency to a remote server.
Please refer the following Medium article for details  
[Monitoring dashboard for Huawei 4G routers](https://medium.com/@nilushancosta/monitoring-dashboard-for-huawei-4g-routers-ce5126b18e2f)

## Prerequisites
1. Nodejs
2. Node Package Manager (NPM)
3. Python 3 with Matplotlib

## Installation Instructions
1. Clone the repository  
`git clone https://github.com/nilushancosta/huawei-router-dashboard.git`

2. change directory into the `huawei-router-dashboard` directory

3. Install the dialog router api npm package. Refer https://github.com/ishan-marikar/dialog-router-api for details  
`npm install dialog-router-api`

4. Open `run.sh` with a text editor and specify values for the DEFAULT\_GATEWAY\_IP, MAX\_DOWNLOAD\_SPEED and MAX\_UPLOAD\_SPEED variables. They are the IP address of the default Gateway, the maximum download speed of the 4G connection in Mbps and the maximum upload speed of the 4G connection in Mbps respectively.   
Ex. If the default gateway IP address is 192.168.1.1, maximum download speed is 8 Mbps and the maximum upload speed is 2 Mbps, the variables should be set as follows 
```
DEFAULT_GATEWAY_IP=192.168.1.1
MAX_DOWNLOAD_SPEED=8
MAX_UPLOAD_SPEED=2
```

5. Execute the `run.sh` script  
`bash run.sh`

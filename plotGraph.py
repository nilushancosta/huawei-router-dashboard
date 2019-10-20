### Written by Nilushan Costa

### Purpose - Plot the bandwidth utilization of the 4G router and the latency to a remote server
### Input - Download and upload speed in bytes per second as csv values measured periodically and input line by line
### Output - Two real-time plots; Speed and latency

### Implementation method 
# Download speed, Upload speed and latency are inserted into three FIFO queues. Matplotlib plots the 
# graphs using this data

import sys
import subprocess
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

speedYLimMax=int(sys.argv[1])

latencyProcess = subprocess.Popen("ping 8.8.8.8", shell=True, stdout=subprocess.PIPE) #ping Google DNS
plt.ylim([0,2])
x = [60,58,56,54,52,50,48,46,44,42,40,38,36,34,32,30,28,26,24,22,20,18,16,14,12,10,8,6,4,2,0]
downloadRate = [0]*31
uploadRate = [0]*31
latency = [0]*31
plt.ion()

fig = plt.figure(figsize=(20,10))
fig.patch.set_facecolor('xkcd:black') #set background colour of figure

#Bandwith utilization graph
speedGraph = fig.add_subplot(2,1,1)
speedGraph.set_title('Upload and Download speed')
speedGraph.title.set_color('orange')
speedGraph.set_ylim([0,speedYLimMax+1])
speedGraph.set_xlabel('time')
speedGraph.xaxis.label.set_color('orange')
speedGraph.set_ylabel('Speed (Mbps)')
speedGraph.yaxis.label.set_color('orange')
speedGraph.spines['top'].set_color('orange')
speedGraph.spines['right'].set_color('orange')
speedGraph.spines['bottom'].set_color('orange')
speedGraph.spines['left'].set_color('orange')
downloadRatePatch = mpatches.Patch(color='blue', label='Download speed')
uploadRatePatch = mpatches.Patch(color='green', label='Upload speed')
speedGraph.legend(handles=[downloadRatePatch, uploadRatePatch])
line1, = speedGraph.plot(x,downloadRate,'b-')
line2, = speedGraph.plot(x,uploadRate,'g-')
speedGraph.tick_params(axis='x', colors='orange')
speedGraph.tick_params(axis='y', colors='orange')
speedGraph.set_facecolor('black')
plt.margins(0)

#Latency graph
latencyGraph = fig.add_subplot(2,1,2)
latencyGraph.set_title('Latency to 8.8.8.8')
latencyGraph.title.set_color('orange')
latencyGraph.set_xlabel('time')
latencyGraph.xaxis.label.set_color('orange')
latencyGraph.set_ylabel('Latency (ms)')
latencyGraph.yaxis.label.set_color('orange')
latencyGraph.spines['top'].set_color('orange')
latencyGraph.spines['right'].set_color('orange')
latencyGraph.spines['bottom'].set_color('orange')
latencyGraph.spines['left'].set_color('orange')
lineb1, = latencyGraph.plot(x, latency, 'r-')
plt.subplots_adjust(hspace=0.3, left=0.06, right=0.95, bottom=0.06, top=0.95)
latencyGraph.tick_params(axis='x', colors='orange')
latencyGraph.tick_params(axis='y', colors='orange')
latencyGraph.set_facecolor('black')
plt.margins(0)

while 1:
    inputValues = sys.stdin.readline().split(',')
    downloadSpeed = float(inputValues[0]) #speed is in Bps
    uploadSpeed = float(inputValues[1]) #speed is in Bps
    
    downloadSpeedInMbps = (downloadSpeed * 8 ) / 1000000 #convert Bps to Mbps
    downloadRate.append(downloadSpeedInMbps)
    if (len(downloadRate) > 31):
        del downloadRate[0]
    
    uploadSpeedInMbps = (uploadSpeed * 8)/1000000  #Convert Bps to Mbps
    uploadRate.append(uploadSpeedInMbps)
    if (len(uploadRate)> 31):
        del uploadRate[0]

    extracted = str(latencyProcess.stdout.readline()).split(' ')[6].split('=') #Extract RTT (includes 'time' label as well)
    if (len(extracted) > 1):
        latency.append(float(extracted[1])) #get RTT value
    if (len(latency) > 31):
        del latency[0]

    ## Uncomment the following lines to print the raw data in the queues to the console
    #print(downloadRate)
    #print(uploadRate)
    #print(latency)

    line1.set_ydata(downloadRate)
    line2.set_ydata(uploadRate)
    lineb1.set_ydata(latency)
    latencyGraph.relim()
    latencyGraph.autoscale_view(True,False,True)
    fig.canvas.draw()

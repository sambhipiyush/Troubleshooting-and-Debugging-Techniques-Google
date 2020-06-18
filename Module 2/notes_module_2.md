Troubleshooting and Debugging Techniques
=========================================

by Google

# Module 2
#
## Title: SLOWNESS

### Learning Objectives

* Rundown of the different reasons that can make things run slowly by:
	* Looking into what causes slow scripts, slow computers, or slow systems
	* Looking into what tools are there to help identify the most common causes of slowness, and apply solutions to improve the overall performance

### Why is my computer slow

* The general strategy for addressing slowness is to **identify the bottleneck** for addressing slowness in  device, script, or system to run slowly. Some of the reaons could be:
	* Running out of the CPU time
	* Time spent reading data from disk waiting for data transmitted over the network
	* Moving data from disk to RAM
* Treat each part of the computer (CPU, memory, disk, newtwork bandwidth) as **finite resources**.
* Identifying the bottleneck allows us to manage the available resources more effectively. In order to find what is causing the bottleneck, **monitor** the usage of resources to know which of them are being exhausted.
* We can use the following commands on Linux to monitor the usage of resources:
	* ```top``` command on shows
		* Which currently running processes are using the most CPU time
		* Which currently running processes are using the most memory
	* Other load information related to the current state of the computer such as how many processes are running and how the CPU time or memory is being used
	* ```iotop``` command shows which processes are currently using the most disk IO usage and swap memory usage
	* ```iftop``` command shows which processes are currently using the most network bandwidth
* Therefore, steps to diagnose what's causing the computer to run slow would be:
	1. Open one of above tools to check what's going on
	2. Try to understand which resources the bottleneck and why
	3. Plan how you're going to solve the issue

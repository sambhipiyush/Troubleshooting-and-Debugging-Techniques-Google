Troubleshooting and Debugging Techniques
=========================================

by Google

# Module 1
#
## Title: TROUBLESHOOTING CONCEPTS

### Introduction to Debugging

#### What is debugging

> Wireshark is an open source tool for profiling network traffic and analyzing TCP/IP packets
#
> The tcpdump tool is a powerful command-line analyzer that captures or "sniffs" TCP/IP packets

* Problems may caused by the any of the following
	* Hardware
	* The operating system
	* Applications running on the computer
	* The environment and configuration of the software
* **Troubleshooting** is the process of identifying, analyzing, and solving problems while **Debugging** is the process of identifying, analyzing, and removing bugs in a system.
* But generally, we say **troubleshooting** when we're fixing problems in the system running the application, and **debugging** when we're fixing the bugs in the actual code of the application.
* **Debuggers** let us follow the code line by line, inspect changes in variable assignments, interrupt the program when a specific condition is met, and more.
* On top of that, if we can modify the code, we can change it so that it provides more logging information
	* This can help us understand what's going on behind the scenes
* There are different tools to get information about the system and what the programs in our system are doing:
	* **tcpdump** and **Wireshark**: shows ongoing network connections, and help with analyzing the traffic going over the cables
	* **ps**, **top**, or **free**: shows the number and types of resources used in the system
	* **strace**: shows the system calls made by a program
	* **ltrace**: shows the library calls made by the software

#### Problem Solving Steps

1. Getting Information : Gathering as much information from any of the existing documentation about
    * The current state of things
    * What the issue is
    * When it happens
    * What the consequences are
    * Reproduction case, which is a clear description of how and when the problem appears --> Super important resource to resolve a problem
	1. Existing documentation can be
	    1. This can be internal documentation
	    1. Manual pages
	    1. Questions asked on internet
1. Find the root cause of the problem
	* This is usually the most difficult step
	* But the key here is to get to the bottom of 
		* what's going on
		* what triggered the problem
		* how we can change that
1. Perform the necessary remediation
	* Depending on the problem, this might include
		* **Immediate remediation** - to get system back to health
		* **Medium** or **long-term remediation** - to avoid the problem in future
    * Workaround can be used when we could understand the problem just enough and try our users get back to work quickly
    * Ultimately, prevent the problem from occurring to save time in the future

* Also document the debugging process for the future referece. (This will make your life easy if in case same issue comes up again)

#### Silently Crashing Application

* Details we can ask when someone reports an issue
	* What the error is that the user is getting
	* check if we experience the same failure
* One of the tools to check what is going on with the system and with our applications
	* **strace**
		* lets us look more deeply at what the program is doing
		* It will trace a system calls made by the program and tell us what the result of each of these calls was
		* This command shows us all the system calls are program made
		```bash
		$ strace ./<PROGRAM_NAME>
		```
		* Manage output of **strace** command
			* We could pipe the output of **strace** to the less command which we could use to scroll through a lot of texts
			* We could use the `-o` flag of the **strace** command to store the output into a file and then browse the contents of that file
			* The `-o` flag, lets us refer back to the file later if we need to so, let's go with that one
			```bash
			$ strace -o <OUTPUTFILE_NAME> ./<PROGRAM_NAME>
			$ less <OUTPUTFILE_NAME>  #Shift + G , to go to the end of file
			# OR
			$ strace ./<PROGRAM_NAME> | less
			```
* **System Calls** are the calls that the programs running on our computer make to the running kernel
	* There are loads of different system calls and depending on what we're trying to debug


### Understanding the Problem

#### It Doesn't Work

> Q: When a user reports that a "website doesn't work," what is an appropriate follow-up question you can use to gather more information about the problem?
  A: Asking the user what steps they performed will help you gather more information in order to better understand and isolate the problem

* There are some common questions that we can ask a user that simply report something doesn't work
	* What were you trying to do?
	* What steps did you follow?
	* What was the expected result?
	* What was the actual result?
* When debugging a problem, we want to consider the simplest explanations first and avoid jumping into complex or time-consuming solutions unless we really have to
* After having a basic idea of what the problem is
	* Try to figure out the **root cause** by applying a **process of elimination**
		* starting with the **simplest explanations** first and testing those until you can isolate the **root cause**
* **top** command shows the state of the computer and processes using the most CPU and shows if the computer is super overloaded
* The **load average** on Linux shows how much time a processor is busy in a given minute, with one meaning it was busy for the whole minute
	* So normally this number shouldn't be above the amount of processors in the computer
	* A number higher than the amount of processors means the computer is overloaded
* **kill-stop** - This will suspend the execution of the program until you let it continue or decide to terminate it

#### Creating a Reproduction Case

* A **reproduction case** is a way to verify if the problem is present or not
	* When trying to create a reproduction case, we want to find the actions that reproduce the issue, and we want these to be as simple as possible
	* The smaller the change in the environment and the shorter the list of steps to follow, the better
* Bunch of reasons in user's environment or configuration for application failure are
	1. network routing
	1. old config files interfering with a new version of the program
	1. a permissions problem blocking the user from accessing some required resource
	1. even some faulty piece of hardware acting out
* When debugging, the first step is to **read the logs**. Which logs to read, will depend on the operating system and the application that you're trying to debug.
	* On **Linux**, read system logs like `/var/log/syslog` and user-specific logs like `the.xsession-errors` file located in the user's home directory
	* On **MacOs**, on top of the `system logs`, go through the logs stored in the `library logs` (`/Library/Logs`) directory
	* On **Windows**, use the `Event Viewer tool` to go through the event logs
* No matter the operating system, remember to look at the logs when something isn't behaving as it should
	* Lots of times, you'll find an error message that will help you understand what's going on like, unable to reach server, invalid file format, or permission denied
* If in case error message from logs are not very useful like ~~Internal System Error~~, then next step is to isolate the conditions that trigger the issue, by asking questions like
	1. Do other users in the same office also experienced the problem?
	1. Does the same thing happen if the same user logs into a different computer?
	1. Does the problem happen if the applications config directory is moved away?
* Having a clear reproduction case, let's do investigate the issue, and quickly see what changes it
	* For example, 
		* does the problem go away if you revert the application to the previous version?
		* Are there any differences in the strace log, or the ltrace logs when running the application with the bug config and without it? 
		* On top of that, having a clear reproduction case, lets you share with others when asking for help

#### Finding the Root Cause

> Understanding the root cause is essential for providing the long-term resolution.

* Understanding the root cause is essential for performing the long-term remediation.
* How do we go about finding the actual root cause of the problem?
	* We generally follow a cycle of looking at the information we have, coming up with a hypothesis that could explain the problem, and then testing our hypothesis
	* If we confirm our theory, we found the root cause. If we don't, then we go back to the beginning and try different possibility
	* We need to come up with an idea of a possible cause, check if it's correct and if not, come up with a different idea until we find one that explains the problem
* To make these hypothesis and trying out new ideas we need to 
	* We look at information we currently have and gather more if we need
	* Searching online for the error messages that we get or looking at the documentation of the applications involved can also help us imagine new possibilities of what might be at fault
	* Whenever possible, we should check our hypothesis in a **test environment**, instead of the production environment that our users are working with
		* We avoid interfering with what our users are doing and we can tinker around without fear of breaking something important
* Tools which can be used for root cause analysis
	* **iotop**, which is a tool similar to top that lets us see which processes are using the most input and output
	* **iostat** and **vmstat**, these tools show statistics on the input/output operations and the virtual memory operations
	* **ionice** Reduce the I/O priority of the scrip, so that it does not disrupt other processes
	* **iftop** shows the current traffic on the network interfaces
	* **rsync** command, which is often used for backing up data, includes a `-bwlimit`, just for this purpose
	* **Trickle** this a program to limit the bandwidth being used
	* **nice** command to reduce the priority of the process and accessing the CPU


#### Dealing with Intermitent Issues

> Power cycling releases resources stored in cache or memory, which gets rid of the problem.

* Most common issues that most of us have dealt with programs are 
	1. randomly crashing
	1. laptops that sometimes fail to suspend
	1. web services that unexpectedly stop replying
	1. file contents that get corrupted
* When dealing with intermitent issues,
	1. Get more involved in what's going on, so that you understand when the issue happens and when it doesn't
	    * Usually invovles going through logs or enabling debugging information
	2. Look at different sources of information, like the load on the computer, the processes running at the same time, the usage of the network, and so on
* If a problem goes away by turning it off and on again, there's almost certainly a bug in the software, and the bug probably has to do with not managing resources correctly.
* Many applications and services already include a debugging mode that generates a lot more output then the default mode
	* By enabling the debug information in advance, you can get a better picture of what's going on the next time the problem happens
	* If that's not possible, you'll need to resort to monitoring the environment when the issue triggers
* Depending on what the problem is, you might want to look at different sources of information, like 
	1. the load on the computer
	1. the processes running at the same time
	1. the usage of the network , etc ...
* Types of Intermitent issues
	* **Observer effect**, where just observing a phenomenon alters the phenomenon.
		* Werner Heisenberg, a scientist described observer's effect
		* These bugs usually 
			1. point to bad resource management
			1. Maybe the memory was wrongly allocated
			1. the network connections weren't correctly initialized
			1. the open files weren't properly handled
	* Another type of intermittent issue is the one that goes away when we turn something off and on again
		* There's plenty of jokes related to how, in IT, a lot of what we do to solve problems, is just turn things off and on again
			* in many cases, power cycling a device or restarting a program gets rid of whichever problem we were trying to fix
		* But why is that?
			* When we reboot a computer or restart a program, a bunch of things change like 
				1. Going back to a clean slate means releasing all allocated memory
				1. deleting temporary files
				1. resetting the running state of programs
				1. re-establishing network connections
				1. closing open files and more
		* If a problem goes away by turning it off and on again, there's almost certainly a bug in the software, and the bug probably has to do with not managing resources correctly

##### Review

1. Few ways of getting to the root cause of a problem, like 
	1. isolating causes
	1. understanding error messages
	1. adding logging information
	1. generating new ideas for possible failures
1. Also talked about problems that go away on their own and then pop up again, and looked at how to figure those out


### Binary Searching a Problem

#### What is binary search

* **Linear search** works but the longer the list, the longer it can take to search
	* Time it takes to search is proportional to the length of list
	* In a list of 1000 elements, worst case is 1000 comparisons
* If the list is **sorted**, we can use an alternative algorithm for searching called **binary search**
	* It may take more time to sort an unsorted list to perform binary search
	* It can still make sense to do it if we're going to search through it several times
	* It doesn't make sense to sort the list and then use binary search to only find one element
		* In that case, using linear search is simpler and faster
	* In a list of 1000 elements, worst case is only 10 comparisons
	* In a list of 100,000 elements, worst case is only 17 comparisons
	* **NOTE: List needs to be sorted for this algorithm to work**

#### Applying Binary Search in Troubleshooting

* In troubleshooting, we can apply **bisecting** to go through and test a long list of hypotheses, list can have items like
	* entries in a file
	* extensions enabled
	* boards connected to a server
	* even lines of code added to a faulty release
* With each iteration, the problem is cut in half
	* When doing this, the list of elements contains all the possible causes of the problem and we keep reducing the problem by half until only one option is left
* This approach is sometimes called **bisecting** which means dividing in two
* When using Git for version control, we can use a __Git command called `bisect`__
	* Bisect receives two points in time in the Git history and repeatedly lets us try the code at the middle point between them until we find the commit that caused the breakage
	* You can use the **bisect** command to find out which command cause the software to stop working

#### Finding Invalid Data

> We should always do troubleshooting in TEST environment, and not in PRODUCTION environment.

* **wc** command - counts characters, words, and lines in a file
	* `-l` - flag to print the line count
	* `-w` - flag to print the word count
	* `-m` - flag to print the character count
	* `-c` - flag to print the byte counts
* **head** command - prints the first lines in the file
	* We can pass the amount of lines we want to include as a parameter
	* `-nK` - flat to print the first K lines instead of the first 10
* **tail** command - to print the last lines
	* We can pass the amount of lines we want to include as a parameter
	* `-nK` - flag to output the last K lines, instead of the last 10


### Module Review

* We learned the general principles of debugging and troubleshooting
* We looked into the basic process of solving a technical problem like 
	* getting information
	* finding the root cause
	* implementing the remediation
* We learned about a bunch of different tools and techniques that we can use to better understand what's going on with our systems and our programs, including 
	* how to create a reproduction case
	* how to find the root cause for problem
	* how to deal with issues that only appear occasionally
* We learned about the binary search algorithm, and how we can use it to bisect a problem and quickly find the root cause of a technical problem
* We have seen how we can apply this to lots of different types of problems, like 
	* a bug in our code
	* a bug in someone else's code
	* a configuration issue
	* even a hardware problem
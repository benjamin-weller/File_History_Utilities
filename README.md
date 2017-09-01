# File_History_Utilities
I have been getting up early to program in the morning, this plays well with my goal to program for an hour each day. As a result, from these two happenings I decided to start this project. I tried to take it slow and estimate the length of time this project would take (I initially thought three hours, but it turned out to be six). On a final note for the first three hours I forced myself to only work on them an hour each day, doing this I learned a lot about switching costs, and the power of flow.

**First(s) during this project**
1.	Honestly trying idiomatic Python
2.	Project estimation, this was very difficult!
3.	Pylint and Python styling
4.	Large scale OS interactions via programs

**What I learned:**
1.	Python is awesome!
2.	Estimations are hard
3.	Feature creep is a real thing (I thought I was done at hour 2)
4.	Refer to the first point
5.	Go with the flow (don’t “break the chain”)

**Problem:**

I was switching between operating systems and decided to make a fresh install of Windows. I use the File History backup feature on an external drive. It’s great to have backups but when I copied everything over, all my files had odd timestamps associated with them. I knew due to the magnitude of the problem that I wouldn’t be trying to solve this issue with simple batch file scripting. I instead chose to more fun and versatile tool, Python. 

**Issues/Cases to keep in mind:**
1.	Some files have been tracked through file history a few different times, they have two time stamps (shown below).
2.	If I modified a word document, saved it, and then ran file history there would be two copies of the file basically with the same name. The only differentiating factor would be the time stamp (shown below). I want my program to remove the older files.
3.	Some files have the Windows standard “(1)” placed at the end of the file name, I have to be sure that I’m not targeting those files.
4.	While renaming files I must keep their extensions intact. I can’t rename a word file and delete its “.docx” extension.
5.	All files when being copied out of File History are read only, as such I need to change that before I delete or rename any of the files.

![problem picture](https://user-images.githubusercontent.com/22554871/29929432-8712a358-8e39-11e7-946b-2b700d074fec.png)

**Solution:**

I developed a program that used regular expressions and some very handy methods from the os module to complete my aims.

**Features of my program:**
1.	Recursively crawls the file system given a root directory
2.	Removes time stamps
3.	Ensures extensions remain intact
4.	Deletes “old” and “redundant” files.
5.	Makes all files both readable and writable
6.	Accurately targets time stamps (doesn’t get confused with “(1)” endings)
7.	Handles periods positioned within file names correctly

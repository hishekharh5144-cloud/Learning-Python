                     #HOW STRING WORK INTERNALLY

#-->Each character in a string is stored with its own unicode number. That,s why string use more memory than integer

from operator import index


ord("A") # -->65 (unicode of a)
chr(65)  #--> "A" (character from unicode)

#-->String indexing

#-->  Negative index   # -7-6-5-4-3-2-1
                       #  C O L L E G E
#-->  positive index   #  0 1 2 3 4 5 6

a="COLLEGE"
print(a[0],a[-7])   #this will print c because in both negative and posive C is there 
print(a[-1],a[-6])  

                               #string slicing

#if i want to take a portion from my string

                     # -8-7-6-5-4-3-2-1
                     #  H I M A N S H U
                     #  0 1 2 3 4 5 6 7
b="HIMANSHU"
#b[start:stop:step]
#start-->from where i want to start the slicing
#stop-->from where i want to stop the slicing+1,if i want to stop at 5th index then i will write 6 because it will stop at 5th index.
#step-->step size
print(b[3:6:1])

#if i want to print H M N H i have to write step size 2 because i want to skip 1 character after every character
print(b[0:8:2])

#i can also write like this
print(b[::2])
'''this will print H M N H because i have not given any start and stop index
so it will take the whole string and step size is 2 so it will skip 1 character after every character'''

#if i keep this funtion empty,this has a default value of start=0,stop=len(string),step=1
print(b[::])
'''this will print the whole string because i have not given any start and stop index 
so it will take the whole string and step size is 1 so it will not skip any character'''

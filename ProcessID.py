import os

print("PID of current process is : ",os.getpid())
print("PID of parent process is : ",os.getppid())

#OUTPUT
# (base) prajaktashinde@Prajaktas-MacBook-Pro 5th July 2026 % python ProcessID.py
# PID of current process is :  1662
# PID of parent process is :  1197
# (base) prajaktashinde@Prajaktas-MacBook-Pro 5th July 2026 % python ProcessID.py
# PID of current process is :  1675
# PID of parent process is :  1197
# (base) prajaktashinde@Prajaktas-MacBook-Pro 5th July 2026 % python ProcessID.py
# PID of current process is :  1685
# PID of parent process is :  1197
# (base) prajaktashinde@Prajaktas-MacBook-Pro 5th July 2026 % python ProcessID.py
# PID of current process is :  1686
# PID of parent process is :  1197

#Below is for MacOS / Linux
# ps - command on command prompt/terminal
# (base) prajaktashinde@Prajaktas-MacBook-Pro 5th July 2026 % ps
#   PID TTY           TIME CMD
#  1197 ttys000    0:00.05 -zsh
#  1381 ttys002    0:00.01 /bin/zsh

#Below for Windows
# tasklist - command on command prompt
# Output on command prompt is number of tasks list.

#Note: Here parent process is command prompt/terminal

#Check Linux OS installation on MacOS using virtual machine. Check dual boot
# Linux operating systems is for developers by developers and maintained by developers
#!/usr/bin/env python3
import os
import sys
VERSION = "0.1.3"
help_msg="""
pstat by Proactive Development 2022

Standard Commands:
    -V  --app-version  Displays the current version of pstat
    -i  --cpuinfo      Displays the /proc/cpuinfo file and returns information about the processor, such as its type, make, model, and performance.
    -I  --interrupts   Displays the /proc/interrupts file and shows which interrupts are in use, and how many of each there have been.
    -f  --filesystems  Displays the /proc/filesystems file and shows filesystems configured/supported into/by the kernel.
    -fm --file-max     Displays the /proc/sys/fs/file-max file and shows filesystem max storage size.
    -m  --iomem        Displays the /proc/iomem file and shows a memory map
    -M  --mounts       Displays the /proc/mounts file and shows what mounted filesystems are attached to the kernel
    -p  --partitions   Displays the /proc/partitions file and shows a table of partitions known to the system
    -u  --uptime       Displays the /proc/uptime file and shows the uptime of the system
    -v  --version      Displays the /proc/version file and shows the kernal version
    -lp --ls-pids      Lists all the pids in /proc
    -w  --wireless     Displays the /proc/wireless file and shows the wireless interface data
    -mi --memory-info  Displays the /proc/meminfo file and shows the information about memory usage, both physical and swap.
    -nd --net-dev      Displays the /proc/net/dev file and shows the network devices and their statistics.
Sudo Required Commands:

    --pid-cmdline --pid-cl Gets the command line of the pid that you specifiy e.g pstat --pid-cl 100
    --pid-io Gets the io statisicts of the pid that you specifiy e.g pstat --pid-io 100
"""

commands="[-V -i -I -f -fm -m -M -p -u -v -lp -w -mi -nd --pid-cl --pid-io]"

if __name__ == "__main__":
    for arg in sys.argv:
        if arg == "-V" or arg == "--app-version":
            print(VERSION)
            exit()

        elif arg == "-i" or arg == "--cpuinfo":
            try:
                with open("/proc/cpuinfo","r") as f:
                    print(f.read())
                    f.close()
                exit()
            except FileNotFoundError:
                print("[Error 2] The file /proc/cpuinfo is missing from your system")

        elif arg == "-s" or arg == "--stat":
            try:
                with open("/proc/stat","r") as f:
                    print(f.read())
                    f.close()
                exit()
            except FileNotFoundError:
                print("[Error 2] The file /proc/stat is missing from your system")
        elif arg == "-I" or arg == "--interrupts":
            try:
                with open("/proc/","r") as f:
                    print(f.read())
                    f.close()
                exit()
            except FileNotFoundError:
                print("[Error 2] The file /proc/interrupts is missing from your system")
        elif arg == "-f" or arg == "--filesystems":
            try:
                with open("/proc/filesystems","r") as f:
                    print(f.read())
                    f.close()
                exit()
            except FileNotFoundError:
                print("[Error 2] The file /proc/filesystems is missing from your system")
        elif arg == "-fm" or arg == "--file-max":
            try:
                with open("/proc/sys/fs/file-max","r") as f:
                    print(f.read(), "bytes")
                    f.close()
                exit()
            except FileNotFoundError:
                print("[Error 2] The file /proc/sys/fs/file-max is missing from your system")
        elif arg == "-m" or arg == "--iomem":
            try:
                with open("/proc/iomem","r") as f:
                    print(f.read())
                    f.close()
                exit()
            except FileNotFoundError:
                print("[Error 2] The file /proc/iomem is missing from your system")
        elif arg == "-M" or arg == "--mounts":
            try:
                with open("/proc/mounts","r") as f:
                    print(f.read())
                    f.close()
                exit()
            except FileNotFoundError:
                print("[Error 2] The file /proc/iomem is missing from your system")
        elif arg == "-p" or arg == "--partitions":
            try:
                with open("/proc/partitions","r") as f:
                    print(f.read())
                    f.close()
                exit()
            except FileNotFoundError:
                print("[Error 2] The file /proc/partitions is missing from your system")
        elif arg == "-u" or arg == "--uptime":
            try:
                with open("/proc/uptime","r") as f:
                    print(f.read())
                    f.close()
                exit()
            except FileNotFoundError:
                print("[Error 2] The file /proc/uptime is missing from your system")
        elif arg == "-v" or arg == "--version":
            try:
                with open("/proc/version","r") as f:
                    print(f.read())
                    f.close()
                exit()
            except FileNotFoundError:
                print("[Error 2] The file /proc/version is missing from your system")
        elif arg == "-w" or arg == "--wireless":
            with open("/proc/net/wireless","r") as f:
                print(f.read())
                f.close()
            exit()

        elif arg == "-nd" or arg == "--net-dev":
            try:
                with open("/proc/net/dev","r") as f:
                    print(f.read())
                    f.close()
                exit()
            except FileNotFoundError:
                print("[Error 2] The file /proc/net/dev is missing from your system")        

        elif arg == "-mi" or arg == "--memory-info":
            try:
                with open("/proc/meminfo","r") as f:
                    print(f.read())
                    f.close()
                exit()
            except FileNotFoundError:
                print("[Error 2] The file /proc/meminfo is missing from your system")     

        elif arg == "-lp" or arg == "--ls-pids":
            for i in os.listdir("/proc"):
                if i.replace("_","").replace("-","").isalpha() == False:
                    print(i, end=" ")
            exit()

        elif arg == "--pid-cmdline" or arg == "--pid-cl":
            try:
                with open("/proc/"+sys.argv[sys.argv.index(arg)+1]+"/cmdline","r") as f:
                    print(f.read())
                    f.close()
            except PermissionError:
                print("Error reading the io file of "+sys.argv[sys.argv.index(arg)+1]+" try running with sudo")       
            exit()

        elif arg == "--pid-io":
            try:
                with open("/proc/"+sys.argv[sys.argv.index(arg)+1]+"/io","r") as f:
                    print(f.read())
                    f.close()
            except PermissionError:
                print("Error reading the io file of "+sys.argv[sys.argv.index(arg)+1]+" try running with sudo")
            exit()

        elif arg == "-h" or arg == "--help":
            print(help_msg)
            exit()
        

    print("Invalid/Unknown Command for help run -h or --help")
    print(commands)

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

commands="[-V -i -I -f -m -M -p -u -v -lp -w -mi -nd --pid-cl--pid-io]"

if __name__ == "__main__":
    for arg in sys.argv:
        if arg == "-V" or arg == "--app-version":
            print(VERSION)
            exit()

        elif arg == "-i" or arg == "--cpuinfo":
            with open("/proc/cpuinfo","r") as f:
                print(f.read())
                f.close()
            exit()

        elif arg == "-s" or arg == "--stat":
            with open("/proc/stat","r") as f:
                print(f.read())
                f.close()
            exit()

        elif arg == "-I" or arg == "--interrupts":
            with open("/proc/interrupts","r") as f:
                print(f.read())
                f.close()
            exit()

        elif arg == "-f" or arg == "--filesystems":
            with open("/proc/filesystems","r") as f:
                print(f.read())
                f.close()
            exit()

        elif arg == "-m" or arg == "--iomem":
            with open("/proc/iomem","r") as f:
                print(f.read())
                f.close()
            exit()

        elif arg == "-M" or arg == "--mounts":
            with open("/proc/mounts","r") as f:
                print(f.read())
                f.close()
            exit()

        elif arg == "-p" or arg == "--partitions":
            with open("/proc/partitions","r") as f:
                print(f.read())
                f.close()
            exit()

        elif arg == "-u" or arg == "--uptime":
            with open("/proc/uptime","r") as f:
                print(f.read())
                f.close()
            exit()

        elif arg == "-v" or arg == "--version":
            with open("/proc/version","r") as f:
                print(f.read())
                f.close()
            exit()

        elif arg == "-w" or arg == "--wireless":
            with open("/proc/net/wireless","r") as f:
                print(f.read())
                f.close()
            exit()

        elif arg == "-nd" or arg == "--net-dev":
            with open("/proc/net/dev","r") as f:
                print(f.read())
                f.close()
            exit()
        

        elif arg == "-mi" or arg == "--memory-info":
            with open("/proc/meminfo","r") as f:
                print(f.read())
                f.close()
            exit()

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

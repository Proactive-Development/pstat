#!/usr/bin/env python3
import os
import sys
import psutil

VERSION = 0.1

if __name__ == "__main__":
    for arg in sys.argv:

        if arg == "-V" or arg == "--app-version":
            print(VERSION)

        if arg == "-i" or arg == "--cpuinfo":
            with open("/proc/cpuinfo","r") as f:
                print(f.read())
                f.close()
       
        elif arg == "-s" or arg == "--stat":
            with open("/proc/stat","r") as f:
                print(f.read())
                f.close()
       
        elif arg == "-I" or arg == "--interrupts":
            with open("/proc/interrupts","r") as f:
                print(f.read())
                f.close()
        
        elif arg == "-f" or arg == "--filesystems":
            with open("/proc/filesystems","r") as f:
                print(f.read())
                f.close()
        
        elif arg == "-m" or arg == "--iomem":
            with open("/proc/iomem","r") as f:
                print(f.read())
                f.close()
       
        elif arg == "-M" or arg == "--mounts":
            with open("/proc/mounts","r") as f:
                print(f.read())
                f.close()
        
        elif arg == "-p" or arg == "--partitions":
            with open("/proc/partitions","r") as f:
                print(f.read())
                f.close()
        
        elif arg == "-u" or arg == "--uptime":
            with open("/proc/uptime","r") as f:
                print(f.read())
                f.close()
        
        elif arg == "-v" or arg == "--version":
            with open("/proc/version","r") as f:
                print(f.read())
                f.close()
        
        elif arg == "-w" or arg == "--wifi":
            with open("/proc/net/wireless","r") as f:
                print(f.read())
                f.close()

        elif arg == "-mi" or arg == "--memory":
            with open("/proc/meminfo","r") as f:
                print(f.read())
                f.close()
        
        elif arg == "-lp" or arg == "--ls-pids":
            for i in os.listdir("/proc"):
                if i.replace("_","").replace("-","").isalpha() == False:
                    print(i, end=" ")

        elif arg == "--pid-cmdline" or arg == "--pid-cl":
            try:
                with open("/proc/"+sys.argv[sys.argv.index(arg)+1]+"/cmdline","r") as f:
                    print(f.read())
                    f.close()
            except PermissionError:
                print("Error reading the io file of "+sys.argv[sys.argv.index(arg)+1]+" try running with sudo")       
        
        elif arg == "--pid-io":
            try:
                with open("/proc/"+sys.argv[sys.argv.index(arg)+1]+"/io","r") as f:
                    print(f.read())
                    f.close()
            except PermissionError:
                print("Error reading the io file of "+sys.argv[sys.argv.index(arg)+1]+" try running with sudo")
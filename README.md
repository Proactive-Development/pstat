# Pstat
<img src="https://raw.githubusercontent.com/Proactive-Development/Logos/main/Pstat/pstat%20logo.png" width=100>

A faster way to read proc info in linux

## Dependencies
- Psutil (Not used yet but will be implemented soon)

## Auto Installation

### Stable Install
```curl -fsSL https://files.proactive-dev.xyz/Git%20Projects/pstat/scripts/stableinstall.sh | bash -```

### Beta/Unstable Install
```curl -fsSL https://files.proactive-dev.xyz/Git%20Projects/pstat/scripts/betainstall.sh | bash -```


## Commands

### Standard Commands:
```
    -V  --app-version  Displays the current version of pstat
    -i  --cpuinfo      Displays the /proc/cpuinfo file and returns information about the processor, such as its type, make, model, and performance.
    -I  --interrupts   Displays the /proc/interrupts file and shows which interrupts are in use, and how many of each there have been.
    -f  --filesystems  Displays the /proc/filesystems file and shows filesystems configured/supported into/by the kernel.
    -fm  --file-max    Displays the /proc/sys/fs/file-max file and shows filesystem max storage size.
    -m  --iomem        Displays the /proc/iomem file and shows a memory map
    -M  --mounts       Displays the /proc/mounts file and shows what mounted filesystems are attached to the kernel
    -p  --partitions   Displays the /proc/partitions file and shows a table of partitions known to the system
    -u  --uptime       Displays the /proc/uptime file and shows the uptime of the system
    -v  --version      Displays the /proc/version file and shows the kernel version
    -lp --ls-pids      Lists all the pids in /proc
    -w  --wireless     Displays the /proc/wireless file and shows the wireless interface data
    -mi --memory-info  Displays the /proc/meminfo file and shows the information about memory usage, both physical and swap.    
```
### Sudo Required Commands:
```
    --pid-cmdline --pid-cl Gets the command line of the pid that you specifiy e.g pstat --pid-cl 100
    --pid-io Gets the io statisicts of the pid that you specifiy e.g pstat --pid-io 100
```

## Feature requests
If you have any feature requests, please open an issue on the [Github page](https://github.com/Proactive-Development/pstat/issues)

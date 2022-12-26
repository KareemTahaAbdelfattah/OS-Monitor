import psutil

print(psutil.pids()  )
pids = psutil.pids()
#p = psutil.Process( pids[3] )
#print(p)
print("|" +  ("-"*10 + "|" )*20 )
psutil.process_iter(attrs=None, ad_value=None)
def display():
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid
            ProcessStatus = proc.status();
            ProcessMemoryInfo = proc.memory_info
            print("Process ----> '", processName,"', Pid = ", processID, ", Status = '", ProcessStatus, "', Memory Info ----> ", ProcessMemoryInfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
display()


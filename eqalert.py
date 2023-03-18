import os
import time
import alert_dict

#log_path = "/home/callojoee/.wine/drive_c/Program Files (x86)/EverQuest/Logs/"

log_path = "./"

### Get the active toon by checking the current modified file ###
def get_active_toon():
    toon_logs = []
    os.chdir(log_path)
    files_list = os.listdir()
    for file in files_list:
        if file[:6] == 'eqlog_':
            toon_logs.append([file, os.stat(file).st_mtime])
    toon_logs = sorted(toon_logs,key=lambda l:l[1], reverse=True)
    toon = toon_logs[0][0]
    return toon

### Reads the last line of the log file ###
def read_log(log_loc):
    with open(log_loc, "rb") as f:
        first = f.readline()
        f.seek(-2, 2)
        while f.read(1) != b"\n":
            try:
                f.seek(-2, 1)
            except IOError:
                f.seek(-1, 1)
                if f.tell() == 0:
                    break
        last = f.readline()
    return last

### Main loop ###
while True:
    #time.sleep(0.05)

    ### Sleep at 3 seconds for testing
    time.sleep(3)
    os.system("clear")
    toon = get_active_toon()
    ### Get file size - Part of my idea
    file_size = os.path.getsize(log_path + toon)
    last_line = read_log(log_path + toon)
    last_line = last_line.strip()
    last_line = last_line.decode()
    
    ### Added for debugging
    print(os.path.getsize(log_path + toon)) 
    
    ### This was my idea. Trying to figure it out!
    if os.path.getsize(log_path + toon) > file_size:
    #if file_size < (os.path.getsize(log_path + toon)):
    #if file_size != (os.path.getsize(log_path + toon)):
    #if os.path.getsize(log_path + toon) != file_size:
        for k in alert_dict.alerts:
            if k in last_line:
                os.system(alert_dict.alerts.get(k))
                break;

    print(f'''

    Tell Me! 
    ==============================================================
     File Size {file_size}
     Toon: {toon[6:-16]} 
    ==============================================================
            ''')

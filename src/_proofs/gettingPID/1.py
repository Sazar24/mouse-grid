import psutil
from time import sleep

PROCNAME = r"\\.\DISPLAY2"
knowPID = 29128

x = ""
# found = ""
for proc in psutil.process_iter():
    try:
        # if PROCNAME in proc.title :
        #     print("!!!!!!!!!")
        #     print(proc)
        #     found = proc
        # sleep(2)
        # print(proc)
        if proc.pid == knowPID:
            found = proc
            x = proc
            break
    except:
        print("dupa")
        # sleep(1)

print(dir(x))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_create_time', '_exe', '_exitcode', '_gone', '_hash', '_ident', '_init', '_last_proc_cpu_times', '_last_sys_cpu_times', '_lock', '_name', '_pid', '_ppid', '_proc', 'as_dict', 'children', 'cmdline', 'connections', 'cpu_affinity', 'cpu_percent', 'cpu_times', 'create_time', 'cwd', 'environ', 'exe', 'io_counters', 'ionice', 'is_running', 'kill', 'memory_full_info', 'memory_info', 'memory_info_ex', 'memory_maps', 'memory_percent', 'name', 'nice', 'num_ctx_switches', 'num_handles', 'num_threads', 'oneshot', 'open_files', 'parent', 'parents', 'pid', 'ppid', 'resume', 'send_signal', 'status', 'suspend', 'terminate', 'threads', 'username', 'wait']
# print(doc(x))

print("found:")
print(found)
print(found.name)
print(found.pid)

print(found.username())
print(found.parent())
print(found.cwd())
print(found.cwd())
print(found.cwd())
print(found.cwd())

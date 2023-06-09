import gdb
enable_syscall_trace = True
syscalls = ['mmap', 'read', 'write', 'brk', 'open', 'mprotect']
syscall_str = ' '.join(syscalls)
sym = []
def stop_handler(stopEvent):
    global sym
    sym_ = gdb.execute("info symbol $rip",to_string=True)
    mapp = gdb.execute("xinfo $rip",to_string=True)
    mapp = mapp[mapp.find('mapping:'):mapp.find('Offset info')].split()[-1]
    if 'No symbol' not in sym_:
        tar = sym_[:sym_.find(' ')]
        if sym[-1] != tar:
            sym.append(tar)
    if 'linux-gnu' in mapp or 'vdso' in mapp:
        gdb.execute("fin")

if 'call ' in gdb.execute("x/xi $rip",to_string=True):
    next = gdb.execute("x/2xi $rip",to_string=True)
    next = next[next.find("\n"):]
    next = next[next.find('0x'):next.find(':')]
    print("TRACE")
    if enable_syscall_trace:
        gdb.execute(f"catch syscall {syscall_str}")
    a = gdb.execute("info symbol $rip",to_string=True)
    if "No symbol" in a:
        sym.append("START_TRACE")
    else:
        sym.append(a[:a.find(' ')])
    gdb.execute("si")
    gdb.events.stop.connect(stop_handler)
    while str(gdb.parse_and_eval("$rip")) != next:
        gdb.execute("si")
    gdb.events.stop.disconnect(stop_handler)
    c = 0
    flag = {x : -1 for x in set(sym)}
    for i,j in enumerate(sym):
        if '_dl_runtime_resolve' in j:
            flag[j]=-1
        if flag[j]==-1:
            flag[j] =c
        elif flag[j] != -1:
            c = flag[j]
        tmp = '  ' * c + j
        print(f"{i : <3} | {tmp}")
        c += 1
else:
    print("OPCODE != call")
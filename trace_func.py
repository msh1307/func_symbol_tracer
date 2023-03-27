import gdb
next = gdb.execute("x/2xi $rip",to_string=True)
next = next[next.find("\n"):]
next = next[next.find('0x'):next.find(':')]
if 'call ' in gdb.execute("x/xi $rip",to_string=True):
    print("TRACE")
    sym = ['START_TRACE']
    gdb.execute("si")
    while str(gdb.parse_and_eval("$rip")) != next:
        sym_ = gdb.execute("info symbol $rip",to_string=True)
        last = 0
        if 'No symbol' not in sym_:
            tar = sym_[:sym_.find(' ')]
            if sym[-1] != tar:
                sym.append(tar)
        mapp = gdb.execute("xinfo $rip",to_string=True)
        mapp = mapp[mapp.find('mapping:'):mapp.find('Offset info')].split()[-1]
        if 'linux-gnu' in mapp or 'vdso' in mapp:
            gdb.execute("fin")
        gdb.execute("si")

    for i,j in enumerate(sym):
        print(f"{i : <3} | {j}")
else:
    print("OPCODE != call")
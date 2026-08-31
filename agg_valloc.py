import re, csv

dll_total = {}
sys_modules = {
    'ntdll','kernel32','kernelbase','ntoskrnl','wow64','wow64cpu','hal',
    'user32','gdi32','gdi32full','combase','rpcrt4','ole32','oleaut32',
    'shell32','advapi32','msvcrt','ucrtbase','vcruntime','bcrypt',
    'bcryptprimitives','sechost','crypt32','wintrust','setupapi',
    'cfgmgr32','devobj','imm32','msctf','uxtheme','dwmapi','propsys',
    'twinapi','shlwapi','dcomp','coremessaging','coreui','umpdc',
    'textinputframework','winmm','ws2_32','iphlpapi','nsi','dnsapi',
    'fwpuclnt','mswsock','audioses','mmdevapi','d3d10warp','d3d12',
    'd3d12core','d3d','dxgi','dxilconv','drvstore','spinf','clbcatq',
    'profapi','winhttp','winspool','version','oleacc','hid',
    'twinapi.appcore','windows.storage','textinput',
    'cryptsp','ncrypt','fltlib','cryptbase','dbghelp',
}

with open('mem_raw.txt', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        if len(row) < 8: continue
        stack = row[2]
        if not stack: continue
        try:
            size_mb = float(row[7])
        except (ValueError, IndexError):
            continue
        if size_mb <= 0: continue

        found = False
        for m in re.finditer(r'([\w._-]+)\.dll!', stack):
            dll = m.group(1).lower()
            if dll not in sys_modules:
                dll_total[dll] = dll_total.get(dll, 0) + size_mb
                found = True
                break
        if not found:
            dll_total['<unresolved/system>'] = dll_total.get('<unresolved/system>', 0) + size_mb

print("=== VirtualAlloc Impacting Size by DLL ===\n")
total = sum(dll_total.values())
for dll, size in sorted(dll_total.items(), key=lambda x: -x[1]):
    pct = size / total * 100 if total > 0 else 0
    print(f"  {size:8.1f} MB  ({pct:5.1f}%)  {dll}")
print(f"\n  {'─'*45}")
print(f"  {total:8.1f} MB  total")

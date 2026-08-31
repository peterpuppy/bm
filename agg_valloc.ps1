$data = Get-Content "mem_raw.txt" | Select-Object -Skip 1
$dllTotal = @{}
foreach ($line in $data) {
    if (-not $line) { continue }
    $cols = $line -split '\t'
    if ($cols.Count -lt 2) { continue }
    [double]$size = 0
    if ([double]::TryParse($cols[0], [ref]$size) -and $size -gt 0) {
        $stackCol = if ($cols.Count -ge 5) { $cols[4] } else { $cols[$cols.Count-1] }
        $matches = [regex]::Matches($stackCol, '([\w._-]+\.dll)!')
        $found = $false
        foreach ($m in $matches) {
            $dll = $m.Groups[1].Value.ToLower()
            if ($dll -match '^(ntdll|kernel32|kernelbase|ntoskrnl|wow64|user32|gdi32|combase|rpcrt4|ole32|shell32|advapi32|msvcrt|ucrtbase|bcrypt|sechost|crypt32|wintrust|setupapi|cfgmgr32|devobj|imm32|msctf|uxtheme|dwmapi|propsys|twinapi|shlwapi|dcomp|coremessaging|coreui|umpdc|textinput|winmm|ws2_32|iphlpapi|nsi|dnsapi|mswsock|audioses|mmdevapi|d3d10warp|d3d12core|d3d12|d3d|dxgi|dxilconv|drvstore|spinf|clbcatq|oleaut32|profapi)$') { continue }
            $dllTotal[$dll] = ($dllTotal[$dll] + $size)
            $found = $true
            break
        }
        if (-not $found) {
            $dllTotal['<unresolved>'] = ($dllTotal['<unresolved>'] + $size)
        }
    }
}
"=== VirtualAlloc Outstanding by DLL ==="
$dllTotal.GetEnumerator() | Sort-Object Value -Descending | Select-Object -First 30 | ForEach-Object {
    "{0,8:N1} MB  {1}" -f ($_.Value, $_.Key)
}

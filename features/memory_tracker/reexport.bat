@echo off
REM Re-run the WPR analyzer over every raw\<scenario>\data.txt and regenerate the
REM wpr_*.txt/csv reports in place. Run after the analyzer changes, or after
REM capturing new data into a raw\<scenario>\ folder.
setlocal
cd /d "%~dp0"

REM memory_analyzer lives next to this workbench:  E:\code\memory_analyzer
set "ANALYZER=%~dp0..\..\..\memory_analyzer\wpr.py"
if not exist "%ANALYZER%" (
    echo Analyzer not found: %ANALYZER%
    echo Expected memory_analyzer at E:\code\memory_analyzer -- edit ANALYZER in this script if it moved.
    exit /b 1
)

for /d %%D in ("%~dp0raw\*") do (
    if exist "%%D\data.txt" (
        echo === %%~nxD ===
        python "%ANALYZER%" "%%D\data.txt" --out "%%D"
        echo.
    ) else (
        echo --- skip %%~nxD ^(no data.txt^) ---
    )
)

echo Done. Reports regenerated in each raw\^<scenario^>\ folder.
endlocal

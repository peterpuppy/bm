@echo off
REM One-shot test: analyze the bundled sample CSV and print + write a report.
REM Run by double-clicking, or `test.bat` from a terminal.
setlocal
cd /d "%~dp0"

python wpr.py testdata\sample.csv --out testdata\report
if errorlevel 1 (
    echo.
    echo FAILED -- is Python on PATH?  Try:  py wpr.py testdata\sample.csv --out testdata\report
    exit /b 1
)

echo.
echo ============================================================
type testdata\report\wpr_summary.txt
echo.
echo Report files written to: %~dp0testdata\report
endlocal

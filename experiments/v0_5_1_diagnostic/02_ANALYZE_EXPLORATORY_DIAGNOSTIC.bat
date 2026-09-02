@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 analyze_diagnostic_v0_5_1.py
) else (
  python analyze_diagnostic_v0_5_1.py
)
pause

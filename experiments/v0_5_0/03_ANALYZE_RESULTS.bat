@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 analyze_v0_5_0.py
) else (
  python analyze_v0_5_0.py
)
pause

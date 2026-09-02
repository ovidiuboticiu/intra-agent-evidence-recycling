@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 run_diagnostic_v0_5_1.py verify
) else (
  python run_diagnostic_v0_5_1.py verify
)
pause


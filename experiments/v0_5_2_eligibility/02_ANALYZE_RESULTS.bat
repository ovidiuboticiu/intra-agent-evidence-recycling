@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
    py -3 analyze_eligibility_v0_5_2.py
) else (
    python analyze_eligibility_v0_5_2.py
)
pause

@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 run_experiment_v0_5_0.py verify
) else (
  python run_experiment_v0_5_0.py verify
)
pause

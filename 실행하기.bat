@echo off
chcp 65001 > nul

echo ==================================
echo   Automation Tool 실행중...
echo ==================================

cd /d %~dp0

python -m app.main

if %errorlevel% neq 0 (
    echo [ERROR] 실행 실패
    pause
    exit /b
)

echo ==================================
echo   완료!
echo ==================================
pause
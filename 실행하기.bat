@echo off
chcp 65001 > nul

cd /d %~dp0

REM ==================================
REM Virtual Environment Activate
REM ==================================

if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
) else (
    echo [ERROR] .venv 가 존재하지 않습니다.
    pause
    exit /b
)

echo ==================================
echo   Automation Tool 실행중...
echo ==================================

python -m app.runner

if %errorlevel% neq 0 (
    echo [ERROR] 실행 실패
    pause
    exit /b
)

echo ==================================
echo   완료!
echo ==================================
pause
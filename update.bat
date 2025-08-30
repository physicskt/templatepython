chcp 65001 >nul
@echo off
echo updating software...

git stash
git pull
call setup.bat

pause
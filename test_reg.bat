@echo off
echo Starting Huorong registry rule tests...

rem Enable delayed expansion for errorlevel in loops
setlocal enabledelayedexpansion

rem Enable ANSI color codes
for /f %%A in ('echo prompt $E ^| cmd') do set "ESC=%%A"

rem Check if HKEY_CLASSES_ROOT\test already exists
reg query "HKEY_CLASSES_ROOT\test" >nul 2>&1
if %errorlevel% equ 0 (
    echo HKCR\test already exist, please backup
    echo press any key to exit
    pause >nul
    exit /b 1
)

rem Initialize first by running init.py
echo Initializing...
python hr_test_reg\init.py
if %errorlevel% neq 0 (
    echo Failed to initialize
    exit /b %errorlevel%
)

rem Import profile2.reg for tests 1-2
echo Importing profile2.reg...
reg import hr_test_reg\profile2.reg
if %errorlevel% neq 0 (
    echo Failed to import profile2.reg
    exit /b %errorlevel%
)

rem Run tests 1-2
for /L %%i in (1, 1, 2) do (
    echo !ESC![92m=============== TEST %%i ===============!ESC![0m
    python hr_test_reg\%%i.py
    if !errorlevel! neq 0 (
        echo Test %%i failed with error code !errorlevel!
    )
    echo.
)

rem Import profile2.reg again for test 3
echo Importing profile2.reg again...
reg import hr_test_reg\profile2.reg
if %errorlevel% neq 0 (
    echo Failed to import profile2.reg
    exit /b %errorlevel%
)

rem Run test 3
echo !ESC![92m=============== TEST 3 ===============!ESC![0m
python hr_test_reg\3.py
if %errorlevel% neq 0 (
    echo Test 3 failed with error code %errorlevel%
)
echo.

rem Import profile1.reg
echo Importing profile1.reg...
reg import hr_test_reg\profile1.reg
if %errorlevel% neq 0 (
    echo Failed to import profile1.reg
    exit /b %errorlevel%
)

rem Run tests 4-13 in sequence (updated range)
for /L %%i in (4, 1, 13) do (
    echo !ESC![92m=============== TEST %%i ===============!ESC![0m
    python hr_test_reg\%%i.py
    if !errorlevel! neq 0 (
        echo Test %%i failed with error code !errorlevel!
    )
    echo.
)

rem Import profile3.reg
echo Importing profile3.reg...
reg import hr_test_reg\profile3.reg
if %errorlevel% neq 0 (
    echo Failed to import profile3.reg
    exit /b %errorlevel%
)

rem Run test 14 (updated from 13)
echo !ESC![92m=============== TEST 14 ===============!ESC![0m
python hr_test_reg\14.py
if %errorlevel% neq 0 (
    echo Test 14 failed with error code %errorlevel%
)
echo.

rem Import profile1.reg again
echo Importing profile1.reg again...
reg import hr_test_reg\profile1.reg
if %errorlevel% neq 0 (
    echo Failed to import profile1.reg
    exit /b %errorlevel%
)

rem Run tests 15-16 (updated from 14-15)
for /L %%i in (15, 1, 16) do (
    echo !ESC![92m=============== TEST %%i ===============!ESC![0m
    python hr_test_reg\%%i.py
    if !errorlevel! neq 0 (
        echo Test %%i failed with error code !errorlevel!
    )
    echo.
)

echo All tests completed.

rem Import profile0.reg
echo Importing profile0.reg
reg import hr_test_reg\profile0.reg
if %errorlevel% neq 0 (
    echo Failed to import profile0.reg
    exit /b %errorlevel%
)


rem Parse and display test results
echo.
echo Parsing test results...
python hr_test_reg\parse_result.py

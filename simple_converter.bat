@echo off
title Image Converter - Simple Mode
color 0A

:menu
cls
echo ====================================
echo    IMAGE CONVERTER - Simple Mode
echo ====================================
echo.
echo This tool works without right-click menu!
echo.
echo [1] Convert single image
echo [2] Convert all images in a folder
echo [3] Exit
echo.
set /p choice="Select option (1-3): "

if "%choice%"=="1" goto single
if "%choice%"=="2" goto folder
if "%choice%"=="3" goto end
goto menu

:single
cls
echo ====================================
echo    Convert Single Image
echo ====================================
echo.
set /p file="Drag and drop an image file here and press Enter: "

REM Remove quotes
set file=%file:"=%

if not exist "%file%" (
    echo.
    echo ERROR: File not found!
    pause
    goto menu
)

echo.
echo Select output format:
echo [1] JPG (High Quality 95%%)
echo [2] JPG (Normal 85%%)
echo [3] PNG
echo [4] WebP
echo.
set /p format="Select format (1-4): "

set "SCRIPT_DIR=%~dp0"
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

if "%format%"=="1" (
    python "%SCRIPT_DIR%\convert_image.py" -f jpg -q 95 "%file%"
) else if "%format%"=="2" (
    python "%SCRIPT_DIR%\convert_image.py" -f jpg -q 85 "%file%"
) else if "%format%"=="3" (
    python "%SCRIPT_DIR%\convert_image.py" -f png -q 95 "%file%"
) else if "%format%"=="4" (
    python "%SCRIPT_DIR%\convert_image.py" -f webp -q 90 "%file%"
) else (
    echo Invalid choice!
    pause
    goto menu
)

echo.
echo ====================================
echo Conversion complete!
echo ====================================
echo.
timeout /t 2 /nobreak >nul
goto menu

:folder
cls
echo ====================================
echo    Convert All Images in Folder
echo ====================================
echo.
set /p folder="Drag and drop a folder here and press Enter: "

REM Remove quotes
set folder=%folder:"=%

if not exist "%folder%" (
    echo.
    echo ERROR: Folder not found!
    timeout /t 2 /nobreak >nul
    goto menu
)

echo.
echo Select output format:
echo [1] JPG (High Quality 95%%)
echo [2] JPG (Normal 85%%)
echo [3] PNG
echo [4] WebP
echo.
set /p format="Select format (1-4): "

set "SCRIPT_DIR=%~dp0"
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

echo.
echo Converting all images in folder...
echo.

if "%format%"=="1" (
    for %%f in ("%folder%\*.webp" "%folder%\*.png" "%folder%\*.jpg" "%folder%\*.jpeg" "%folder%\*.bmp" "%folder%\*.gif" "%folder%\*.tiff" "%folder%\*.avif" "%folder%\*.heic") do (
        if exist "%%f" python "%SCRIPT_DIR%\convert_image.py" -f jpg -q 95 "%%f"
    )
) else if "%format%"=="2" (
    for %%f in ("%folder%\*.webp" "%folder%\*.png" "%folder%\*.jpg" "%folder%\*.jpeg" "%folder%\*.bmp" "%folder%\*.gif" "%folder%\*.tiff" "%folder%\*.avif" "%folder%\*.heic") do (
        if exist "%%f" python "%SCRIPT_DIR%\convert_image.py" -f jpg -q 85 "%%f"
    )
) else if "%format%"=="3" (
    for %%f in ("%folder%\*.webp" "%folder%\*.png" "%folder%\*.jpg" "%folder%\*.jpeg" "%folder%\*.bmp" "%folder%\*.gif" "%folder%\*.tiff" "%folder%\*.avif" "%folder%\*.heic") do (
        if exist "%%f" python "%SCRIPT_DIR%\convert_image.py" -f png -q 95 "%%f"
    )
) else if "%format%"=="4" (
    for %%f in ("%folder%\*.webp" "%folder%\*.png" "%folder%\*.jpg" "%folder%\*.jpeg" "%folder%\*.bmp" "%folder%\*.gif" "%folder%\*.tiff" "%folder%\*.avif" "%folder%\*.heic") do (
        if exist "%%f" python "%SCRIPT_DIR%\convert_image.py" -f webp -q 90 "%%f"
    )
) else (
    echo Invalid choice!
    timeout /t 2 /nobreak >nul
    goto menu
)

echo.
echo ====================================
echo Conversion complete!
echo ====================================
echo.
timeout /t 2 /nobreak >nul
goto menu

:end
exit

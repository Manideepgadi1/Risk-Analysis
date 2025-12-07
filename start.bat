@echo off
echo Starting Riskometer Application...
echo.
echo Installing dependencies (if needed)...
D:\Riskometer\.venv-1\Scripts\python.exe -m pip install -q -r requirements.txt

echo.
echo Starting FastAPI server...
echo Server will be available at: http://localhost:8000
echo.
echo Press CTRL+C to stop the server
echo.

D:\Riskometer\.venv-1\Scripts\python.exe main.py

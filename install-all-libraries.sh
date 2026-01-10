# Upgrade pip first
Write-Host "Upgrading pip..."
python -m pip install --upgrade pip
Write-Host "Pip upgraded successfully!"

# Install required libraries
pip install pandas qrcode xlrd openpyxl

Write-Host "All libraries installed successfully!"

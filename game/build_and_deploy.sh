#!/bin/bash

# Step 1: Create the executable using PyInstaller
echo "Creating executable..."
docker run --rm -v "$PWD":/app -w /app python:3.9-slim bash -c "
pip install --no-cache-dir pyinstaller &&
pyinstaller --onefile tictactoe_game.py"

# Step 2: Upload the executable to S3
echo "Uploading executable to S3..."
aws s3 cp dist/tictactoe_game.exe s3://builddb/tictactoe-executable.exe

echo "Deployment complete!"

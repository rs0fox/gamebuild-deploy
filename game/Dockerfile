# Use a base Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir pyinstaller

# Bundle app source and create an executable
RUN pyinstaller --onefile tictactoe_game.py

# Command to run the executable
CMD ["dist/tictactoe_game"]

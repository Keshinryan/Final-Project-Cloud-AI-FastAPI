# Use Python 3.9 as the base image
FROM python:3.9 

# Create a user and set environment variables
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Set the working directory
WORKDIR $HOME/app

# Copy dependencies and install them
COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application files
COPY --chown=user . $HOME/app

# Run FastAPI on port 7860 and start Gradio
CMD uvicorn app:app --host 0.0.0.0 --port 7860 

FROM python:3.12-slim

WORKDIR /app

# Copy automation project
COPY automation_manager ./automation_manager

# Install dependencies
COPY automation_manager/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Default region (can be overridden by -e AWS_DEFAULT_REGION=...)
ENV AWS_DEFAULT_REGION=ap-southeast-2

# Run as a module so that relative imports (from .utils ...) work
CMD ["python", "-m", "automation_manager.main"]
README.md
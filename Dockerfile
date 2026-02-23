FROM python:3.13-slim

WORKDIR /app

# installing packages / dependencies
COPY requirements.txt ./app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# COPY ./src ./app/src
# COPY ./README.md ./app/
COPY . .

EXPOSE 8000

# Run the module
CMD ["python", "-m", "src.main"]
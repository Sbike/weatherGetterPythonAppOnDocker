# Base image
FROM python:3.9-slim

#working directory
WORKDIR /app

## we copy the script into the container
COPY weatherGetterPython.py . 


# Installing python dependencies
RUN pip install requests

# Runing the weather getter script
CMD ["python", "./weatherGetterPython.py"]

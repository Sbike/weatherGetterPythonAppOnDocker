# Weather App

This repository contains a Dockerized Python application that fetches weather information for a specified city using the WeatherAPI.com API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker installed on your machine.
- An API key from WeatherAPI.com. (Free for 14 days, accessible on https://www.weatherapi.com/docs/)

### Installing

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Sbike/weatherGetterPythonAppOnDocker.git
   
   cd weatherGetterPythonAppOnDocker
   ```

2. **Build the Docker Image**

    Build the Docker image :

    ```bash
    docker build -t yourusername/weather-app . #Replace yourusername with your Docker Hub username
    ```
    Run the Container

    ```bash
    docker run -it yourusername/weather-app
    ```
    Follow the prompts in the application to test it.

3. **Push the Image to Docker Hub (optional for sharing with someone)**

    First, log in to Docker Hub:
    ```bash
    docker login
    ```
    Then push the image:
    ```bash
    docker push yourusername/weather-app
    ```

4. **Running the tests**
    
    Ask someone else to pull your Docker image and run it on their machine to verify it works correctly with the command:
    
    ```bash
    docker run -it yourusername/weather-app
    ```

## Faster Use
For a faster use, you can directly pull my image from https://hub.docker.com/r/leroyhubert/weather-app using the command 

```bash
docker pull leroyhubert/weather-app
```
and run it with 
```bash
docker run -it leroyhubert/weather-app
```

## Authors

Hubert Leroy - Initial work - https://github.com/Sbike

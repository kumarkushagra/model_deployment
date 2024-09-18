# Chat with an Open-Source LLM

This project allows you to chat with a pre-trained LLM using a web interface.

## How to Run Locally

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. Go to `http://localhost:5000` to interact with the model.

## Docker

To run the project using Docker:

1. Build the Docker image: `docker build -t llm-app .`
2. Run the Docker container: `docker run -p 5000:5000 llm-app`

## Deploy on Railway

- Link this repository with Railway.app and deploy.

# ML Engineer's Test Assignment Alindor

This project aims to provide a web interface for users to upload audio files containing dialogues between at least two speakers. The system then utilizes Deepgram API for speech-to-text conversion to extract the transcript from the audio. The transcript is then analyzed for sentiment and psychological insights using the OpenAI API. The output is presented to the user through the web interface.

## Features

- User-friendly web interface for uploading audio files.
- Integration with Deepgram API for speech-to-text conversion.
- Utilization of OpenAI API for sentiment and psychological analysis.
- Scalable processing using a AWS cloud engine and Fast API development.
- Creativity in sentiment analysis to provide multiple insightful outputs.

## How to Run

1. Clone the repository from GitHub:

```bash
git clone <repository_url>
cd <repository_name>
```

2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

3. Set up Deepgram API credentials:

    - Obtain Deepgram API credentials and add them to the `.env` file.

4. Set up OpenAI API credentials:

    - Sign up for the OpenAI API and obtain API key.
    - Add the API key to the `.env` file.

5. Run the FastAPI server:

```bash
uvicorn genai_api.api.api_fastapi:app --port 8008 --reload
```

6. Access the web interface by navigating to `http://localhost:8008` in your web browser.

## Folder Structure

- `AssignmentAlindor/`: Root directory for the project. 
   - `genai_api/`: Directory containing all the files.
        - `api/`: Directory containing API files.
            - `api_fastapi.py`: FastAPI application for handling web requests.
            - `DeepAI.py`: Module for interfacing with DeepAI API.
        - `models/`: Directory containing model files.
            - `generative_llm.py`: Module for utilizing the OpenAI API.
        - `prompts/`: Directory containing prompt files.
            - `prompts.py`: Module containing specialized prompts for sentiment analysis.
        - `templates/`: Directory containing HTML templates for the web interface.
            - `index.html`: HTML template for the web interface.
   - `Dockerfile`: Docker configuration for containerization.
   - `requirements.txt`: List of Python dependencies.
   - `.env`: Configuration file for API credentials.

## Usage

1. Access the web interface.
2. Upload an audio file containing dialogue between at least two speakers. The audio file can be in the form of `.mp3` or `.wav`.
3. Wait for the analysis to complete.
4. View the sentiment and psychological insights derived from the conversation.

## Deployment on AWS

To deploy the service on AWS, I performed the following steps:

1. Pushed the Docker image to Amazon Elastic Container Registry (ECR):
   
   - Created a repository in AWS ECR with the name "api".
   - Configured my AWS credentials locally.
   - Executed docker tag and docker push commands.

```bash
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account_id>.dkr.ecr.<region>.amazonaws.com
docker tag <image_name>:<tag> <account_id>.dkr.ecr.<region>.amazonaws.com/<repository_name>:<tag>
docker push <account_id>.dkr.ecr.<region>.amazonaws.com/<repository_name>:<tag>
```

2. Launched an EC2 instance:

    - Chose an instance type suitable for my application.
    - Configured security groups to allow inbound traffic on port 8008.
   

3. Logged into the EC2 instance locally and pulled the Docker image from ECR:

```bash
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account_id>.dkr.ecr.<region>.amazonaws.com
docker pull <account_id>.dkr.ecr.<region>.amazonaws.com/<repository_name>:<tag>
```

4. Ran the Docker container on the EC2 instance:

```bash
docker run -it -p 8008:8008 <account_id>.dkr.ecr.<region>.amazonaws.com/<repository_name>:<tag>
```

5. Accessed the web interface by navigating to Public IPv4 DNS URL `http://ec2-23-20-20-249.compute-1.amazonaws.com:8008/` in web browser.


## Testing with cURL Request and URL

Below is the URL and cURL request provided to test the service.

1. **Testing via web user interface:**

```commandline
http://ec2-23-20-20-249.compute-1.amazonaws.com:8008/
```

```bash
curl -X 'POST' \
  'http://ec2-23-20-20-249.compute-1.amazonaws.com:8008/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'input_audio=@<path_to_audio_file>'
```

2. **Testing via FastAPI UI:**

```commandline
http://ec2-23-20-20-249.compute-1.amazonaws.com:8008/docs
```

```bash
curl -X 'POST' \
  'http://ec2-23-20-20-249.compute-1.amazonaws.com:8008/upload_file' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'input_audio=@<path_to_audio_file>'
```

Replace `<path_to_audio_file>` with the path of the audio file you want to analyze.


## Contact

For any inquiries or issues, please contact at `8897285347vinaykumar@gmail.com`.

## Note

This project is developed as a test assignment for Alindor Corp.
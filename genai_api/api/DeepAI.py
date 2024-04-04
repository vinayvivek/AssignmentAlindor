import os
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
)
from dotenv import load_dotenv

load_dotenv()


def speech_to_text(input_audio):
    DeepAI_api_key = os.getenv("DEEPAI_API_KEY")
    deepgram = DeepgramClient(DeepAI_api_key)
    payload: FileSource = {
        "buffer": input_audio,
    }
    options = PrerecordedOptions(
        model="nova-2",
        smart_format=True,
    )

    response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
    transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]
    return transcript



from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import whisper
class TranscriptionInput(BaseModel):
    file_path: str = Field(..., description="Path to the video/audio file")

class TranscriptionTool(BaseTool):
    name: str = "Transcription Tool"
    description: str = (
        "A tool that transcribes audio and video files into text using OpenAI's Whisper."
    )
    args_schema: Type[BaseModel] = TranscriptionInput 

    def _run(self, file_path: str) -> str:
        model = whisper.load_model("base")
        result = model.transcribe(file_path)
        return result['text']
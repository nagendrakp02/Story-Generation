from typing import TypedDict, Optional
from pydantic import BaseModel, Field

class Story(BaseModel):
    title: str = Field(description="Title of the story")
    content: str = Field(description="Content of the story")

class StoryState(TypedDict, total=False):
    topic: str
    story: Story
    current_language: Optional[str]

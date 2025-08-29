from src.states.storystate import StoryState, Story
from langchain_core.messages import HumanMessage

class StoryNode:
    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state: StoryState):
        if "topic" in state and state["topic"]:
            prompt = f"""
            You are a creative storyteller. 
            Generate a **unique and engaging story title** for the topic: {state['topic']}.
            """
            response = self.llm.invoke(prompt)
            return {"story": Story(title=response.content, content="")}

    def content_generation(self, state: StoryState):
        if "topic" in state and state["topic"]:
            prompt = f"""
            You are a professional story writer.
            Write a **detailed, engaging story** based on the topic: {state['topic']}.
            Use chapters or sections where appropriate.
            Make it vivid, emotional, and captivating.
            """
            response = self.llm.invoke(prompt)
            story = state["story"]
            return {"story": Story(title=story.title, content=response.content)}

    def translation(self, state: StoryState):
        story = state["story"]
        target_lang = state.get("current_language", "english")
        prompt = f"""
        Translate the following story into {target_lang}.
        Keep the storytelling style intact.

        Title: {story.title}

        Story:
        {story.content}
        """
        messages = [HumanMessage(content=prompt)]
        response = self.llm.invoke(messages)
        return {"story": Story(title=story.title, content=response.content)}

    def route(self, state: StoryState):
        return {"current_language": state["current_language"]}

    def route_decision(self, state: StoryState):
        lang = state.get("current_language", "").lower()
        if lang == "hindi":
            return "hindi"
        elif lang == "french":
            return "french"
        return None

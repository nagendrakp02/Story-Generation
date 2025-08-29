from langgraph.graph import StateGraph, START, END
from src.states.storystate import StoryState
from src.nodes.story_node import StoryNode

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(StoryState)

    def build_topic_graph(self):
        node = StoryNode(self.llm)
        self.graph.add_node("title_creation", node.title_creation)
        self.graph.add_node("content_generation", node.content_generation)
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)
        return self.graph

    def build_language_graph(self):
        node = StoryNode(self.llm)
        self.graph.add_node("title_creation", node.title_creation)
        self.graph.add_node("content_generation", node.content_generation)
        self.graph.add_node("hindi_translation", lambda s: node.translation({**s, "current_language": "hindi"}))
        self.graph.add_node("french_translation", lambda s: node.translation({**s, "current_language": "french"}))
        self.graph.add_node("route", node.route)

        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", "route")

        self.graph.add_conditional_edges(
            "route",
            node.route_decision,
            {
                "hindi": "hindi_translation",
                "french": "french_translation"
            }
        )
        self.graph.add_edge("hindi_translation", END)
        self.graph.add_edge("french_translation", END)
        return self.graph

    def setup_graph(self, usecase):
        if usecase == "topic":
            self.build_topic_graph()
        elif usecase == "language":
            self.build_language_graph()
        return self.graph.compile()

from collections import deque


class ConversationMemory:
    def __init__(self, max_memory=5):
        self.chat_history = deque(maxlen=max_memory)

    def add_interaction(self, user_input, assistant_response):
        self.chat_history.append((user_input, assistant_response))

    def get_memory_context(self):
        memory = ""
        for user_input, response in self.chat_history:
            memory += f"User: {user_input}\nAssistant: {response}\n"
        return memory.strip()

from src.app import App


class Tool(App):
    def __init__(self, name: str, **app_data):
        super().__init__(name=name, **app_data)


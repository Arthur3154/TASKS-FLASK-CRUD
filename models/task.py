class Task:
    def __init__(self, id, title, description, completed=False) -> None:
        self.id = id 
        self.title = title
        self.description = description
        self.completed = completed

        def to__dict(self):
            return {
                "id": self.id,
                "title": self.title,
                "description": self.description,
                "complrtrd": self.completed
            }
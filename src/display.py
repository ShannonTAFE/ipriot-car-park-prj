class Display:

    def __init__(self, id, message="",is_on=False):
        self.id = id
        self.message = message
        self.is_on = is_on


    def __str__(self):
        return f"{self.id}: Display is {"on" if self.is_on else "off"}"
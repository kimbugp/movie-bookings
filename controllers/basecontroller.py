from utils import NotFound


class BaseController:
    data = {}
    id = 0

    def __init__(self, data=None):
        self.new = data

    def save(self):
        id = self.id_generator()
        self.data[id] = self.new
        return self.data[id]

    def get(self, id):
        todo = self.data.get(id, None)
        if todo:
            return todo
        raise NotFound()

    def update(self, id, data):
        self.get(id)
        self.data[id] = data
        return data

    def delete(self, id):
        todo = self.data.pop(id, None)
        if todo:
            return True
        raise NotFound()

    @classmethod
    def id_generator(cls):
        return str(cls.id + 1)

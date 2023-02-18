class BaseRepository:
    def add(self, entity):
        raise NotImplementedError

    def remove_by_complex_number(self, complex_number):
        raise NotImplementedError

    def remove_all(self):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def find_by_complex_number(self, entity_complex_number):
        raise NotImplementedError


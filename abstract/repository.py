from abc import ABC, abstractmethod


class IRepository(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def create(self, item):
        raise NotImplementedError

    @abstractmethod
    def update(self, item):
        raise NotImplementedError


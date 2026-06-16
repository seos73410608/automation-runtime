from abc import ABC, abstractmethod


class BaseJob(ABC):

    @abstractmethod
    def execute(self):
        pass
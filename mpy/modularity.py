# modularity.py
from abc import ABC, abstractmethod
from pydantic import BaseModel
import typing as t

class Null(BaseModel):
    pass

class ModularityBase(ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initialize_methods()

    def _initialize_methods(self):
        for name, annot in self.METHODS.items():
            if getattr(self, name, Null) is not Null:
                continue
            setattr(self, name, annot(this=self))

    @classmethod
    def __init_subclass__(cls, *args, **kwargs):
        cls.METHODS = getattr(cls, 'METHODS', {})
        cls.CLASS_METHODS = getattr(cls, 'CLASS_METHODS', {})
        super().__init_subclass__(*args, **kwargs)

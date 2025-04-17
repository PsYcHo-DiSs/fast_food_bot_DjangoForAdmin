import os
import uuid

from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndRename:
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        # генерируем уникальное имя
        filename = f"{uuid.uuid4().hex}_{filename}"
        return os.path.join(self.path, filename)

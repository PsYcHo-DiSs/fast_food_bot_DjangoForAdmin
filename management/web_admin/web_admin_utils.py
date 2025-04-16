import os
import uuid

from django.utils.deconstruct import deconstructible
from django.utils.text import slugify


@deconstructible
class PathAndRename:
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        # получаем название категории(русс.) и делаем его транслитерацию, так как динамически создастся каталог
        category_name = slugify(instance.category.category_name)
        # генерируем уникальное имя
        filename = f"{uuid.uuid4().hex}_{filename}"
        return os.path.join(self.path, category_name, filename)

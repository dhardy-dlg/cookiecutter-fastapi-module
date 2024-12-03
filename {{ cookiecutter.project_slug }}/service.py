from typing import Sequence, Optional
from sqlmodel import Session
from shared.{{cookiecutter.module_name}}.schemas import {{cookiecutter.module_name.capitalize()}}Create, {{cookiecutter.module_name.capitalize()}}Update
from shared.{{cookiecutter.module_name}}.models import {{cookiecutter.module_name.capitalize()}}
from shared.{{cookiecutter.module_name}}.store import {{cookiecutter.module_name.capitalize()}}Store

class {{cookiecutter.module_name.capitalize()}}Service:
    """
    Service layer for managing {{cookiecutter.module_name}} business logic.
    """
    def __init__(self, session: Session):
        self.store = {{cookiecutter.module_name.capitalize()}}Store(session)

    def get(self, item_id: str) -> Optional[{{cookiecutter.module_name.capitalize()}}]:
        """
        Retrieve a {{cookiecutter.module_name}} by ID.
        """
        return self.store.get(item_id)

    def create(self, item: {{cookiecutter.module_name.capitalize()}}Create) -> {{cookiecutter.module_name.capitalize()}}:
        """
        Create a new {{cookiecutter.module_name}}.
        """
        return self.store.create(item)

    def update(self, item_id: str, update: {{cookiecutter.module_name.capitalize()}}Update) -> Optional[{{cookiecutter.module_name.capitalize()}}]:
        """
        Update an existing {{cookiecutter.module_name}} by ID.
        """
        return self.store.update(item_id, update)

    def search(self, limit: int = 10, offset: int = 0) -> Sequence[{{cookiecutter.module_name.capitalize()}}]:
        """
        Search for {{cookiecutter.module_name}}s with pagination.
        """
        return self.store.search(limit, offset)

    def delete(self, item_id: str) -> Optional[{{cookiecutter.module_name.capitalize()}}]:
        """
        Delete a {{cookiecutter.module_name}} by ID.
        """
        return self.store.delete(item_id)
from sqlmodel import Session, select
from api.{{cookiecutter.module_name}}.models import {{cookiecutter.module_name.capitalize()}}
from api.{{cookiecutter.module_name}}.schemas import {{cookiecutter.module_name.capitalize()}}Create, {{cookiecutter.module_name.capitalize()}}Update
from typing import Optional, Sequence


class {{cookiecutter.module_name.capitalize()}}Store:
    """
    Store layer for managing {{cookiecutter.module_name.capitalize()}} database operations.
    """
    def __init__(self, session: Session):
        self.session = session

    def get(self, item_id: str) -> Optional[{{cookiecutter.module_name.capitalize()}}]:
        """
        Retrieve a {{cookiecutter.module_name}} by ID.
        """
        return self.session.get({{cookiecutter.module_name.capitalize()}}, item_id)

    def get_all(self) -> Sequence[{{cookiecutter.module_name.capitalize()}}]:
        """
        Retrieve all {{cookiecutter.module_name}}s.
        """
        query = select({{cookiecutter.module_name.capitalize()}})
        return self.session.exec(query).all()

    def create(self, create_item: {{cookiecutter.module_name.capitalize()}}Create) -> {{cookiecutter.module_name.capitalize()}}:
        """
        Create a new {{cookiecutter.module_name}} in the database.
        """
        item = {{cookiecutter.module_name.capitalize()}}(
            **create_item.dict(),
        )
        self.session.add(item)
        self._commit()
        return item

    def update(self, item_id: str, update: {{cookiecutter.module_name.capitalize()}}Update) -> Optional[{{cookiecutter.module_name.capitalize()}}]:
        """
        Update an existing {{cookiecutter.module_name}} by ID.
        """
        item = self.get(item_id)
        if not item:
            return None

        item_data = update.model_dump(exclude_unset=True)
        for key, value in item_data.items():
            setattr(item, key, value)

        self.session.add(item)
        self._commit()
        return item

    def search(self, limit: int = 10, offset: int = 0) -> Sequence[{{cookiecutter.module_name.capitalize()}}]:
        """
        Search and return a list of {{cookiecutter.module_name}}s with pagination.
        """
        query = select({{cookiecutter.module_name.capitalize()}}).limit(limit).offset(offset)
        return self.session.exec(query).all()

    def delete(self, item_id: str) -> Optional[{{cookiecutter.module_name.capitalize()}}]:
        """
        Delete a {{cookiecutter.module_name}} by ID.
        """
        item = self.get(item_id)
        if not item:
            return None
        self.session.delete(item)
        self._commit()
        return item

    def _commit(self):
        """
        Commit session changes and handle exceptions.
        """
        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
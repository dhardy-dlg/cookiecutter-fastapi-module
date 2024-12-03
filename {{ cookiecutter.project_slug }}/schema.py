from datetime import datetime, timezone
from pydantic import BaseModel


class BaseSchema(BaseModel):
    """
    Base schema that includes common fields for all entities.
    Extend this schema in other Pydantic models where applicable.
    """
    createdAt: datetime = datetime.now(timezone.utc)
    updatedAt: datetime = datetime.now(timezone.utc)

class {{cookiecutter.module_name.capitalize()}}Base(BaseSchema):
    """
    Base schema for user fields.
    """
    pass


class {{cookiecutter.module_name.capitalize()}}Create(BaseSchema):
    pass

class {{cookiecutter.module_name.capitalize()}}Update(BaseSchema):
    pass

class {{cookiecutter.module_name.capitalize()}}Public(DocumentBase):
    pass


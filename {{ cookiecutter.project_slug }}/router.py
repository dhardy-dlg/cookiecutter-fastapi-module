import logging
from typing import Sequence
from fastapi import APIRouter, HTTPException, status, Depends
from api.database.database import DbSession
from api.{{cookiecutter.module_name}}.service import {{cookiecutter.module_name.capitalize()}}Service
from api.{{cookiecutter.module_name}}.schemas import {{cookiecutter.module_name.capitalize()}}Create, {{cookiecutter.module_name.capitalize()}}Update, {{cookiecutter.module_name.capitalize()}}Public
from api.{{cookiecutter.module_name}}.models import {{cookiecutter.module_name.capitalize()}}

log = logging.getLogger(__name__)

# Initialize the router
{{cookiecutter.module_name}}_router = APIRouter(
    tags=["{{cookiecutter.module_name.capitalize()}}"],
    prefix="/{{cookiecutter.module_name}}s",
    dependencies=[]  # Add dependencies here if needed
)

{% set crud_operations = cookiecutter.full_crud.split(",") %}

{% if "all" in crud_operations or "read" in crud_operations %}
@{{cookiecutter.module_name}}_router.get(
    "/{item_id}",
    summary="Retrieves a {{cookiecutter.module_name}} by id.",
    response_model={{cookiecutter.module_name.capitalize()}}Public,
)
def get(item_id: str, session: DbSession = Depends()) -> {{cookiecutter.module_name.capitalize()}}Public:
    item = {{cookiecutter.module_name.capitalize()}}Service(session).get(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="{{cookiecutter.module_name.capitalize()}} not found")
    return item
{% endif %}

{% if "all" in crud_operations or "create" in crud_operations %}
@{{cookiecutter.module_name}}_router.post(
    "/",
    summary="Creates a new {{cookiecutter.module_name}}.",
    status_code=status.HTTP_201_CREATED,
    response_model={{cookiecutter.module_name.capitalize()}},
)
def create(item: {{cookiecutter.module_name.capitalize()}}Create, session: DbSession = Depends()) -> {{cookiecutter.module_name.capitalize()}}:
    return {{cookiecutter.module_name.capitalize()}}Service(session).create(item)
{% endif %}

{% if "all" in crud_operations or "update" in crud_operations %}
@{{cookiecutter.module_name}}_router.patch(
    "/{item_id}",
    summary="Updates an existing {{cookiecutter.module_name}}.",
    response_model={{cookiecutter.module_name.capitalize()}},
)
def update(item_id: str, update: {{cookiecutter.module_name.capitalize()}}Update, session: DbSession = Depends()) -> {{cookiecutter.module_name.capitalize()}}:
    updated_item = {{cookiecutter.module_name.capitalize()}}Service(session).update(item_id, update)
    if not updated_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="{{cookiecutter.module_name.capitalize()}} not found")
    return updated_item
{% endif %}

{% if "all" in crud_operations or "delete" in crud_operations %}
@{{cookiecutter.module_name}}_router.delete(
    "/{item_id}",
    summary="Deletes an existing {{cookiecutter.module_name}}.",
    response_model={{cookiecutter.module_name.capitalize()}}Public,
)
def delete(item_id: str, session: DbSession = Depends()) -> {{cookiecutter.module_name.capitalize()}}Public:
    item_service = {{cookiecutter.module_name.capitalize()}}Service(session)
    item = item_service.get(item_id)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="{{cookiecutter.module_name.capitalize()}} not found")
    deleted_item = item_service.delete(item_id)
    return deleted_item
{% endif %}

{% if "all" in crud_operations or "search" in crud_operations %}
@{{cookiecutter.module_name}}_router.get(
    "/search",
    summary="Search {{cookiecutter.module_name}}s.",
    response_model=list[{{cookiecutter.module_name.capitalize()}}Public],
)
def search(session: DbSession = Depends(), limit: int = 10, offset: int = 0) -> Sequence[{{cookiecutter.module_name.capitalize()}}]:
    return {{cookiecutter.module_name.capitalize()}}Service(session).search(limit, offset)
{% endif %}
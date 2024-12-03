import sys

def validate_full_crud():
    allowed = {"all", "create", "read", "update", "delete", "list", "search"}
    user_input = "{{cookiecutter.full_crud}}".split(",")
    invalid = [item for item in user_input if item.strip() not in allowed]

    if invalid:
        print(f"Invalid CRUD options: {', '.join(invalid)}. Allowed options are: {', '.join(allowed)}")
        sys.exit(1)

validate_full_crud()
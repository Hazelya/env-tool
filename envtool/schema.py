
# Lecture du schema

import yaml
from validate_file_path import validate_file_path


def load_schema(file_path):

    try:
        validate_file_path(file_path=file_path)
    except (FileNotFoundError, ValueError, PermissionError) as e:
        print(f"File validation error: {e}")
    
    with open(file_path, "r") as file:
        schema = yaml.safe_load(file)

    return schema





def test_load_schema():
    schema = load_schema("./examples/env_schema.yml")
    print(schema)



#test_load_schema()
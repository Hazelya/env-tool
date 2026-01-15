
# Lecture du .env

from validate_file_path import validate_file_path

"""
Docstring pour envtool.loader
"""


def load_env(file_path):

    try:
        validate_file_path(file_path=file_path)
    except (FileNotFoundError, ValueError, PermissionError) as e:
        print(f"File validation error: {e}")

    env_vars = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()

        if not line or line == "\n": # Line is empty 
            #print("empty")
            continue

        if line.startswith("#"):
            #print("start with #")
            continue

        if "=" not in line:
            #print("not =")
            continue
        
        line_split = line.split("=")
        key = line_split[0]
        value = line_split[1]

        key = key.strip()
        value = value.strip()
        value = value.strip('"')
        value = value.strip("'")
    

        env_vars[key] = value

    return env_vars


def load_env_secure(file_path):

    untreated_env = load_env(file_path)

    masked_env = {}

    for key in enumerate(untreated_env):
        masked_env[key] = "***"

    return untreated_env, masked_env







def test_load_env():

    file_path = "./examples/.env"

    # function
    env_vars = load_env(file_path=file_path)

    # Verification
    assert env_vars["DB_HOST"] == "localhost"
    assert env_vars["DB_PORT"] == "5432"
    assert env_vars["DEBUG"] == "false"
    assert env_vars["API_KEY"] == "secret_key"

    # number of variables
    assert len(env_vars) == 4

    print(env_vars)



#test_load_env()
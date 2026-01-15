import os

def validate_file_path(file_path):
    ## Check if path exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Path {file_path} does not exist")

    ## Check if it's a file
    if not os.path.isfile(file_path):
        raise ValueError(f"{file_path} is not a valid file")

    ## Check read permissions
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"No read permission for {file_path}")

    return True






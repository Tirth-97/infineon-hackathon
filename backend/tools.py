def read_code(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def read_error(error_path=None):
    if error_path is None:
        return "No runtime error provided. Analyze code logically."
    with open(error_path, "r", encoding="utf-8") as f:
        return f.read()

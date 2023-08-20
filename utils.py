def get_file_details(file_path):
    split_file_path = file_path.split("/")
    path = "/".join(split_file_path[:-1])
    name = split_file_path.pop().split(".")[0]

    return {"path": path, "name": name}

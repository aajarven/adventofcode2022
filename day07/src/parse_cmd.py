import sys

from src.file_tree import File, Directory


def process_ls(input_lines, ls_line, current_dir):
    """
    Add files/directories from ls output as children of current dir
    """
    line_number = ls_line + 1
    current_line = input_lines[line_number].strip()
    while "$" not in current_line:
        current_line = input_lines[line_number].strip()
        parts = current_line.split()
        if parts[0] == "dir":
            new_file = Directory(parts[1], current_dir)
        else:
            new_file = File(parts[1], current_dir, int(parts[0]))
        current_dir.add_child(new_file)

        line_number += 1
        if line_number == len(input_lines):
            return
        current_line = input_lines[line_number].strip()


def parse_cmd(input_lines):
    root_node = Directory("/", None)
    current_dir = root_node
    line_number = 1
    while line_number < len(input_lines):
        current_line = input_lines[line_number].strip()
        if current_line == "$ ls":
            process_ls(input_lines, line_number, current_dir)

        elif "$ cd" in current_line:
            destination = current_line.split()[2]
            if destination == "..":
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.get_child(destination)
        line_number += 1

    return root_node


def list_small(root, threshold):
    for file in root.traverse():
        if file.__class__ == Directory and file.size <= threshold:
            yield file


def small_total(root, threshold=100000):
    return sum(file.size for file in list_small(root, threshold))


def list_big(root, threshold):
    for file in root.traverse():
        if file.__class__ == Directory and file.size >= threshold:
            yield file


def smallest_to_remove(root, must_free):
    candidates = list_big(root, must_free)
    smallest_candidate_size = sys.maxsize
    for candidate in candidates:
        if candidate.size < smallest_candidate_size:
            smallest_candidate_size = candidate.size
    return smallest_candidate_size

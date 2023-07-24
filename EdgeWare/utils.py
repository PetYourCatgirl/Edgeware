from pathlib import Path
import os


def get_file_paths_recursive(root_dir: Path | str) -> list[Path]:
    """Given a directory, return a list of every file path in any level of subdirectory"""
    if isinstance(root_dir, str):
        root_dir = Path(root_dir)

    if not root_dir.is_dir():
        return []

    file_paths = []
    for dirname, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            path = Path(os.path.join(dirname, filename))
            file_paths.append(path)

        # os.walk only looks one level deep
        # so call this recursively
        for dirname in dirnames:
            subdir_file_paths = get_file_paths_recursive(os.path.join(dirname, ""))
            file_paths += subdir_file_paths
    return file_paths


if __name__ == "__main__":
    breakpoint()

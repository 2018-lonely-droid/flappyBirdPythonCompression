import os

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size


relative_directory_path_list = ['Flappy-bird-python', 'Flappy-bird-python-compressed']  # Relative to the current working directory

for path in relative_directory_path_list:
    absolute_directory_path = os.path.abspath(path)
    size_in_bytes = get_directory_size(absolute_directory_path)
    size_in_kilobytes = size_in_bytes / 1024.0
    size_in_megabytes = size_in_kilobytes / 1024.0

    print(f"Size of directory '{path}':")
    print(f"In Bytes: {size_in_bytes}")
    print(f"In Kilobytes: {size_in_kilobytes}")
    print(f"In Megabytes: {size_in_megabytes}")
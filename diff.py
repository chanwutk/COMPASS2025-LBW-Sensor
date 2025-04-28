import os

ignore = [
    '.git',
    '_original',
    '.github'
]

root_files: list[tuple[str, str]] = []

for root, _, files in os.walk('.'):
    for file in files:
        if not any(ignored in root for ignored in ignore):
            if file.endswith('.tex'):
                root_files.append((root, file))

for root, file in root_files:
    current = os.path.join(root, file)
    original = os.path.join('./_original', root[2:], file)
    print(os.path.join(root, file))
    print(os.path.join('./_original', root[2:], file))

    os.system(f'latexdiff {original} {current} > {current}')
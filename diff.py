import os

ignore = [
    '.git',
    '_original',
    '.github'
]

for root, _, files in os.walk('.'):
    for file in files:
        if not any(ignored in root for ignored in ignore):
            if file.endswith('.tex'):
                current = os.path.join(root, file)
                original = os.path.join('./_original', root[2:], file)
                print(os.path.join(root, file))
                print(os.path.join('./_original', root[2:], file))

                os.system(f'latexdiff {current} {original} > {current}')
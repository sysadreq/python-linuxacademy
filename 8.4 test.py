
lines = input('--> ')

if not lines.strip():
    with open('file2', 'w') as f:
        f.writelines(lines)
        f.close()
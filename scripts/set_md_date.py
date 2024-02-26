import os
import subprocess
import toml

def get_creation_time(filepath):
    git_log = subprocess.run(['git', 'log', '--reverse', '--format=%aI', '--', filepath], capture_output=True, text=True)
    first_commit_date = git_log.stdout.split('\n')[0]
    return first_commit_date.strip()

def main():
    for path, dirs, files in os.walk('content'):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(path, filename)
                creation_time_str = get_creation_time(filepath)
                if creation_time_str is None:
                    print(f"Could not get creation date for file {filepath}")
                    continue
                with open(filepath, 'r') as file:
                    lines = file.readlines()
                try:
                    front_matter_start = lines.index('+++\n') + 1
                    front_matter_end = lines.index('+++\n', front_matter_start)
                    front_matter = toml.loads(''.join(lines[front_matter_start:front_matter_end]))
                except ValueError:
                    print(f"File {filepath} doesn't have front matter")
                    continue

                front_matter['date'] = creation_time_str

                with open(filepath, 'w') as file:
                    file.write('+++\n')
                    file.write(toml.dumps(front_matter))
                    file.write('+++\n')
                    file.write(''.join(lines[front_matter_end+1:]))

                print(f"Added date {creation_time_str} to the file {filepath}")

if __name__ == "__main__":
    main()
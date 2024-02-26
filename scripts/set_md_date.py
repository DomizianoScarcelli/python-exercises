import os
import time
import toml

def main():
    for path, dirs, files in os.walk('content'):
        for filename in files:
            if filename.endswith('.md'):
                filepath = os.path.join(path, filename)
                creation_time = os.path.getctime(filepath)
                creation_time_str = time.strftime('%Y-%m-%d', time.localtime(creation_time))

                with open(filepath, 'r') as file:
                    lines = file.readlines()
                try:

                    front_matter_start = lines.index('+++\n') + 1
                    front_matter_end = lines.index('+++\n', front_matter_start)
                    front_matter = toml.loads(''.join(lines[front_matter_start:front_matter_end]))
                except ValueError:
                    print(f"File {filepath} doesn't have front matter")
                    continue

                if 'date' in front_matter:
                    print(f"File {filepath} already has a date")
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
from project import Project

# constants
PROJECT_FILE = 'projects.txt'


def load_project(project_file):
    """Read file of project details, return a list of project."""
    projects = []
    # Open the file for reading
    in_file = open(project_file, 'r')

    # File format is like: name, start_date, priority, estimate, completion
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()

    # All other lines are project data
    for line in in_file:
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split('\t')

        # Construct a ProgrammingLanguage object using the elements
        # priority should be an int
        # estimate should be a float
        # completion should be an int
        project = Project(parts[0],
                          parts[1],
                          int(parts[2]),
                          float(parts[3]),
                          int(parts[4]))

        # Add the language we've just constructed to the list
        projects.append(project)

    # Close the file as soon as we've finished reading it
    in_file.close()
    return projects


def main():
    # testing load_project
    projects = load_project(PROJECT_FILE)
    for project in projects:
        print(project)


if __name__ == '__main__':
    main()

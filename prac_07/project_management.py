from project import Project
import datetime

# constants
PROJECT_FILE = 'projects.txt'


def load_projects(project_file):
    """Read file of project details, return a list of projects."""
    projects = []
    try:
        # Open the file for reading
        with open(project_file, 'r') as in_file:
            # File format is like: name, start_date, priority, completion
            # 'Consume' the first line (header) - we don't need its contents
            in_file.readline()

            # All other lines are project data
            for line in in_file:
                # Strip newline from end and split it into parts (CSV)
                parts = line.strip().split('\t')

                # Construct a Project object using the elements
                # priority should be an int
                # completion should be an int
                project = Project(parts[0],
                                  datetime.datetime.strptime(parts[1], "%d/%m/%Y").date(),
                                  float(parts[2]),
                                  float(parts[3]))

                # Add the project we've just constructed to the list
                projects.append(project)
        return projects
    except FileNotFoundError:
        return projects


def save_projects(project_file, projects):
    """Save list of projects to the data file."""
    try:
        # Open the file for writing
        with open(project_file, 'w') as out_file:
            # Write the header
            out_file.write("Name\tStart Date\tPriority\tCompletion\n")

            # Write project data
            for project in projects:
                out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}"
                               f"\t{project.priority}\t{project.completion}\n")
    except IOError:
        print("Error saving projects to the file.")


def display_projects(projects):
    """Display two groups of projects: incomplete projects and completed projects, both sorted by priority."""
    incomplete_projects = sorted(filter(lambda p: p.completion < 100, projects), key=lambda p: p.priority)
    completed_projects = sorted(filter(lambda p: p.completion == 100, projects), key=lambda p: p.priority)

    print("Incomplete Projects:")
    for project in incomplete_projects:
        print(project)

    print("\nCompleted Projects:")
    for project in completed_projects:
        print(project)


def filter_projects_by_date(projects):
    """Ask the user for a date and display only projects that start after that date, sorted by date."""
    date_string = input("Enter date (d/m/yyyy) to filter projects: ")
    try:
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

        filtered_projects = sorted(filter(lambda p: p.start_date > date, projects), key=lambda p: p.start_date)

        print(f"Projects starting after {date.strftime('%d/%m/%Y')}:")
        for project in filtered_projects:
            print(project)
    except ValueError:
        print("Invalid date format. Please enter a valid date (d/m/yyyy).")


def add_new_project(projects):
    """Ask the user for the inputs and add a new project to memory."""
    name = input("Enter project name: ")
    date_string = input("Enter project start date (d/m/yyyy): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Enter project priority (higher number indicates higher priority): "))
    completion = int(input("Enter project completion (0-100%): "))

    project = Project(name, start_date, priority, completion)
    projects.append(project)
    print("Project added successfully!")


def update_project(projects):
    """Choose a project, then modify the completion % and/or priority - leave blank to retain existing values."""
    project_name = input("Enter the name of the project to update: ")
    project = next((p for p in projects if p.name == project_name), None)

    if project:
        new_completion = input(
            f"Enter new completion percentage for '{project.name}' (blank to retain existing value): ")
        new_priority = input(f"Enter new priority for '{project.name}' (blank to retain existing value): ")

        if new_completion:
            project.completion = int(new_completion)

        if new_priority:
            project.priority = int(new_priority)
        print("Project updated successfully!")
    else:
        print(f"Project with name '{project_name}' not found.")


def main():
    # Load projects from the data file when the program starts
    projects = load_projects(PROJECT_FILE)

    while True:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ")

        if choice == "l":
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            break
        else:
            print("Invalid choice. Please try again.")

    # Save projects to the data file when the user quits
    save_projects(PROJECT_FILE, projects)
    print("Thank you for using custom-built project management software.")


if __name__ == '__main__':
    main()

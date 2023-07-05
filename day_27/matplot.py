import matplotlib.pyplot as plt
from datetime import datetime, timedelta

MENU = """Options:
    [s] start timer
    [e] end timer
    [d] delete
    [r] report
    [a] analytics
    [q] quit"""
VALID_INSTRUCTIONS = {'s', 'e', 'd', 'r', 'q', 'a'}
NO_DATETIME = ''

class Task:
    """Store a task timer.
    Note, the timer starts when the object is created.
    Attributes:
        - id: the task name
        - start: datetime representing start time
        - end: datetime representing end time. None when still running
    """

    def __init__(self, task_id, start=None, end=None):
        self.id = task_id
        self.start = start
        if self.start is None:
            self.start_timer()
        self.end = end

    def __repr__(self):
        """ Return a string like what you would use to create a Task.
        When printing a list of `Tasks` this method will be called to display
        each task. Note, to call this method use the repr() function.
        """
        return f"Task('{self.id}', {repr(self.start)}, {repr(self.end)})"

    def __str__(self):
        """Return a nice human-readable string version of the Task.
        When insterting a task into an f-string this method is called.
        Note, to call this method use the str() function.
        """
        string = f"{self.id} {self.start.date()}: "
        if self.is_running():
            string += "<still running>"
        else:
            string += f"{self.duration()}"
        return string

    def is_running(self):
        """Returns True if task has no end time, False otherwise."""
        return self.end == None

    def start_timer(self):
        """Start the timer by setting start to current datetime"""
        self.start = datetime.now()  # Use the current datetime.

    def end_timer(self):
        """End the timer by setting end to current datetime.
        If the timer is not running do not end the timer."
        """
        if self.is_running():
            self.end = datetime.now()

    def duration(self):
        """Returns the duration of the timer as a timedelta.
        If the timer isn't stopped, return a timedelta(0).
        """
        if self.end == None:
            return timedelta(0)
        else:
            duration = self.end - self.start
        return duration


# Start of provided code ===================================================================


def read_list(prompt):
    """Prompt user for input (comma separated values).
    Returns a list of the comma separated values, whitespace stripped.
    """
    strings = input(prompt).split(',')
    return [string.strip() for string in strings]


def read_valid_input(valids, transformer=None):
    """Read and return an input from stdin.
    Only accept inputs in valids, repeatedly prompt until one is given.
    Apply the transformer function to the user's inputs, if provided.
    """
    instruction = input('Select option: ')
    if transformer:
        instruction = transformer(instruction)
    while instruction not in valids:
        print('Please select a valid option')
        instruction = input('Select option: ')
        if transformer:
            instruction = transformer(instruction)
    return instruction


def read_instruction():
    """Read and return a valid instruction from stdin."""
    instruction = read_valid_input(VALID_INSTRUCTIONS, str.lower)
    return instruction


def select_timer_index(tasks):
    """Takes a list of Task objects, then prompts the
    user to select one. Returns the user selected Task object.
    """
    print("Select task:")
    for i, task in enumerate(tasks):
        print(f"      [{i}] {str(task)}")
    valid_task_nums = range(len(tasks))
    task_index = read_valid_input(valid_task_nums, int)
    return task_index


def add_task(tasks, task_id=None, start=None, end=None):
    """Add a new task to tasks.
    When task_id isn't provided prompt the user for it.
    """
    if task_id is None:
        task_id = input("Enter project name: ")
    timer = Task(task_id, start, end)
    tasks.append(timer)


def end_task(tasks):
    """Prompt the user to select a running task (from tasks).
    End the selected task.
    """
    running_tasks = [task for task in tasks if task.is_running()]
    if len(running_tasks) > 0:
        task_index = select_timer_index(running_tasks)
        task = tasks[task_index]
        task.end_timer()
    else:
        print("Can't end task: no timers are running.")


def delete_task(tasks):
    """Prompt the user to select a task (from tasks).
    Remove the selected task from tasks.
    """
    if len(tasks) > 0:
        task_index = select_timer_index(tasks)
        tasks.pop(task_index)
    else:
        print("Can't delete task: no timers exist.")


def print_report(tasks):
    """Print a basic report of times in tasks."""
    print("Report:")
    for task in tasks:
        print(f"    {task}")


def timedelta_duration_string(delta):
    """Returns string representation of  a datetime.timedelta as:
    hours:minutes:seconds.
    This function will be useful when answering question 8.
    """
    seconds_in_minute = 60
    seconds_in_hour = seconds_in_minute * 60

    seconds = delta.total_seconds()
    hours, seconds = divmod(seconds, seconds_in_hour)
    minutes, seconds = divmod(seconds, seconds_in_minute)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"


def datetime_from_iso(string):
    """Return a datetime from an ISO format string.
    When no datetime, return None.
    """
    if string == NO_DATETIME:
        return None
    return datetime.fromisoformat(string)


def read_task_file(filename):
    """Opens a task file, with file name filename and reads it.
    Returns a task list containing the tasks in that file.
    """
    infile = open(filename, 'r')
    lines = infile.read().splitlines()
    infile.close()

    tasks = []
    for line in lines:
        name, start, end = line.split(',')
        start = datetime_from_iso(start)
        end = datetime_from_iso(end)
        add_task(tasks, name, start, end)
    return tasks


# End of provided code ===================================================================


def save_task(tasks):
    """Open a new file and write task data file with that filename."""
    saved_file = input('Save tasks as (enter filename): ')
    if saved_file != '':
        writting_file = open(saved_file, 'w')
        for task in tasks:
            if task.end == None:
                content = task.id + ',' + task.start.isoformat() + ',' + '\n'
            if task.end != None:
                content = task.id + ',' + task.start.isoformat() + ',' + task.end.isoformat() + '\n'
            writting_file.write(content)
        writting_file.close()


def analyse_tasks(tasks):
    """Return each task id in alphabetical order,
    the frequency and total time on each one"""

    task_dictionary = {}

    data_gragh = {}

    total_time = timedelta(0)
    print("Task Analytics:")
    print("    Task ID    Freq Time")
    for task in tasks:
        if task.id not in task_dictionary:
            time = task.duration()
            task_dictionary[task.id] = [time]
        else:
            time = task.duration()
            task_dictionary[task.id] += [time]
        total_time += time
    for key, value in sorted(task_dictionary.items()):
        time_on_task = timedelta(0)
        frequency = len(value)
        for duration in value:
            time_on_task += duration
        data_gragh[key] = round(time_on_task / total_time * 100)
        print(f"    {key:10}{frequency:5} {timedelta_duration_string(time_on_task)}")
    print(f"You spent {timedelta_duration_string(total_time)} on {len(tasks)} task(s).\n")
    axes = plt.axes()
    # range_of_y = max(data_gragh.values()) + 5
    while max(data_gragh.values()) % 5 != 0:
        y = max(data_gragh.values()) + 1
    axes.bar(range(len(data_gragh)), data_gragh.values())
    axes.set_title("Total Time (%)")
    axes.set_xlabel("Tasks")
    axes.set_xticks(range(len(data_gragh)))
    axes.set_xticklabels(data_gragh.keys())
    plt.ylim(0, y)

    plt.show()


def main():
    """Ask for an input filename, if one is provided read the tasks from that file.
    Show the menu once and accept commands until the quit command is given.
    When quitting, ask for a filename and save the tasks to that file.
    """
    tasks = []

    instruction = ''
    filename = input("Enter filename to open (or enter to skip): ")
    if filename != '':
        tasks = read_task_file(filename)
    print(MENU)
    while instruction != 'q':
        instruction = read_instruction()
        if instruction == 's':
            add_task(tasks)
        elif instruction == 'e':
            end_task(tasks)
        elif instruction == 'd':
            delete_task(tasks)
        elif instruction == 'r':
            print_report(tasks)
        elif instruction == 'a':
            analyse_tasks(tasks)
    save_task(tasks)


if __name__ == "__main__":
    main()



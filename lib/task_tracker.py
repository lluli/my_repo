"""As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list."""

class TaskTracker():

    def __init__(self):
        self.to_do = []
    
    def add(self, task):
        self.to_do.append(task)

    def remove(self, task):
        self.to_do.remove(task)
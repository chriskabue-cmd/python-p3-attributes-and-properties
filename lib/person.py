#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    approved_jobs = ["Sales", "Manager", "Engineer", "Teacher", "Developer"]

    def __init__(self, name="unknown", job=None):
        # --- Validate name ---
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            # convert name to title case before saving
            name = name.title()

        self.name = name

        # --- Validate job only if provided ---
        if job is not None:
            if job not in self.approved_jobs:
                print("Job must be in list of approved jobs.")
            self.job = job
        else:
            self.job = None
    pass
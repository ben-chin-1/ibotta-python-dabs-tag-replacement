import yaml
import json
from databricks.bundles.jobs import Job
from databricks.bundles.core import Bundle, Resources, Variable, variables


"""
The main job for dabs_python_example.
"""

variables_imported = yaml.safe_load(open("variables/variables.yml", "r"))
custom_tags = variables_imported['variables']['custom_tags']['default']
custom_tags_string = json.dumps(custom_tags)

dabs_python_example_job = Job.from_dict(
    {
        "name": "dabs_python_example_job",
        "trigger": {
            # Run this job every day, exactly one day from the last run; see https://docs.databricks.com/api/workspace/jobs/create#trigger
            "periodic": {
                "interval": 1,
                "unit": "DAYS",
            },
        },
        "email_notifications": {
            "on_failure": [
                "benjamin.chin@databricks.com",
            ],
        },
        "tasks": [
            {
                "task_key": "notebook_task",
                "notebook_task": {
                    "notebook_path": "src/notebook.ipynb",
                    "base_parameters": {
                        "custom_tags": custom_tags_string
                    },
                },
            },
        ],
    }
)

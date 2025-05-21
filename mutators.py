import yaml
import json
from dataclasses import replace
from databricks.bundles.core import Bundle, job_mutator
from databricks.bundles.jobs import Job, JobEmailNotifications, Task

# import in custom tags from variable
variables_imported = yaml.safe_load(open("variables/variables.yml", "r"))
custom_tags = variables_imported['variables']['custom_tags']['default']
custom_tags_string = json.dumps(custom_tags)

@job_mutator
def add_custom_tags_to_notebook_task(bundle: Bundle, job: Job) -> Job:
    new_tasks = []
    for task in job.tasks:
        if "notebook_task" in task.as_dict().keys():
            existing_task_config = task.as_dict()
            existing_task_config['notebook_task']['base_parameters']['custom_tags'] = custom_tags_string
            tagged_task = Task.from_dict(existing_task_config)
            new_tasks.append(tagged_task)
        else:
            new_tasks.append(task)

    return replace(job, tasks=new_tasks)
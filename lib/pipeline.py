import yaml
import subprocess

color_err   = "\033[1;31m"  


def load_pipeline_file(pipeline):
    return yaml.safe_load(open(pipeline))

def get_pipelines(pipeline_loaded):
    return pipeline_loaded['pipelines']

def get_picked_pipeline(pipelines, picked_name):
    message_pipeline(picked_name)
    return list(filter(lambda pipeline: pipeline['name'] in picked_name, pipelines))

def get_tasks_definitions(pipeline_loaded):
    return pipeline_loaded['tasks']

def get_tasks_pipeline(pipeline):
    return pipeline[0]['tasks']

def get_command_tasks(tasks, tasks_definitions):
    tasks_commands = []
    for task in tasks:
        for k,v in tasks_definitions.items():
            if task == k:
                tasks_commands.append(v)
    return tasks_commands

def execute_tasks(tasks_commands):
    return list(map(lambda task: (message_task(task), execute_shell(task)), tasks_commands))

def execute_shell(command):
    try:
        return subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as err:
        raise SystemExit("{}{}".format(color_err,err))         

def message_task(task):
    return print ("--- Executing command: '{}' ---".format(task))

def message_pipeline(pipeline):
    return print ("##### Executing pipeline: '{}' #####".format(pipeline))
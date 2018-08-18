#!/usr/bin/env python3
import sys

from lib.project import enter_folder_project, get_project_name, clone_project, check_project_exist
from lib.pipeline import load_pipeline_file, get_pipelines, get_picked_pipeline, get_tasks_definitions, get_tasks_pipeline, get_command_tasks, execute_tasks


pipeline_file = 'pipeline.yml'


def main(argv):
    
    #recive args
    pipeline_for_run = argv[1]
    repo = argv[2]

    #git settings
    project_name =  get_project_name(repo)
    clone_project(project_name, repo) # clone just if project not exist
    enter_folder_project(project_name)

    #run pipeline and tasks 
    pipeline_loaded = load_pipeline_file(pipeline_file)
    pipelines = get_pipelines(pipeline_loaded)
    picked_pipeline = get_picked_pipeline(pipelines, pipeline_for_run)
    tasks_definitions = get_tasks_definitions(pipeline_loaded)
    tasks_pipeline = get_tasks_pipeline(picked_pipeline)
    tasks_commands = get_command_tasks(tasks_pipeline, tasks_definitions)
    execute_tasks(tasks_commands)


if __name__ == "__main__":
    main(sys.argv)



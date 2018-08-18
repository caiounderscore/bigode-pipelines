#!/usr/bin/env python3
import git
import os

def enter_folder_project(project_name):
    os.chdir(project_name)

def get_project_name(repo):
    return os.path.basename(repo)


def clone_project(project_name, repo):
    if not check_project_exist(project_name):
        git.Git("./").clone(repo)

def check_project_exist(project_name):
    return os.path.exists(project_name)


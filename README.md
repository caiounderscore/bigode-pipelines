DevOps Software Enginnering Challenge
======

We wrote a simple dummy Java app but we decided that we don't want to use Jenkins nor CircleCI for our Continous Integration, instead, we've decided to ask you to write a simple Continous Integration engine for us :)

Your challenge is to write a script that will execute a simple pipeline described in a `pipeline.yml` that should be placed **in the root of a Git repository**.

Your CI tool will lookup this file, parse it and run the set of steps of the selected pipeline.

**NOTE**

Steps and pipelines changes from repo to repo, `pipeline-example` is just **one example that you can use to test your code** while developing.

At a glance, your script needs to:

1. Fetch git code (https://gitlab.com/devops-samples/pipeline-example.git for example)
1. Parse the `pipeline.yml`
1. Run selected pipeline

Pipeline.yml Format
======
The pipeline file has only two main hashes.

Tasks: Saved commands that can be used to create a pipeline

Pipelines: Group of ordered tasks


A pipeline.yml example:

```yaml
tasks:
  build: pip3 install -r ./requirements.txt
  test: python3 -m py_compile bigode-pipelines.py
  compress: zip -r project.zip ./

pipelines:
  - name: build
    tasks:
      - build
  - name: release
    tasks:
    - build
    - test
    - compress
```

Script Arguments
======

1. Pipeline name, E.g: build
1. Git repository URL (https or ssh)

Note that the command **should be in this exact order**, dont use flags such as `--pipeline`, keep it simple. Don't add extra parameters as well, just the pipeline name and the repository URL.

Examples
=====
Assuming you wrote a python script named `pipeline.py` (You're free to give a name to your CI tool :) )


```shell
python pipeline.py release https://github.com/caiounderscore/bigode-pipelines
```
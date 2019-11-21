# Easy-to-use StyleGAN implementation 

This implementation can either be used via command line or via Python API for easy use from Jupyter Notebooks or Python applications. The focus is on a good user experience with the most important parameters to tweak. More finegrained tuning options will be added over time, but always putting a good user experience first.

Usage is similar for command line and high-level Python API.

# Quickstart

Starting a project is as easy as:

1. Create a new project:
```sh
$ python main.py init /path/to/project
```

2. Edit your config (e.g. where's your training data?):
```sh
$ editor /path/to/project/config.yml 
```

3. Start (or resume) training:
```sh
$ python main.py train /path/to/project
```

If training is interrupted, you can simply start training again. Training will resume at the latest checkpoint:
```sh
$ python main.py train /path/to/project
```


# Structure of a training project

```
/path/to/dataset
/path/to/results
  |- config.yml    // All configuration to run, resume and reproduce this project
  |- samples/
  |    |- fake-0000000.png
  |    |- fake-0001040.png
  |    \    ...
  |- checkpoints/
  |    |- snapshot-001040.pkl
  |    |- snapshot-004120.pkl
  |    \    ...
  |- training.log
  |- events.tfevents
  \    ...
```
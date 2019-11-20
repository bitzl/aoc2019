# Easy-to-use StyleGAN implementation 

This implementation can either be used via command line or via Python API for easy use from Jupyter Notebooks or Python applications. The focus is on a good user experience with the most important parameters to tweak. More finegrained tuning options will be added over time, but always putting a good user experience first.

Usage is similar for command line and Python API.

Structure of a training project:

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
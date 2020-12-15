#!/usr/bin/env python

import app.jobs
import schedule
import time
from autoload import load_submodules


jobs = load_submodules(app.jobs)

for name in jobs:
    job = jobs.get(name)
    if hasattr(job, 'make'):
        job.make(schedule)

try :
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("quitting schedules...")
    for name in jobs:
        job = jobs.get(name)
        if hasattr(job, 'destroy'):
            job.destroy()
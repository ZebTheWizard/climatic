#!/usr/bin/env python

import app.schedules
import schedule
import time
from autoload import load_submodules


jobs = load_submodules(app.schedules)

for name in jobs:
    job = jobs.get(name)
    job.make(schedule)

try :
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("quitting schedules...")
    for name in jobs:
        job = jobs.get(name)
        try:
            job.destroy()
        except:
            pass
from django_cron import CronJobBase, Schedule
from django.core.management import call_command


class missingplayers(CronJobBase):
    RUN_EVERY_MINS = 10 # every 20 min
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'honbot.missingplayers'

    def do(self):
    	call_command('missingplayers')
        pass


class heroes(CronJobBase):
    RUN_EVERY_MINS = 24 * 60 # every 24 hours
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'honbot.heroes'

    def do(self):
    	call_command('heroes')
        pass


class herouse(CronJobBase):
    RUN_AT_TIMES = ['0:00']
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'honbot.herouse'

    def do(self):
    	call_command('herouse')
        pass


class removenullmatches(CronJobBase):
    RUN_EVERY_MINS = 60 * 3 # every 3 hours
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'honbot.removenullmatches'

    def do(self):
    	call_command('removenullmatches')
        pass
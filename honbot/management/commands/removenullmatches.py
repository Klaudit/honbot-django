from honbot.models import HeroAll, HeroUseage
from django.core.management.base import BaseCommand, CommandError
from honbot.api_call import get_json

class Command(BaseCommand):
	help = 'This will get hero data and hero usage'

	def handle(self, *args, **options):

		self.stdout.write("Success! Deleted: " + str(count) + ' matches')

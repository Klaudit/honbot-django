from django.core.management.base import BaseCommand, CommandError
from honbot.api_call import get_json
from honbot.models import HeroAll, HeroUseage

class Command(BaseCommand):
	help = 'This will get hero data and hero usage'

	def handle(self, *args, **options):
		data = get_json('/heroes')
		self.stdout.write(data)

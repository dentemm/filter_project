from django.core.management.base import BaseCommand, CommandError
from django.core.mail import send_mail

from datetime import datetime, timedelta

from filter_app.models import Module

class Command(BaseCommand):

	help = 'Adss end date for all festivals'

	def handle(self, *args, **options):

		for module in Module.objects.all():

			if module.time_to_next_swap == 574:

				message = 'De filter leeftijd van module %s van toestel %s wordt over 4 weken bereikt!' % (module.name, module.main_tool.name) 
				send_mail('Filter wissel over 4 weken!', message, 'filters@imec.thinkmobile.webfactional.com', ['tim.claes@live.be', ], fail_silently=False)


				print('nog 4 weken te gaan')

			elif module.time_to_next_swap == 0:

				message = 'De filter leeftijd van module %s van toestel %s is VANDAAG bereikt!' % (module.name, module.main_tool.name) 
				send_mail('Filter leeftijd vervalt vandaag!', message, 'filters@imec.thinkmobile.webfactional.com', ['tim.claes@live.be', ], fail_silently=False)

				print('vandaag wisselen!!!')

			else:
				pass

		self.stdout.write(self.style.SUCCESS('Done!'))
import random
import string

from django.conf import settings

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 4)

def shortcode_generator(size=SHORTCODE_MAX, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=SHORTCODE_MAX):

	shortcode = shortcode_generator(size=size)

	#get the class
	Klass = instance.__class__

	#check if this shortcode already exists
	if Klass.objects.filter(shortcode=shortcode).exists():
		return create_shortcode(instance)
	return shortcode


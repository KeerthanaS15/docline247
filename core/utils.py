import string
from django.utils.text import slugify
import random
from random import shuffle


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):

    if new_slug is not None:
        slug = new_slug
    else:
        val_1 = str(instance.patient)
        val_1 = list(val_1)
        shuffle(val_1)
        val_1 = "".join(val_1)
        slug_1 = slugify(val_1)
        slug_2 = slugify(random_string_generator(size=3))
        slug = slug_1 + slug_2
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4))

        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

import random
import string

from django.test import TestCase
er_code = ''
chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789-_'
for i in range(28):
    a = random.choice(chars)
    er_code+=a
er_code = er_code+'='
print(er_code)

# Create your tests here.

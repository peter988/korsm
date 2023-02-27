from django.contrib import admin

# Register your models here.
from mikeal.models import men, women, kids, handbags, shoes1

admin.site.register(men)
admin.site.register(women)
admin.site.register(kids)
admin.site.register(handbags)
admin.site.register(shoes1)

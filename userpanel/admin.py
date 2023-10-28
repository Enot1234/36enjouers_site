from django.contrib import admin
from .models import Study
from .models import Result
from .models import Test

admin.site.register(Study)
admin.site.register(Result)
admin.site.register(Test)

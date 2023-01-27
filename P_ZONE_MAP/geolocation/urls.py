
from django.urls import path
from .views import *

app_name="geolocation"

urlpatterns = [
	path('',geo,name ='geo'),
	path('proximal/',find_P_ZONE, name="proximal"),
]

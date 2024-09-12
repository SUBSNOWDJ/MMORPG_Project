from django.urls import path
from .views import registration_view, login_view, logout_view, code_conformation_view

urlpatterns = [
    path('registration/', registration_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('code/', code_conformation_view),
]

from django.urls import path
from .views import TicketsList, ticket_edit, UserRespondsList, ticket_create, ticket_responds, UserTicketsList, ticket_detail, respond_conformation, respond_delete, ticket_delete, create_news

urlpatterns = [
    path('', TicketsList.as_view()),
    path('ticket/<int:pk>/edit/', ticket_edit, name='ticket_edit'),
    path('ticket/<int:pk>', ticket_detail, name='ticket_detail'),
    path('responds/', UserRespondsList.as_view()),
    path('my_tickets/', UserTicketsList.as_view()),
    path('create/', ticket_create),
    path('respond/<int:pk>/confirm/', respond_conformation, name='respond_conformation'),
    path('respond/<int:pk>/delete/', respond_delete, name='respond_delete'),
    path('ticket/<int:pk>/delete/', ticket_delete, name='ticket_delete'),
    path('ticket/<int:pk>/responds/', ticket_responds, name='ticket_responds'),
    path('create_news/', create_news)
]

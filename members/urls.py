from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("agent/", views.agent, name="agent"),
    path("customer/", views.customer, name="customer"),
    path("member_login/", views.login_member, name="login"),
    path("member_logout/", views.logout_member, name="logout"),
    path("register/", views.register_member, name="register"),
    path("detail_ticket/<int:ticket_id>/", views.detail_ticket, name="detail_ticket"),
    path("change_password/", views.change_password, name="change_password"),
]
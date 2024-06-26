from django.urls import include,path
from pierzada_app import views
from pierzada_app.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="pierzada/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
    path("image/", views.image, name="image"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout/", views.logout_view, name="logout")
]
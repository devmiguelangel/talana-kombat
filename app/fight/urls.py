from django.urls import path, include
# Views
from fight.views import FightAPIView

urlpatterns = [
    path('fights', FightAPIView.as_view(), name='fight'),
]

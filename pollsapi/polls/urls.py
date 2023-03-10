from django.urls import path
from .views import polls_list, polls_details
from .apiviews import PollList, PollDetails, ChoiceList, CreateVote

urlpatterns = [
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choices_list'),
    path('polls/<int:pk>/choices/<int:choices_pk>/vote/', CreateVote.as_view(), name='create_vote')
]
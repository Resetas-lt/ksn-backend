from django.urls import path

from .views import (
    ContactusView,
    PostsList,
    PostDetails,
    ContactList,
    BudgetReportList,
    FinancesReportList,
    SalaryReportList,
    ProjectList,
)

urlpatterns = [
    path('contactus/', ContactusView.as_view()),
    path('posts/', PostsList.as_view()),
    path('posts/<slug:slug>/', PostDetails.as_view()),
    path('contacts/', ContactList.as_view()),
    path('budget-reports/', BudgetReportList.as_view()),
    path('finances-reports/', FinancesReportList.as_view()),
    path('salary-reports/', SalaryReportList.as_view()),
    path('projects/', ProjectList.as_view()),
]

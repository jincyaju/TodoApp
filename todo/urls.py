"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from crm import views as crm_views #aliasing


from django.conf import settings
from django.conf.urls.static import static

from crmapi import views as api_views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()
router.register("api/employees",api_views.EmployeesView,basename="employees")

router.register("api/v1/employees",api_views.EmployeeViewSetView,basename="memployees")

from todoapi import views as todo_views
router.register("api/users",todo_views.UsersView,basename="users")
router.register("api/todos",todo_views.TodosView,basename="todos")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/add/',views.TodoCreateView.as_view(),name="todo-add"),
    path('todo/all/',views.TodoListView.as_view(),name="todo-list"),
    path('todo/<int:pk>',views.TodoDetailsView.as_view(),name="todo-detail"),
    path('todo/<int:pk>/remove/',views.TodoDeleteView.as_view(),name="todo-delete"),
    path('todo/<int:pk>/change/',views.TodoEditView.as_view(),name="todo-edit"),
    path('todo/completed/',views.TodoCompletedView.as_view(),name="todo-completed"),

    path('emp/add/',crm_views.EmployeeCreateView.as_view(),name="emp-add"),
    path('emp/all/',crm_views.EmployeeListView.as_view(),name="emp-list"),
    path('emp/<int:pk>',crm_views.EmployeeDetailView.as_view(),name="emp-detail"),
    path('emp/<int:pk>/remove/',crm_views.EmployeeDeleteView.as_view(),name="emp-delete"),
    path('emp/<int:pk>/change/',crm_views.EmployeeEditView.as_view(),name="emp-edit"),

    path('register/',crm_views.SignUpView.as_view(),name="register"),
    path('login/',crm_views.SignInView.as_view(),name="signin"),
    path("logout/",crm_views.signout_view,name="signout"),
    path('api/token/',ObtainAuthToken.as_view())




]+router.urls

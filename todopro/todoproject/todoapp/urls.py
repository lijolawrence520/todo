from django.urls import path
from.import views
app_name='todoapp'
urlpatterns = [
      path('',views.add,name="add"),
      # path('details/',views.detail,name="details")
      path('delete/<int:taskid>/',views.delete,name="delete"),
      path('upate/<int:id>/',views.update,name="update"),
      path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
      # path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetail'),
      path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
      path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete'),
]
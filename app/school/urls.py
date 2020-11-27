from django.urls import path
from school import views

app_name = 'school'

urlpatterns = [
    path('category/', views.CategoryListAPIView.as_view(),
         name='category-list'),
    path('category/create/', views.CategoryCreateAPIView.as_view(),
         name='category-create'),
    path('category/<int:pk>/update/', views.CategoryUpdateAPIView.as_view(),
         name='category-update'),
    path('category/<int:pk>/delete/', views.CategoryDestroyAPIView.as_view(),
         name='category-delete'),
    path('category/<int:pk>/view/', views.CategoryRetrieveAPIView.as_view(),
         name='category-view'),

    path('create/', views.SchoolCreateAPIView.as_view(),
         name="create"),
    path('', views.SchoolListAPIView.as_view(), name="list"),
    path('<int:pk>/update/', views.SchoolUpdateAPIView.as_view(),
         name="update"),
    path('<int:pk>/delete/', views.SchoolDeleteAPIView.as_view(),
         name="delete"),
    path('<int:pk>/view/', views.SchoolRetrieveAPIView.as_view(),
         name="view"),

    path('subjects/create/', views.SubjectCreateAPIView.as_view(),
         name='subject-create'),
    path('subjects/',  views.SubjectListAPIView.as_view(),
         name='subject-list'),
    path('subjects/<int:pk>/update/', views.SubjectUpdateAPIView.as_view(),
         name='subject-update'),
    path('subjects/<int:pk>/delete/', views.SubjectDestroyAPIView.as_view(),
         name='subject-delete'),
    path('subjects/<int:pk>/view/', views.SubjectRetrieveAPIView.as_view(),
         name='subject-view'),

    path('levels/', views.LevelListAPIView.as_view(),
         name='level-list'),
    path('levels/create/', views.LevelCreateAPIView.as_view(),
         name='level-create'),
    path('levels/<int:pk>/update/', views.LevelUpdateAPIView.as_view(),
         name='level-update'),
    path('levels/<int:pk>/delete/', views.LevelDestroyAPIView.as_view(),
         name='level-delete'),
    path('levels/<int:pk>/view/', views.LevelRetrieveAPIView.as_view(),
         name='level-view'),
]

from django.urls import path
from school import views

app_name = 'school'

urlpatterns = [

     # category urls
     path('category/', views.CategoryListAPIView.as_view(),
          name='category-list'),
     path('category/public/', views.CategoryPublicListAPIView.as_view(),
          name='category-public-list'),
     path('category/create/', views.CategoryCreateAPIView.as_view(),
          name='category-create'),
     path('category/<int:pk>/update/', views.CategoryUpdateAPIView.as_view(),
          name='category-update'),
     path('category/<int:pk>/delete/', views.CategoryDestroyAPIView.as_view(),
          name='category-delete'),
     path('category/<int:pk>/view/', views.CategoryRetrieveAPIView.as_view(),
          name='category-view'),

     # School urls
     path('create/', views.SchoolCreateAPIView.as_view(),
          name="create"),
     path('', views.SchoolListAPIView.as_view(), name="list"),
     path('public/', views.SchoolPublicListAPIView.as_view(), name="public-list"),
     path('<int:pk>/update/', views.SchoolUpdateAPIView.as_view(),
          name="update"),
     path('<int:pk>/delete/', views.SchoolDeleteAPIView.as_view(),
          name="delete"),
     path('<int:pk>/view/', views.SchoolRetrieveAPIView.as_view(),
          name="view"),

     # Subject urls
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

     # Level url
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

     # Lesson url
     path('lessons/', views.LessonListAPIView.as_view(),
         name='lesson-list'),
     path('lessons/create/', views.LessonCreateAPIView.as_view(),
          name='lesson-create'),
     path('lessons/<int:pk>/update/', views.LessonUpdateAPIView.as_view(),
          name='lesson-update'),
     path('lessons/<int:pk>/delete/', views.LessonDestroyAPIView.as_view(),
          name='lesson-delete'),
     path('lessons/<int:pk>/view/', views.LessonRetrieveAPIView.as_view(),
          name='lesson-view'),

     path('sessions/', views.SessionListAPIView.as_view(),
          name='session-list'),
     path('sessions/create/', views.SessionCreateAPIView.as_view(),
          name='session-create'),
     path('sessions/<int:pk>/update/', views.SessionUpdateAPIView.as_view(),
          name='session-update'),
     path('sessions/<int:pk>/delete/', views.SessionDestroyAPIView.as_view(),
          name='session-delete'),
     path('sessions/<int:pk>/view/', views.SessionRetrieveAPIView.as_view(),
          name='session-view'),

     path('attachments/', views.AttachmentListAPIView.as_view(),
          name='attachment-list'),
     path('attachments/create/', views.AttachmentCreateAPIView.as_view(),
          name='attachment-create'),
     path('attachments/<int:pk>/update/',
          views.AttachmentUpdateAPIView.as_view(),
          name='attachment-update'),
     path('attachments/<int:pk>/delete/',
          views.AttachmentDestroyAPIView.as_view(),
          name='attachment-delete'),
     path('attachments/<int:pk>/view/',
          views.AttachmentRetrieveAPIView.as_view(),
          name='attachment-view'),

     path('moderations/', views.ModerationListAPIView.as_view(),
          name='moderation-list'),
     path('moderations/create/', views.ModerationCreateAPIView.as_view(),
          name='moderation-create'),
     path('moderations/<int:pk>/update/',
          views.ModerationUpdateAPIView.as_view(),
          name='moderation-update'),
     path('moderations/<int:pk>/delete/',
          views.ModerationDestroyAPIView.as_view(),
          name='moderation-delete'),
     path('moderations/<int:pk>/view/',
          views.ModerationRetrieveAPIView.as_view(),
          name='moderation-view'),

]

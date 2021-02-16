from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

urlpatterns = [
    # 함수형 베이스 뷰는 바로 함수 이름을 써주면 되지만, class베이스 뷰는 .as_view()를 붙여줘야한다
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'),
]
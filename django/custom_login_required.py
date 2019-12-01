from functools import wraps
from urllib.parse import urlparse

from django.contrib.auth.decorators import login_required as django_login_required
from django.contrib.auth.views import redirect_to_login
from django.core.handlers.wsgi import WSGIRequest

"""
@login_required 데코레이터의 단점 보완 - from https://lhy.kr/django-post-request-referer-redirect-decorator
login 페이지에서 로그인 후 'next'로 redirect 될 때, next에 post 메서드가 포함될 경우 에러를 일으킨다.
- 인증이 안되었을 경우, HTTP_REFERER를 이용해 로그인 페이지에 접속하기 전 페이지를 next의 주소로 변경 후 redirect_to_login()
    -> 인증된 유저가 아닐 경우, 로그인 페이지로 이동
- 인증된 유저일 경우 post 메서드에 해당하는 view를 실행
    -> 인증된 유저일 경우, post 페이지(예: 게시글 작성, 댓글 작성 등..) 실행
    -> decorator의 arg & kwargs에 사용자가 입력한 데이터를 담고 있기 때문에 
       post 동작이 원활하게 이루어진다.   
"""


def login_required(view_func):
    @wraps(view_func)
    def decorator(*args, **kwargs):
        if args:
            request = args[0]
            # Django의 view에서 첫 번째 매개변수는 HttpRequest타입의 변수(request)이며, 이를 확인한다
            # 또한 요청 메서드가 POST인지 확인
            if isinstance(request, WSGIRequest) and request.method == 'POST':
                # request의 user가 존재하고 인증되어있는지 확인
                user = getattr(request, 'user')
                if user and user.is_authenticated:
                    return view_func(*args, **kwargs)
                # 인증되지 않았을 경우, HTTP_REFERER의 path를 가져온다
                # HTTP_REFERER: 로그인 페이지에 접속하기 전 페이지
                path = urlparse(request.META['HTTP_REFERER']).path
                # 로그인 뷰로 이동하며 GET파라미터의 next값을 path로 지정해주는
                # redirect_to_login함수를 되돌려준다
                return redirect_to_login(path)
        # 위에 해당하지 않는 경우, Django에서 제공하는 기본 login_required를 데코레이터로 사용한다
        return django_login_required(view_func)(*args, **kwargs)

    return decorator

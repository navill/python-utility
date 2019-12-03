from django.contrib.auth.models import User
from django.db import models


"""
[Doc] https://docs.djangoproject.com/en/1.9/ref/models/fields/#django.db.models.ManyToManyField.symmetrical
중개 모델과 monkey patch를 이용한 following & follower 구현
중개 모델(intermediary model): ManyToMany에 사용될 두 모델에 대한 관계(테이블)를 형성하는 모델(Contact)

# 예제의 add_to_class는 아래의 코드와 유사하다 - db를 생성하지 않고 런타임 시 생성되어 사용된다.
(User에 필드를 추가하기 어렵기 때문에 몽키 패치를 이용하였음)

class User(models.Model):
    ...
    following = models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False)
    # self를 참조하기 때문에 user_set은 생성되지 않는다.
    
# symmetrical: 다 대 다 관계가 형성될 때, 서로의 관계에 대한 방향(양방향인가? 단방향인가?)을 설정
symmetrical=True -> if A is B, B is A
symmetrical=False -> A is B, but B is not A


# 예제
python manage.py shell

Contact.objects.get_or_create(user_from=my_user, user_to=target_user)  # Contact(A:B) 관계
user = User.objects.get(id=my_user.id)
user.following.all() -> my_user follows target_user
user.followers.all() -> my_user is followed by None  # following 관계만 형성

Contact.objects.get_or_create(user_from=target_user, user_to=my_user)  # Contact(B:A) 관계
user.followers.all() -> my_user is followed by target_user  # following & follower 관계 형성
"""


class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)


User.add_to_class('following',
                  models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False))

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

"""
[Doc]https://docs.djangoproject.com/en/2.2/ref/contrib/contenttypes/#generic-relations
ContentType: 프로젝트에 포함된 모든 모델을 포함하는 모델(db 테이블)
    -> 모델 동작을 추적하거나 모델간 상호작용을 가농토록 함(generic relation)
    -> limit_choices_to 속성을 이용해 필드를 제한할 수 있다.
content_type: 모델(타입) id값을 foreignkey로 사용(예: user=1, group=2, permission=3....)
object_id: 해당 모델(객체) id(my_user=1, my_user2=2,....)
content_object: GenericForeignKey
"""
class Action(models.Model):
    ...
    content_type = models.ForeignKey(ContentType, blank=True, null=True, related_name='target_obj',
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    # GenericForeignKey에 대한 db는 생성하지 않는다.
    content_object = GenericForeignKey('content_type', 'object_id')

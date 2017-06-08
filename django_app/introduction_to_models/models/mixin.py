"""
Post모델
    author = User와 연결
    title
    content
    created_date
        DateTimeField사용
    modified_date
        DateTimeField사용

Comment모델
    post = Post와 연결
    author = User와 연결
    content
    created_date
    modified_date

User모델
    name
    created_date
    modified_date
"""
from django.db import models
from utils.models.mixins import TimeStampedMixin


class User(TimeStampedMixin):
    name = models.CharField(max_length=50)


class Post(TimeStampedMixin):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    content = models.TextField()
    like_users = models.ManyToManyField(
        User,
        related_name='like_posts',
        through='PostLike',
    )


class Comment(TimeStampedMixin):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    content = models.TextField()


class PostLike(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table = 'introduction_to_models_post_like_users'


"""
1. PostLike, Tag모델 추가
2. Post모델에 like_users MTM필드 추가 및 through선언
3. makemigrations -> migrate잘 되는지 확인
4. Django shell에서 Post의 like_users에 임의의 User추가하고 결과 확인

PostLike
    post = Post
    user = User
    created_date
    
Tag
    title
    
Post모델
    like_users = User와 MTM으로 연결, Intermediate model로 PostLike모델을 사용
    tags = MTM으로 Tag와 연결
    
    def like_post(self, user):
        return '해당 user의 PostLike를 생성, 이후 생성 객체를 리턴'
        
    def add_tag(self, tag_name):
        return '해당 tag_name의 Tag를 생성 또는 기존항목 가져와서 Post에 추가, 이후 Tag리턴'
"""

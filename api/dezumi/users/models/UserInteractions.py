""" User interactions related models """
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from dezumi.shows.models.Show import Show
from dezumi.users.models.User import User
from dezumi.others.models.Individuals import Person
from dezumi.others.models.Utils import BaseModel
from dezumi.social.models.Post import Post


class UserInteraction(models.Model):
    """
    Model for user interactions.
    """

    user = models.OneToOneField(User, related_name="interactions", on_delete=models.CASCADE)

    # User - User
    # https://adamj.eu/tech/2021/02/26/django-check-constraints-prevent-self-following/
    users_follows = models.ManyToManyField('self', through='UserFollow', blank=True, symmetrical=False, related_name='user_follows')
    users_likes = models.ManyToManyField('self', through='UserLike', blank=True, symmetrical=False, related_name='user_likes')

    # User - Shows
    shows_likes = models.ManyToManyField(Show, blank=True, related_name='show_likes')
    shows_dislikes = models.ManyToManyField(Show, blank=True, related_name='show_dislikes')
    shows_favorites = models.ManyToManyField(Show, blank=True, related_name='show_favorites')

    # User - Person 
    # 'user.User' instead of import User because of cirular import error (More: https://stackoverflow.com/a/4379094)
    people_follows = models.ManyToManyField(Person, blank=True, related_name='person_follows')
    people_likes = models.ManyToManyField(Person, blank=True, related_name='person_likes')
    people_favorites = models.ManyToManyField(Person, blank=True, related_name='person_favorites')

    # User - Posts
    posts_likes = models.ManyToManyField(Post, blank=True, related_name='post_likes')

    def __str__(self):
        return self.user.username


class UserFollow(BaseModel):
    """
    Join table between User and User Model
    Represents each follow by a user
    """

    follower = models.ForeignKey(UserInteraction, on_delete=models.CASCADE, related_name='follower')
    followed = models.ForeignKey(UserInteraction, on_delete=models.CASCADE, related_name='followed')

    class Meta:
        constraints = [
            # Prevents more than one follow from one user to another (Ex: 1:Foo -> Bar, 2:Foo -> Bar)
            models.UniqueConstraint(
                name="%(app_label)s_%(class)s_unique_relationships",
                fields=["followed", "follower"],
            ),
            # Prevents the user from following himself
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_prevent_self_follow",
                check=~models.Q(follower=models.F("followed")),
            ),
        ]

    def __str__(self):
        return f'{self.follower} follows {self.followed}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserInteraction.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.interactions.save()


class UserLike(BaseModel):
    """
    Join table between User and User Model
    Represents each follow by a user
    """

    liker = models.ForeignKey(UserInteraction, on_delete=models.CASCADE, related_name='liker')
    liked = models.ForeignKey(UserInteraction, on_delete=models.CASCADE, related_name='liked')

    class Meta:
        constraints = [
            # Prevents more than one like from one user to another (Ex: 1:Foo -> Bar, 2:Foo -> Bar)
            models.UniqueConstraint(
                name="%(app_label)s_%(class)s_unique_relationships",
                fields=["liked", "liker"],
            ),
            # Prevents the user from giving a like to his own profile
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_prevent_self_follow",
                check=~models.Q(liker=models.F("liked")),
            ),
        ]

    def __str__(self):
        return f'{self.liker} likes {self.liked}'

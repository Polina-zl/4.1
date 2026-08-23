from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Post
from .tasks import notify_subscribers_about_new_post


@receiver(m2m_changed, sender=Post.categories.through)
def notify_subscribers_on_new_post(sender, instance, action, **kwargs):
    """
    Когда пост добавляется в категорию, отправляем письма подписчикам АСИНХРОННО через Celery
    """
    if action == 'post_add':
        categories = instance.categories.all()
        for category in categories:
            notify_subscribers_about_new_post.delay(instance.id, category.id)
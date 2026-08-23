from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from .models import Post, Category


@shared_task
def notify_subscribers_about_new_post(post_id, category_id):
    """Асинхронная отправка уведомлений подписчикам о новой статье"""
    post = Post.objects.get(id=post_id)
    category = Category.objects.get(id=category_id)
    subscribers = category.subscribers.all()

    for subscriber in subscribers:
        send_mail(
            subject=f'Новая статья в категории "{category.name}": {post.title}',
            message=f'Здравствуй, {subscriber.username}!\n\n'
                    f'Новая статья в твоём любимом разделе "{category.name}":\n\n'
                    f'{post.preview()}\n\n'
                    f'Читать полностью: http://127.0.0.1:8000/news/{post.id}/',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[subscriber.email],
            fail_silently=True,
        )

    return f'Уведомления отправлены {subscribers.count()} подписчикам'


@shared_task
def weekly_newsletter():
    """Еженедельная рассылка новых статей за неделю"""
    week_ago = timezone.now() - timedelta(days=7)
    categories = Category.objects.all()

    for category in categories:
        new_posts = category.post_set.filter(created_at__gte=week_ago)
        if not new_posts.exists():
            continue

        posts_html = '<ul>'
        for post in new_posts:
            posts_html += f'<li><a href="http://127.0.0.1:8000/news/{post.id}/">{post.title}</a> - {post.preview()}</li>'
        posts_html += '</ul>'

        for subscriber in category.subscribers.all():
            send_mail(
                subject=f'Новые статьи в категории "{category.name}" за неделю',
                message=f'Здравствуй, {subscriber.username}!\n\n'
                        f'За прошедшую неделю в категории "{category.name}" появились новые статьи:\n\n'
                        f'Ссылки на статьи: http://127.0.0.1:8000/news/',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[subscriber.email],
                fail_silently=True,
                html_message=f'<h2>Здравствуй, {subscriber.username}!</h2>'
                             f'<p>За прошедшую неделю в категории "{category.name}" появились новые статьи:</p>'
                             f'{posts_html}'
                             f'<p><a href="http://127.0.0.1:8000/news/">Перейти на портал</a></p>',
            )

    return 'Еженедельная рассылка завершена'
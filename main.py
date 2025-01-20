import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_lesson.settings")
django.setup()

from orm_test.models import Author, Post

# author = Author.objects.create(name="Denys", age=20, email="sdgsfdf")
# print(author)

author = Author.objects.get(id=1)
print(author)
# post = Post.objects.create(title="POSTIK", body="ttttteeexxt",
#                            author=author)
post = Post.objects.filter(author=author).first()

print(post)
print(post.created_at)
print(post.updated_at)
# post.body = "KKKKKKKK"
# post.save()
print(author.posts.all())
# Steps

## step-9 --> go to setting.py > (within line_no. 30)INSTALLED_APPS ['blog.apps.BlogConfig',]

## step-10 --> Run the following command in the shell prompt to open the Python shell:
"""
python manage.py shell
"""

## step-11 --> Then, type the following lines:
"""
> > > from blog.models import Post
> > > Post.Status.choices
> > > Post.Status.labels
> > > Post.Status.values
> > > Post.Status.names
> > >
> > > """

## step-14 --> Run the following command in the shell prompt from the root directory of your project:
"""
python manage.py makemigrations blog
"""

## step-15 --> Run the following command from the shell prompt to inspect the SQL output of your first migration:
"""
python manage.py sqlmigrate blog 0001
"""

## step-16 --> Execute the following command in the shell prompt to apply existing migrations:
"""
python manage.py migrate
"""

## step-17 --> First, you will need to create a user to manage the administration site. Run the following command:
"""
python manage.py createsuperuser
"""

## step-18 --> Creating objects
# Run the following command in the shell prompt to open the Python shell:
"""
python manage.py shell
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
>>> user = User.objects.get(username='username')
>>> post = Post(title='Another post',
    ... slug='another-post',
    ... body='Post body.',
    ... author=user)
>>> post.save()

>>> all_posts = Post.objects.all() 

"""

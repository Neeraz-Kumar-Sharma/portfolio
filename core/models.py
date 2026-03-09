from django.db import models


class Project(models.Model):
    """Represents a portfolio project."""

    CATEGORY_CHOICES = [
        ('security', 'Security'),
        ('backend',  'Backend'),
        ('fullstack', 'Full Stack'),
        ('systems',  'Systems / C++'),
        ('java',     'Java / OOP'),
    ]

    title       = models.CharField(max_length=120)
    category    = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    emoji       = models.CharField(max_length=10, default='🔐')
    description = models.TextField()
    tags        = models.CharField(max_length=255, help_text='Comma-separated tags, e.g. Python,Django,SQLite')
    github_url  = models.URLField(blank=True, null=True)
    order       = models.PositiveSmallIntegerField(default=0, help_text='Display order (lower = first)')
    is_visible  = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return self.title

    def tag_list(self):
        """Returns tags as a Python list."""
        return [t.strip() for t in self.tags.split(',') if t.strip()]

    def category_display(self):
        return self.get_category_display().upper()


class Skill(models.Model):
    """Represents a skill/technology card."""

    LEVEL_CHOICES = [
        ('strong',       'Strong'),
        ('good',         'Good'),
        ('learning',     'Learning'),
        ('basics',       'Basics'),
    ]

    name    = models.CharField(max_length=60)
    emoji   = models.CharField(max_length=10)
    level   = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    order   = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.name} ({self.level})'

    def level_display(self):
        return self.get_level_display().upper()


class ContactMessage(models.Model):
    """Stores messages submitted via the contact form."""

    name       = models.CharField(max_length=100)
    email      = models.EmailField()
    subject    = models.CharField(max_length=200)
    message    = models.TextField()
    is_read    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'[{self.created_at.strftime("%Y-%m-%d")}] {self.name} — {self.subject}'

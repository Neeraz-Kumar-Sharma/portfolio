from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill
from .forms import ContactForm

SKILLS_DATA = [
    {'name': 'Python',        'emoji': '🐍', 'level': 'STRONG'},
    {'name': 'Java',          'emoji': '☕', 'level': 'GOOD'},
    {'name': 'C++',           'emoji': '⚙️', 'level': 'GOOD'},
    {'name': 'Django',        'emoji': '🦄', 'level': 'GOOD'},
    {'name': 'HTML / CSS',    'emoji': '🌐', 'level': 'GOOD'},
    {'name': 'JavaScript',    'emoji': '🔷', 'level': 'LEARNING'},
    {'name': 'Linux / Kali',  'emoji': '🐧', 'level': 'BASICS'},
    {'name': 'Networking',    'emoji': '📡', 'level': 'BASICS'},
    {'name': 'SQL / SQLite',  'emoji': '🗄️', 'level': 'GOOD'},
    {'name': 'Secure Coding', 'emoji': '🔒', 'level': 'LEARNING'},
    {'name': 'Nmap Basics',   'emoji': '🔎', 'level': 'BASICS'},
    {'name': 'Git / GitHub',  'emoji': '🐙', 'level': 'GOOD'},
]

PROJECTS_DATA = [
    {
        'emoji': '🔐', 'type': 'DJANGO · PYTHON',
        'title': 'Secure Login System',
        'desc': 'Full authentication system with hashed passwords, session management, CSRF protection, and brute-force rate limiting built with Django.',
        'tags': ['Python', 'Django', 'SQLite', 'HTML/CSS'],
        'github': '',
    },
    {
        'emoji': '📡', 'type': 'PYTHON · NETWORKING',
        'title': 'Network Scanner',
        'desc': 'Python script using socket library and Nmap to scan a local network, detect open ports, and display results in a clean CLI interface.',
        'tags': ['Python', 'Socket', 'Nmap', 'CLI'],
        'github': '',
    },
    {
        'emoji': '🌐', 'type': 'FULL STACK',
        'title': 'Personal Blog CMS',
        'desc': 'Content management system with admin panel, user auth, Markdown support and REST API backend. Deployed with security headers configured.',
        'tags': ['Django', 'REST API', 'JS', 'CSS3'],
        'github': '',
    },
    {
        'emoji': '🔑', 'type': 'PYTHON · SECURITY',
        'title': 'Password Manager CLI',
        'desc': "Command-line password manager with AES encryption using Python's cryptography library. Stores credentials in an encrypted local vault.",
        'tags': ['Python', 'Cryptography', 'AES', 'CLI'],
        'github': '',
    },
    {
        'emoji': '📊', 'type': 'C++ · ALGORITHMS',
        'title': 'Data Structures Library',
        'desc': 'Implementation of core data structures (BST, Hash Table, Graph) in C++ with benchmarking and memory management demonstrations.',
        'tags': ['C++', 'Algorithms', 'OOP'],
        'github': '',
    },
    {
        'emoji': '🗒️', 'type': 'JAVA · OOP',
        'title': 'Student Management App',
        'desc': 'Java desktop app for managing student records using OOP principles — inheritance, polymorphism, file I/O, and a simple Swing GUI.',
        'tags': ['Java', 'Swing', 'OOP', 'File I/O'],
        'github': '',
    },
]

PROFICIENCY = [
    {'name': 'Python',                 'pct': 85},
    {'name': 'Java',                   'pct': 75},
    {'name': 'C++',                    'pct': 70},
    {'name': 'Django / Web Backend',   'pct': 75},
    {'name': 'HTML / CSS / JS',        'pct': 70},
    {'name': 'Networking Fundamentals','pct': 55},
    {'name': 'Linux / Kali Basics',    'pct': 60},
]


def index(request):
    form = ContactForm()
    form_success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            form_success = True
            form = ContactForm()

            # Send email
            try:
                send_mail(
                    subject=f"[Portfolio] {contact.subject}",
                    message=f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Email error: {e}")
                pass

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'status': 'ok', 'message': 'Message sent!'})
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'errors': 'Invalid form'}, status=400)

    db_projects = Project.objects.filter(is_visible=True)
    db_skills   = Skill.objects.all()

    context = {
        'form':         form,
        'form_success': form_success,
        'projects':     db_projects if db_projects.exists() else PROJECTS_DATA,
        'skills':       db_skills   if db_skills.exists()   else SKILLS_DATA,
        'proficiency':  PROFICIENCY,
        'use_db':       db_projects.exists(),
    }
    return render(request, 'core/index.html', context)
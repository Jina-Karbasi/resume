from django.shortcuts import render

def index_view(request):
    context = {
        "name": "Jina Farahmand",
        "job_title": "Python Developer",
        "email": "Jinaexample@yahoo.com",
        "city": "Berlin",
        "bio": "I am a Python developer interested in web development",
        "header": "Grow, innovate, and succeed online.",
        "hint": "I build modern web applications to help businesses",
    }
    return render(request, 'core/index.html', context)

def contact_view(request):
    return render(request, 'core/contact.html')

def projects_view(request):
    context = {
        "projectname1": "Personal Resume Website",
        "explain1": "Designed and developed a responsive personal portfolio website using Python, Django, HTML, CSS, and Bootstrap. The website showcases personal information, education, technical skills, projects, and contact details.",
        "projectname2": "Task Management Web Application",
        "explain2": "Developed a task management web application using Django and Python. Users can create, edit, delete, and organize their daily tasks through a simple and user-friendly interface. The project helped improve my understanding of Django views, templates, URLs, and database operations.",
    }
    return render(request, 'core/projects.html', context)

def resume_view(request):
    context = {
        "present_job" : "Secretary",
        "present_company": "Doreh Sara",
        "present_loc": "Iran, Tehran",
        "explain": "Scheduling Classes and Registration Online Support Providing Guides for registrations",
        "ex_job": "Project Control Expert",
        "ex_company": "Saze Gostaran Arak",
        "ex_loc": "Arak",
        "explain2": " Planning and Scheduling Projects Checking, Preparing, and Reporting Work ProgressEstimating and Monitoring Project Costs to Minimize Total Cost",
        "edg_year": "Sep. 2015 – Feb. 2021",
        "colage": "Azad University West Tehran Branch",
        "location": "Tehran, Iran",
        "degree": "Master of Science",
        "ex_year": "Sep. 2007 – Feb. 2014",
        "ex_colage": "Islamic Azad University Malayer Branch",
        "degree2": "Bachelor of Science",
        "ex_location": "Hamedan , Iran",
        "skill1": "Microsoft Office Suite (Word, Excel, PowerPoint)",
        "skill2": "Primavera P6",
        "skill3": "Matlab",
        "skill4": "Operating System: Windows",
        "skill5": "Minitab",
        "skill6": "Arena",
        "lang1": "Django",

    }
    return render(request, 'core/resume.html', context)




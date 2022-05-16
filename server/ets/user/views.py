from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'user/login.html',{'nbar': 'login','role':'manager'})

def dispProfile(request):
    user = {
        'name': 'name-abc',
        'role': 'Role-abc',
        'joined_on': 'joining-abc',
        'office_branch': 'branch-abc',
        'dob': 'DOB-abc',
        'address': 'address-abc',
        'contact': 'contact-abc',
        'email': 'email-abc',
    }
    team = {
        'dept': 'dept-abc',
        'team_name': 'team-name',
        'no_members': 'no-abc',
        'manager': 'manager-abc',
        'team_members': [
            {'m_name':'m1_name', 'm_role':'m1_role'},
            {'m_name':'m3_name', 'm_role':'m2_role'},
            {'m_name':'m3_name', 'm_role':'m3_role'},
        ],
    }
    context = {
        'user': user,
        'team': team,
        'nbar': 'home','role':'manager'
    }
    return render(request,'user/profile.html', context)

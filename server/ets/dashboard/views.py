from django.shortcuts import render

# Create your views here.

def view_dashboard(request):
     return render(request,'dashboard/dashboard_home.html',{'nbar': 'home','role':'manager'})

def get_team_data():
     teams_data=[
        {"member_name":"isha","team_name":"abcd","department":"Software Engineering","prod_per":70,"unprod_per":25,"break_per":5},
        {"member_name":"saket","team_name":"xyz","department":"Sales","prod_per":70,"unprod_per":25,"break_per":5},
        {"member_name":"mahi","team_name":"abcd","department":"Software Engineering","prod_per":70,"unprod_per":25,"break_per":5},
        {"member_name":"manan","team_name":"xyz","department":"Sales","prod_per":70,"unprod_per":25,"break_per":5},
        {"member_name":"emp5","team_name":"deal","department":"Sales","prod_per":70,"unprod_per":25,"break_per":5},
        {"member_name":"emp6","team_name":"deal","department":"Sales","prod_per":70,"unprod_per":25,"break_per":5},
        {"member_name":"emp7","team_name":"deal","department":"Sales","prod_per":70,"unprod_per":25,"break_per":5},
        ]
     team_names_list=set()
          
     for i in range(len(teams_data)):
          team_names_list.add(teams_data[i]["team_name"])
          
     team_names_list=list(team_names_list)
     teams=[]
          
          
     for i in range(len(team_names_list)):
          count=0
          teams_dict={}
          for j in range(len(teams_data)):
               if(teams_data[j]["team_name"]==team_names_list[i]):
                    count=count+1
          
          for k in range(len(teams_data)):
               if(teams_data[k]["team_name"]==team_names_list[i]):
                    teams_dict["team_name"]= teams_data[k]["team_name"]  
                    teams_dict["department"]=teams_data[k]["department"]  
                    teams_dict["number"]=count
                    teams.append(teams_dict)
                    break
     return teams_data,team_names_list,teams

def view_teams(request):
     teams_data,team_names_list,teams=get_team_data()
     context = {
        'nbar': 'teams',
        'role':'manager',
        "teams" : teams,
    }
     return render(request,'dashboard/teams.html',context)

def view_team_details(request,teamname):
     teams_data,team_names_list,teams=get_team_data()
     team_details=[]
     member_details=[]
     for i in range(len(teams_data)):
          if(teams_data[i]["team_name"]==teamname):
               member_details.append(teams_data[i])
          

     for i in range(len(teams)):
          if(teams[i]["team_name"]==teamname):
               team_details=teams[i]
     print(team_details)
     context = {
        'nbar': 'teams',
        'role':'manager',
        "member_details" : member_details,
        "team_details":team_details
    }
     return render(request,'dashboard/team_details.html',context)

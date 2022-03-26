import subprocess
import os
import sys


def setup_schtask():
    script_path = os.path.dirname(os.path.abspath(__file__))
    bat_path = script_path
    vbs_path = script_path + "\\run_script.vbs"
    script_path += "\\run_schtask.bat"
    bat_path = os.path.join(bat_path, "run_schtask.bat")
    with open(vbs_path, "w") as f:
        vbs_command = '''
            'this vbs file is used to run the script.py
            CreateObject("Wscript.Shell").Run "pythonw.exe ""{}"" ",0,True 
        '''.format(
            
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "script.py"),
        )
        print(vbs_command)
        f.write(vbs_command)
        f.close()
    command = '''schtasks /create /tn runpy /sc minute /mo 1 /tr "wscript.exe \\"{}\\"" '''.format(vbs_path)

    # command = '''schtasks /create /tn runpy /sc minute /mo 1 /tr "'{}', Arguments" '''.format(script_path)
    # command = '''schtasks /create /tn runpy /sc minute /mo 1 /tr "wscript.exe \"D:\\mahi\\Projects\\Employee Tracking\\Employee-activity-monitoring-application\\run_script.vbs\"" '''
    # command = '''schtasks /create /tn runpy /sc minute /mo 1 /tr "powershell.exe -Hidden -file '{}', Arguments" '''.format(script_path)
    
    subprocess.call(command)
    # os.system("SCHTASKS /Create /XML runpy.xml /TN runpy /F")  
    # os.system(command)
    # os.system("schtasks /run /tn runpy")

    # command="$taskAction = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument 'py '{}''".format(script_path)
    # subprocess.call(command)
    # subprocess.call("Set-ScheduledTask 'runpy' -Action $taskAction")

    # subprocess.call("create_task.bat")
    command="powershell.exe -ExecutionPolicy RemoteSigned -file modify_schtask.ps1"
    # os.system(command)
    p = subprocess.Popen(command, stdout=sys.stdout)
    p.communicate()
    return True

if __name__ == "__main__":
    setup_schtask()

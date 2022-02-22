import subprocess
import os


def setup_schtask():
    script_path = os.path.dirname(os.path.abspath(__file__))
    bat_path = script_path
    script_path += "\\run_schtask.bat"
    bat_path = os.path.join(bat_path, "run_schtask.bat")
    with open(bat_path, "w") as f:
        bat_command = """
            :: this batch file is used to run the script.py
            py {}
        """.format(
            
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "script.py"),
        )
        print(bat_command)
        f.write(bat_command)
        f.close()
    # command = "schtasks /create /tn runpy /sc minute /mo 1 /tr '{}'".format(script_path)
    # print(command)
    os.system("SCHTASKS /Create /XML runpy.xml /TN runpy /F")   
    # print(command)
    # subprocess.call(command)
    subprocess.call("schtasks /run /tn runpy")
    return True


if __name__ == "__main__":
    setup_schtask()

import subprocess
import os

PATH_VMRUN = r"C:\Program Files (x86)\VMware\VMware Workstation\vmrun.exe"
PATH_VMX = r"K:\May1\Windows-1.vmx"

list_program = {
    r"C:\Program Files\Google\Chrome\Application\chrome.exe" : "Google Chrome",
    r"C:\Program Files\Mozilla Firefox\firefox.exe" : "Mozilla Firefox",
    r"C:\Windows\System32\notepad.exe" : "Notepad",
    }

VM_USER = "admin"
VM_PASSWORD = "123"


def start_vm():
    subprocess.run([PATH_VMRUN, "start", PATH_VMX])
    print("VM Started")


def stop_vm():
    subprocess.run([PATH_VMRUN, "stop", PATH_VMX])
    print("VM Stopped")


def restart_vm():
    subprocess.run([PATH_VMRUN, "reset", PATH_VMX])
    print("VM Restarted")


def display_vm():
    subprocess.run([PATH_VMRUN, "list"])
    print("VM Displayed")


def show_ip():
    subprocess.run([PATH_VMRUN, "getGuestIPAddress", PATH_VMX])
    print("System Info")


def show_configuration_VM():
    info = {}
    with open(PATH_VMX, "r") as file:
        for line in file:
            if line.startswith('displayName'):
                name, value = line.split(" = ")
                value = value.strip().strip('"')
                info["Ten May"] = value
            if line.startswith('memsize'):
                name, value = line.split(" = ")
                value = value.strip().strip('"')
                value = int(float(value) / 1024)
                info["RAM"] = str(value) + "GB"
            if line.startswith('numvcpus'):
                name, value = line.split(" = ")
                value = value.strip().strip('"')
                info["NHAN CPU"] = value
            if line.startswith('guestOS'):
                name, value = line.split(" = ")
                value = value.strip().strip('"')
                info["He Dieu Hanh"] = value
            if line.startswith('ethernet0.generatedAddress'):
                name, value = line.split(" = ")
                value = value.strip().strip('"')
                info["IP MAC"] = value
            if line.startswith('sound.present'):
                name, value = line.split(" = ")
                value = value.strip().strip('"')
                info["SOUND"] = value
            if line.startswith('ethernet0.present'):
                name, value = line.split(" = ")
                value = value.strip().strip('"')
                info["CARD MANG KICH HOAT"] = value

    for key, value in info.items():
        print(f"{key}: {value}")


def check_program_installed():
    for program_path, program_name in list_program.items():
        try:
            subprocess.run([PATH_VMRUN, '-gu', VM_USER, '-gp', VM_PASSWORD, 'runProgramInGuest', PATH_VMX, '-noWait', program_path], capture_output=True, text=True, check=True)
            print(f"{program_name} is installed and successfully executed.")
        except subprocess.CalledProcessError as e:
            print(f"{program_name} is not installed.")



def check_listProcessesInGuest():
        command = [PATH_VMRUN, "-T", "ws", "-gu", VM_USER, "-gp", VM_PASSWORD, "listProcessesInGuest", PATH_VMX,
                   "-interactive"]
        try:
            process = subprocess.run(command, capture_output=True, text=True, check=True)
            print("Processes running in the guest:")
            print(process.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            print("Failed to list processes in the guest.")

def find_PID_by_name(name):
    command = [PATH_VMRUN, "-T", "ws", "-gu", VM_USER, "-gp", VM_PASSWORD, "listProcessesInGuest", PATH_VMX, "-interactive"]
    try:
        process = subprocess.run(command, capture_output=True, text=True, check=True)
        for line in process.stdout.splitlines():
            if name in line:
                n = ""
                for i in line.split()[0]:
                    if i.isdigit():
                        n += i
                return n
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Failed to find process with name {name}.")
        return None

def kill_process():
    process_id = find_PID_by_name("notepad.exe")
    command = [PATH_VMRUN, "-T", "ws", "-gu", VM_USER, "-gp", VM_PASSWORD, "killProcessInGuest", PATH_VMX, process_id]
    try:
        subprocess.run(command, check=True)
        print(f"Process with ID {process_id} killed.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print(f"Failed to kill process with ID {process_id}.")

def update_vm():
    command = [PATH_VMRUN, "upgradevm", PATH_VMX]
    try:
        stop_vm()
        import time
        time.sleep(5)
        subprocess.run(command, check=True)
        print("VM upgraded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Failed to upgrade VM.")

def send_file_to_guest():
    path_host = r"C:\Users\admin\Downloads\winrar-x64-700.exe"
    path_guest = r"C:\Users\admin\Desktop\winrar-x64-700.exe"
    command = [PATH_VMRUN, "-T", "ws", "-gu", VM_USER, "-gp", VM_PASSWORD, "copyFileFromHostToGuest", PATH_VMX, path_host, path_guest]
    try:
        subprocess.run(command, check=True)
        print("File sent successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        print("Failed to send file.")
    return path_guest

def install_program():
    pathh = send_file_to_guest()
    subprocess.run(
        [PATH_VMRUN, '-gu', VM_USER, '-gp', VM_PASSWORD, 'runProgramInGuest', PATH_VMX, '-interactive', pathh],
        capture_output=True, text=True, check=True)
    print("Program installed and successfully executed.")


def main():
    print("1. Start VM")
    print("2. Stop VM")
    print("3. Restart VM")
    print("4. Display VM")
    print("5. Show IP")
    print("6. Show Configuration VM")
    print("7. Check Program Installed")
    print("8. Check List Processes In Guest")
    print("9. Kill Process")
    print("10. Update VM")
    print("11. Send File To Guest")
    print("12. Install Program")
    print("0. Exit")
    while True:
        choice = input("Your choice: ")
        if choice == "1":
            start_vm()
        elif choice == "2":
            stop_vm()
        elif choice == "3":
            restart_vm()
        elif choice == "4":
            display_vm()
        elif choice == "5":
            show_ip()
        elif choice == "6":
            show_configuration_VM()
        elif choice == "7":
            check_program_installed()
        elif choice == "8":
            check_listProcessesInGuest()
        elif choice == "9":
            kill_process()
        elif choice == "10":
            update_vm()
        elif choice == "11":
            send_file_to_guest()
        elif choice == "12":
            install_program()
        elif choice == "0":
            exit()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

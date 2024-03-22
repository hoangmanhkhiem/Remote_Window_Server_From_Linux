import paramiko

def power_on_vm(vm_name):
    # Kết nối SSH đến máy chủ Windows
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname="IP_Address_or_FQDN_of_Windows_Server", username="username", password="password")

    # Thực thi lệnh để bật máy ảo
    ssh_client.exec_command("vmrun start 'path_to_your_vm.vmx'")

    # Đóng kết nối SSH
    ssh_client.close()

def power_off_vm(vm_name):
    # Kết nối SSH đến máy chủ Windows
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname="IP_Address_or_FQDN_of_Windows_Server", username="username", password="password")

    # Thực thi lệnh để tắt máy ảo
    ssh_client.exec_command("vmrun stop 'path_to_your_vm.vmx'")

    # Đóng kết nối SSH
    ssh_client.close()

def list_running_vms():
    # Kết nối SSH đến máy chủ Windows
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname="IP_Address_or_FQDN_of_Windows_Server", username="username", password="password")

    # Thực thi lệnh để liệt kê các máy ảo đang chạy
    stdin, stdout, stderr = ssh_client.exec_command("vmrun list")

    # Đọc kết quả trả về
    output = stdout.read().decode("utf-8")

    # In ra danh sách các máy ảo đang chạy
    print("Các máy ảo đang hoạt động:")
    print(output)

    # Đóng kết nối SSH
    ssh_client.close()

# Thực hiện các thao tác cần thiết
power_on_vm("your_vm_name")
power_off_vm("your_vm_name")
list_running_vms()

$Url = "https://dl.google.com/chrome/install/GoogleChromeStandaloneEnterprise.msi"
$InstallerPath = "$env:TEMP\GoogleChromeInstaller.msi"
Invoke-WebRequest -Uri $Url -OutFile $InstallerPath
Start-Process -FilePath msiexec.exe -ArgumentList "/i $InstallerPath /quiet /qn /norestart" -Wait

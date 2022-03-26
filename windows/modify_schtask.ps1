# set taskSettings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
# set taskName = "runpy"
$taskSettings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -Hidden
$taskName = "runpy"
Set-ScheduledTask -TaskName $taskName -Settings $taskSettings
Start-ScheduledTask -TaskName $taskName
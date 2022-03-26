# set taskSettings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
# set taskName = "runpy"
$taskSettings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
$taskName = "runpy"
Set-ScheduledTask -TaskName $taskName -Settings $taskSettings
Start-ScheduledTask -TaskName runpy
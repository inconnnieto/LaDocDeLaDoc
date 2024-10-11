# 1_Prima

Écrivez un script (sh ou ps ou les deux) qui permet de 
vérifier que Firefox, Chrome, Python et Node sont 
installés et que 2 + 2 fait bien 4.

``` ps1
$node = node --version
$python = python --version
$chrome = $(Get-Package -Name "Google Chrome").Version
$firefox = $(Get-Package -Name "Mozilla Firefox (x64 fr)").Version

$result = 2 + 2

Write-Host "Node Version : $node"
Write-Host "Python Version : $python"
Write-Host "Chrome Version : $chrome"
Write-Host "Firefox Version : $firefox"
Write-Host " 2 + 2 = $result" 
```
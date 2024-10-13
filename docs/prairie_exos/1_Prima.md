# 1_Prima

### brief:
Write a script (sh, ps or both) that checks if Firefox, Chrome, Python and Node are installed, and also checks that 2 + 2 equals 4.

Task objectives:

programs to check:
* Firefox
* Chrome
* Python
* Node.js

check:
* version of each program
* confirm (2 + 2) = 4

### Notes
the arithmetic operation check to ensure script runs without errors.

What does `$` represent?
In PowerShell(& other scripting languages), `$` symbol is used to denote a variable.

`$variableName` refers to a placeholder for data. Variables in PowerShell are dynamic, you don’t have to declare their type in advance.

### My attempt:

PowerShell script that runs on a Windows environment and checks the version of the programs

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

Expected output:
```Node Version : v14.17.0
Python Version : 3.9.5
Chrome Version : 90.0.4430.85
Firefox Version : 88.0.1
2 + 2 = 4
```
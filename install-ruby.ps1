# Install Ruby + Jekyll for mikemalburg.com

$rubyZipUrl = "https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-3.2.2-1/rubyinstaller-3.2.2-1-x64.7z"
$rubyPath = "C:\Tools\ruby"

Write-Host "Creating directory..."
New-Item -ItemType Directory -Path $rubyPath -Force | Out-Null

Write-Host "Downloading Ruby..."
$response = Invoke-WebRequest -Uri $rubyZipUrl -OutFile "$env:TEMP\ruby.7z" -UseBasicParsing
if ($response.StatusCode -ne 200) {
    Write-Host "Fallback to standard release..."
    $rubyZipUrl = "https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-3.2.2-1/rubyinstaller-3.2.2-1-x64.exe"
    Invoke-WebRequest -Uri $rubyZipUrl -OutFile "$env:TEMP\ruby-installer.exe" -UseBasicParsing
    Write-Host "Running interactive installer..."
    Start-Process -FilePath "$env:TEMP\ruby-installer.exe" -Wait
} else {
    Write-Host "Extracting Ruby..."
    if (-not (Get-Command 7z -ErrorAction SilentlyContinue)) {
        Write-Host "Installing 7-Zip..."
        winget install 7zip.7zip --silent
    }
    & 7z x "$env:TEMP\ruby.7z" "-o$rubyPath" | Out-Null
    
    # Add to user PATH
    $currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
    [Environment]::SetEnvironmentVariable("Path", "$rubyPath\bin;$currentPath", "User")
    
    Write-Host "Restart your PowerShell session and run:"
    Write-Host "  gem install bundler jekyll"
    Write-Host "Then in mikemalburg.com directory:"
    Write-Host "  bundle install && jekyll build"
}

# Define the old and new strings
$oldString = "https://nanma80.github.io/"
$newString = "https://www.nan.ma/"

# Get the current script file name
$currentScript = $MyInvocation.MyCommand.Definition

# Get all files in the current directory and subdirectories
$files = Get-ChildItem -Recurse -File

foreach ($file in $files) {
    # Skip the current script file
    if ($file.FullName -eq $currentScript) {
        continue
    }

    # Read the file content
    $content = Get-Content -Path $file.FullName -Raw
    
    # Check if the file contains the old string
    if ($content -match [regex]::Escape($oldString)) {
        # Replace the old string with the new string
        $updatedContent = $content -replace [regex]::Escape($oldString), $newString
        
        # Write the updated content back to the file only if there was a match
        Set-Content -Path $file.FullName -Value $updatedContent

        Write-Output "Updated file: $($file.FullName)"
    }
}

Write-Output "String replacement complete."

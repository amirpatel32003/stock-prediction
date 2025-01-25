# Name of your project
$PROJECT_NAME = "stock-prediction"

# 1. Create project folder
New-Item -ItemType Directory -Name $PROJECT_NAME -Force | Out-Null
Set-Location $PROJECT_NAME

# 2. Create a virtual environment (optional but recommended)
python -m venv venv

# 3. Create subfolders
New-Item -ItemType Directory -Name "data" -Force | Out-Null
New-Item -ItemType Directory -Name "data/raw" -Force | Out-Null
New-Item -ItemType Directory -Name "data/processed" -Force | Out-Null
New-Item -ItemType Directory -Name "notebooks" -Force | Out-Null
New-Item -ItemType Directory -Name "src" -Force | Out-Null
New-Item -ItemType Directory -Name "webapp" -Force | Out-Null

# 4. Create initial files
New-Item -ItemType File -Name "README.md" | Out-Null
New-Item -ItemType File -Name "requirements.txt" | Out-Null
New-Item -ItemType File -Name ".gitignore" | Out-Null

# 5. Add a basic Python .gitignore template
@"
# Python cache
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
venv/
.venv/

# Jupyter Notebook checkpoints
.ipynb_checkpoints/

# VSCode settings
.vscode/
"@ | Out-File -FilePath .gitignore -Encoding utf8

# 6. (Optional) Initialize a Git repository
git init | Out-Null

Write-Host "Project '$PROJECT_NAME' has been set up!"
Write-Host "Navigate into the directory using: cd $PROJECT_NAME"

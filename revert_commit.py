import subprocess
import os

os.chdir(r'c:\PythonProjects\maketables')

# First, abort any ongoing revert
subprocess.run(['git', 'revert', '--abort'], capture_output=True)

# Reset to current HEAD
subprocess.run(['git', 'reset', '--hard', 'HEAD'], check=True)

# Now revert the commit without committing
result = subprocess.run(['git', 'revert', '4367d01', '--no-commit'], capture_output=True, text=True)
print("Revert output:", result.stdout)
print("Revert errors:", result.stderr)

# Remove problematic cache files
subprocess.run(['git', 'rm', '--cached', '-r', 'maketables/__pycache__'], capture_output=True)
subprocess.run(['git', 'checkout', 'HEAD', 'maketables/__pycache__'], capture_output=True)

# Stage all changes
subprocess.run(['git', 'add', '.'], check=True)

# Commit
subprocess.run(['git', 'commit', '-m', 'Revert "Render significance levels in math mode in latex"'], check=True)

print("\nCommit reverted successfully!")
subprocess.run(['git', 'log', '--oneline', '-5'])

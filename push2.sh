#!/bin/bash

echo "Enter the path to your local repository (or open Git Bash within the repository and type 'pwd'):"
read folder_path

if [[ ! -d "$folder_path" ]]; then
  echo "Invalid path. Please enter the correct directory."
  exit 1
fi

cd "$folder_path" || exit


if ! git init > /dev/null 2>&1; then 
  echo "Repository not initialized. Initializing..."
  git init
fi


echo "Do you want to add all files to the staging area (y/n)?"
read -r answer

if [[ "$answer" =~ ^[Yy]$ ]]; then
  git add .
elif [[ "$answer" =~ ^[Nn]$ ]]; then
  echo "Enter specific files to add (separate by spaces, or 'none' if no specific files):"
  read -r specific_files

  if [[ "$specific_files" != "none" ]]; then
    git add $specific_files
  fi
else
  echo "Invalid input. Please enter 'y' or 'n'."
  exit 1
fi

echo "Enter a commit message:"
read -r commit_message

if ! git remote -v | grep origin >/dev/null 2>&1; then
  echo "Remote named 'origin' not found. Do you want to add one (y/n)?"
  read -r answer

  if [[ "$answer" =~ ^[Yy]$ ]]; then
    echo "Enter the remote repository URL:"
    read -r remote_url
    git remote add origin "$remote_url"
  fi
fi


echo "Enter a branch name:"
read -r branch_name

git commit -m "$commit_message"
git branch -M master $branch_name 

  git push -u origin $branch_name  
fi

echo "Finished!"

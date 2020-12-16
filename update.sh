#! /bin/bash

echo "Create local branch..."
git checkout -b newBranch

echo "Commit branch changes..."
git add .
git commit -m "add newBranch support..."

echo "Switch to master branch..."
git checkout master

echo "Merge changes from the new branch to the master branch..."
git merge newBranch

echo "Delete the new branch..."
git branch -D newBranch


echo "Specify remote source..."
git remote add upstream https://github.com/EnableSecurity/wafw00f.git

echo "Get updates from remote sources..."
git fetch upstream

echo "Merged into the local library..."
git merge upstream/master

echo "Submit to the local repository..."
git commit -a -m "merged upstream."

echo "Push and submit to my own github repository."
git push

echo "end..."
#!/bin/bash

commit_msg=${1}

#git init
#git remote add origin https://github.com/Visvasrk-221E/render.git


echo "[Adding current files]..."
git add .
echo "[SUCCESS] : Added all files..."
echo "[Running Command : git commit -m ${commit_msg}]"
git commit -m "${commit_msg}"
echo "[SUCCESS] : Commited added files..."
git push
echo "[SUCCESS] : Push Successfull..."

sleep 3
echo "[Create a new render deploy]..."
echo "[Fetching the latest commit ID]..."
commit_id=$(git rev-parse HEAD)
sleep 1
echo "[Fetched the latest commit ID]"
echo "[Commid ID] : ${commit_id}"
echo "[DEPLOYING]..."
sleep 2
render deploys create srv-d307mabe5dus73dfct1g --commit ${commit_id}

echo "[SUCCESS]..."

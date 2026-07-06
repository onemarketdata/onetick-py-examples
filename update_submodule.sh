#!/bin/bash


PARENT_REPO=$1
PROJECT=$2
SUBMODULE=$3
SUBMODULE_PATH=$4

echo "Updating submodule in $PARENT_REPO at $SUBMODULE_PATH"

git clone https://${GITLAB_CI_USER}:${API_TOKEN}@gitlab.sol.onetick.com/solutions/$PROJECT/$PARENT_REPO.git

if [[ -z "$SUBMODULE_PATH" ]]; then
  cd "$PARENT_REPO"
else
  cd "$PARENT_REPO/$SUBMODULE_PATH"
fi

git config --global url."https://${GITLAB_CI_USER}:${API_TOKEN}@gitlab.sol.onetick.com/".insteadOf "https://gitlab.sol.onetick.com/"
git submodule update --init $SUBMODULE

cd "$SUBMODULE"
git checkout master
git pull
cd ..
git add "$SUBMODULE"

if [ -n "$(git status --porcelain)" ]; then
  echo "Committing and pushing changes to master..."
  git commit -m "Updated $SUBMODULE submodule in $PARENT_REPO to the latest commit"
  git push -u origin master
else 
  echo "No changes to commit"
fi

if [[ -z "$SUBMODULE_PATH" ]]; then
  cd ..
else
  cd ../..
fi

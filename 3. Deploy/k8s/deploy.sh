## Pull repo
git clone https://github.com/rubialex17/birthday.git

## Get commit id
commit=$(git log -n 1 --pretty=format:"%H")
## Install requirements
pip install to-requirements.txt

## Run unit tests
python3 -m unittest tests.tests_app

export IMAGE=\"repository/birthday-app:$commit\"

## Build docker image
docker build . -t "repository/birthday-app:$commit"

# Push dockeri mage
docker push "repository/birthday-app:$commit"

# Add new image to deployment.yaml
envsubst < "deployment.yaml" > "temp.yaml"

## Apply deployment
kubectl apply -f temp.yaml

## Remove temp file
rm temp.yaml


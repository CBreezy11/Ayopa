# Ayopa local dev setup



#### The goals for the environment were:
* Use localstack to test on AWS services locally. [localstack github](https://github.com/localstack/localstack)
* Specifically the s3 and dynamodb services
* Use in docker for consistency
* Create an entire custom developing os container that can be changed as necessary as needs grow
to allow a consistent develop / deploy environment
* Ubuntu 18.04 with git and nano and curl
* Python3.6--check requirements.txt for dependencies installed
* GOlang 1.9.1--must set path to work `export PATH=$PATH:/usr/local/go/bin` then `mkdir $HOME/go` and good to go


## Setup steps
* Have [docker installed](https://www.docker.com/)
* Pull the cbreezy/stack:aws image from the dockerhub
* clone this repo
* build an image from the Dockerfile
* run the stack image detached with a desired name and the host network
* run the ayopa image with a name with desired name, host network, launched in bash, mount your code directory into the container

### The previous steps would look like this
`docker pull cbreezy/stack:aws

`git clone https://github.com/CBreezy11/Ayopa.git`

`docker build -t ayopa-local-dev ./<directory the dockerfile is in>`

`docker run -d --name stack --network host cbreezy/stack:aws`

`docker run -it --name os --network host --mount type=bind,source="$(pwd)",target=/code ayopa-local-dev`

### Test with s3
`$ awslocal s3 mb s3://test1`

`make_bucket: test1`

`$ awslocal s3 ls`

`<date> test1`

Head over to localhost:8080 to see a webui of your deployed resources!

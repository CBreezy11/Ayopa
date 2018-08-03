FROM cbreezy/ayopa:0.5

WORKDIR /

ADD requirements.txt /requirements.txt


RUN apt-get update
RUN apt-get install -y python3.6
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
RUN apt install -y curl
RUN apt-get install nano
RUN curl -O https://storage.googleapis.com/golang/go1.9.1.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.9.1.linux-amd64.tar.gz















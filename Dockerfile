FROM ubuntu:latest
LABEL node="zip-job-docker"
RUN apt-get update && apt-get install -y \
    python3 \
    zip \
    unzip \
    vim \
    python3-pip \
    curl
RUN pip3 install Path
COPY get_info.sh /tmp
RUN chmod 777 /tmp/get_info.sh
RUN mkdir /zip
COPY zip_job.py /tmp
ENV VERSION="1.2.0"
CMD ["/tmp/get_info.sh"]

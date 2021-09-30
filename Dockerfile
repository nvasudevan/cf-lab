FROM python:3.9-alpine

ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000
ARG JENKINS_AGENT_HOME=/home/${user}

RUN adduser -u ${uid} -g ${gid} -h ${JENKINS_AGENT_HOME} -D ${user}

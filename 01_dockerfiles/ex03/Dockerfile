FROM debian:latest

# Update the debian version
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y \
        curl \
        openssh-server \
        ca-certificates \
        postfix \
        tzdata

# Install Gitlab
RUN curl "https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh" | bash

RUN apt-get install -y \
		gitlab-ce

ENV PATH /opt/gitlab/embedded/bin:/opt/gitlab/bin:/assets:$PATH

COPY entrypoint.sh /entrypoint.sh
COPY gitlab.rb /gitlab.rb

RUN chmod +x /entrypoint.sh

EXPOSE 443 80 22

ENTRYPOINT ["sh", "-c", "/entrypoint.sh"]

# Build it
# docker build -t gitlab_img .
#
# Run it
# docker run -it -p 80:80 -p 443:443 -p 8022:22 --priviledged --name gitlab gitlab_img

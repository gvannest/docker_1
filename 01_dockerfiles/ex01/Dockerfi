FROM debian:latest

ENV TSV=3.9.1
ENV TS3SERVER_URL_ALIAS="teamspeak3-server.tar.bz2"
ENV TS3SERVER_USR="teamspeak_usr"
ENV TS3SERVER_GRP="teamspeak_grp"
ENV TS3SERVER_ROUTE="/home/teamspeak"
ENV TS3SERVER_LICENSE="accept"

ENV PATH="${PATH}:${TS3SERVER_ROUTE}"

#  9987 default voice
# 10011 server query
# 30033 file transport
EXPOSE 9987/udp 10011 30033

# Update the debian version
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
        wget \
        tar \
        bzip2

# Install teamspeak

RUN groupadd $TS3SERVER_GRP \
        && useradd -G $TS3SERVER_GRP $TS3SERVER_USR \
        && mkdir -p $TS3SERVER_ROUTE \
        && chown -R $TS3SERVER_USR:$TS3SERVER_GRP $TS3SERVER_ROUTE

RUN wget "https://files.teamspeak-services.com/releases/server/${TSV}/teamspeak3-server_linux_amd64-${TSV}.tar.bz2" -O $TS3SERVER_URL_ALIAS \
        && tar -xvf $TS3SERVER_URL_ALIAS -C $TS3SERVER_ROUTE \
        && chown -R :$TS3SERVER_GRP $TS3SERVER_ROUTE

COPY --chown=$TS3SERVER_USR:$TS3SERVER_GRP /entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# How to build it?
# docker build -t ex01 .

# How to run it?
# docker run --rm -p 9987:9987/udp -p 10011:10011 -p 30033:30033 ex01

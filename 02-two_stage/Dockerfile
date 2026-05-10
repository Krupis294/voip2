# ================================
# BUILD PHASE
# ================================
FROM debian:12-slim AS builder
LABEL maintainer="Jan Rozhon <jan@rozhon.eu>"

RUN apt update -qq && \
    DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends \
        autoconf \
        build-essential \
        binutils-dev \
        ca-certificates \
        curl \
        file \
        less \
        libcurl4-openssl-dev \
        libedit-dev \
        libgsm1-dev \
        libogg-dev \
        libopus-dev \
        libjansson-dev \
        libpopt-dev \
        libresample1-dev \
        libspandsp-dev \
        libspeex-dev \
        libspeexdsp-dev \
        libsqlite3-dev \
        libssl-dev \
        libvorbis-dev \
        libxml2-dev \
        libxslt-dev \
        libsrtp2-dev \
        libncurses5-dev \
        libtinfo-dev \
        ncurses-bin \
        ncurses-term \
        libunwind-dev \
        portaudio19-dev \
        procps \
        python3-pip \
        tcpdump \
        unixodbc-dev \
        uuid-runtime \
        vim-tiny \
        xmlstarlet \
        cmake \
        pkg-config && \
    rm -rf /var/lib/apt/lists/*

RUN useradd --system --home /home/asterisk asterisk

ENV ASTERISK_VERSION=20.6.0
WORKDIR /usr/src/asterisk

ADD http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-${ASTERISK_VERSION}.tar.gz asterisk.tar.gz
RUN tar --strip-components=1 -xzf asterisk.tar.gz

RUN ./configure --with-resample --with-jansson-bundled
RUN make menuselect/menuselect menuselect.makeopts
# menuselect-tree vynecháno

RUN menuselect/menuselect --disable BUILD_NATIVE menuselect.makeopts && \
    menuselect/menuselect --enable BETTER_BACKTRACES menuselect.makeopts && \
    menuselect/menuselect --enable codec_opus menuselect.makeopts

RUN make all
RUN make install && \
    make basic-pbx && \
    make progdocs

RUN mkdir -p /etc/asterisk
COPY asterisk/ /etc/asterisk/

RUN chown -R asterisk:asterisk /etc/asterisk
RUN sed -i -E 's/^;(run)(user|group)/\1\2/' /etc/asterisk/asterisk.conf

# ================================
# FINAL CONTAINER
# ================================
FROM debian:12-slim AS final

RUN apt update -qq && \
    DEBIAN_FRONTEND=noninteractive apt install -y --no-install-recommends \
        file \
        binutils-dev \
        libedit-dev \
        ca-certificates \
        libsqlite3-dev \
        libsrtp2-dev \
        curl \
        less \
        libgsm1 \
        libresample1 \
        libxml2 \
        procps \
        python3-pip \
        tcpdump \
        unixodbc \
        postgresql-client \
        odbc-postgresql \
        uuid-runtime \
        vim-tiny \
        xmlstarlet \
        iproute2 \
        sqlite3 && \
    rm -rf /var/lib/apt/lists/*

RUN useradd --system --home /home/asterisk asterisk

COPY --from=builder --chown=asterisk:asterisk /usr/lib/libasterisk* /usr/lib/
COPY --from=builder --chown=asterisk:asterisk /usr/lib/asterisk/ /usr/lib/asterisk/
COPY --from=builder --chown=asterisk:asterisk /usr/sbin/asterisk /usr/sbin/asterisk
COPY --from=builder --chown=asterisk:asterisk /var/spool/asterisk/ /var/spool/asterisk/
COPY --from=builder --chown=asterisk:asterisk /var/lib/asterisk/ /var/lib/asterisk/
COPY --from=builder --chown=asterisk:asterisk /var/run/asterisk/ /var/run/asterisk/
COPY --from=builder --chown=asterisk:asterisk /var/log/asterisk/ /var/log/asterisk/
COPY --from=builder --chown=asterisk:asterisk /etc/asterisk/ /etc/asterisk/

RUN chown -R asterisk:asterisk \
    /var/lib/asterisk \
    /var/log/asterisk \
    /var/run/asterisk \
    /etc/asterisk

WORKDIR /home/asterisk
USER asterisk

CMD ["asterisk", "-f"]

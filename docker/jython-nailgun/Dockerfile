FROM harisekhon/jython
USER root

# This adds custom stuff to the ClassPath Nailgun uses
ENV NAILGUN_CP ""

ADD ng-server ng-jython /usr/bin/

ARG vNailgun=1.0.0
RUN apk update \
    && apk add --virtual build-dependencies gcc musl-dev \
    && mkdir -p /opt/nailgun \
    && wget https://github.com/facebook/nailgun/releases/download/nailgun-all-v${vNailgun}/nailgun-server-1.0.0-SNAPSHOT-uber.jar -O "/opt/nailgun/nailgun-server.jar" \
    && wget https://github.com/facebook/nailgun/releases/download/nailgun-all-v${vNailgun}/ng.c && gcc ng.c -o /usr/bin/ng \
    && wget https://github.com/facebook/nailgun/releases/download/nailgun-all-v${vNailgun}/ng.py -O /usr/bin/ng.py \
    && chmod +x /usr/bin/ng.py /usr/bin/ng-jython /usr/bin/ng-server \
    && apk del build-dependencies \
    && rm /var/cache/apk/*

ENV NAILGUN_HOME "/opt/nailgun/"

CMD [ "/usr/bin/ng-server" ]

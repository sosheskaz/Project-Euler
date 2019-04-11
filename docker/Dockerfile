FROM alpine:3.9

# Easy stuff and pre-reqs
RUN apk -U add --no-cache git make musl-dev go nodejs npm python3 bash wget curl \
    vim build-base readline-dev openssl-dev zlib-dev linux-headers imagemagick-dev \
    libffi-dev hwinfo
ENV GOROOT /usr/lib/go
ENV GOPATH /go
ENV PATH /go/bin:$PATH

# Ruby
ARG vRuby=2.6.0
ENV PATH $HOME/.rbenv/bin:$HOME/.rbenv/plugins/ruby-build/bin:$PATH
RUN git clone git://github.com/sstephenson/rbenv.git .rbenv \
    && git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build \
    && eval "$(rbenv init -)" && echo 'eval "$(rbenv init -)"' >> $HOME/.bashrc \
    && bash -c 'rbenv install ${vRuby}'

# Groovy
ARG vGroovy=2.5.6
ARG vGroovyServ=1.2.0
RUN apk add --no-cache openjdk8 maven \
    && wget https://bintray.com/artifact/download/groovy/maven/apache-groovy-binary-${vGroovy}.zip \
    && mkdir -p /opt/nailgun \
    && unzip apache-groovy-binary-${vGroovy}.zip \
    && mv groovy-${vGroovy} /opt/groovy \
    && rm apache-groovy-binary-${vGroovy}.zip \
    && wget https://github.com/facebook/nailgun/releases/download/nailgun-all-v1.0.0/nailgun-server-1.0.0-SNAPSHOT.jar -O "/opt/nailgun/nailgun-server.jar" \
    && wget https://github.com/facebook/nailgun/releases/download/nailgun-all-v1.0.0/ng.c && gcc ng.c -o /usr/bin/ng
ENV JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
ENV GROOVY_HOME /opt/groovy
ENV PATH /opt/groovy/bin:$PATH

ADD ng-server /usr/bin/ng-server
ADD ng-groovy /usr/bin/ng-groovy

# Packages
RUN python3 -m pip install tqdm joblib sympy pyyaml

ENTRYPOINT [ "bash" ]

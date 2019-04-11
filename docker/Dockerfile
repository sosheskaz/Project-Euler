FROM alpine:3.9

ENV GOROOT /usr/lib/go
ENV GOPATH /go
ENV PATH /usr/local/groovyserv/bin:/usr/local/groovy/bin:$HOME/.rbenv/bin:$HOME/.rbenv/plugins/ruby-build/bin:/go/bin:$PATH

# Easy stuff and pre-reqs
RUN apk -U add --no-cache git make musl-dev go nodejs npm python3 bash wget curl \
    vim build-base readline-dev openssl-dev zlib-dev linux-headers imagemagick-dev \
    libffi-dev hwinfo

# Ruby
ARG vRuby=2.6.0
RUN git clone git://github.com/sstephenson/rbenv.git .rbenv \
    && git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build \
    && eval "$(rbenv init -)" && echo 'eval "$(rbenv init -)"' >> $HOME/.bashrc \
    && bash -c 'rbenv install ${vRuby}'

# Groovy
ARG vGroovy=2.5.6
ARG vGroovyServ=1.2.0
ENV JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
ENV GROOVY_HOME /usr/local/groovy
RUN apk add --no-cache openjdk8 \
    && wget https://bintray.com/artifact/download/groovy/maven/apache-groovy-binary-${vGroovy}.zip \
    && mkdir -p /usr/local \
    && unzip apache-groovy-binary-${vGroovy}.zip \
    && mv groovy-${vGroovy} /usr/local/groovy \
    && rm apache-groovy-binary-${vGroovy}.zip \
    && wget https://bitbucket.org/kobo/groovyserv-mirror/downloads/groovyserv-${vGroovyServ}-bin.zip \
    && unzip groovyserv-${vGroovyServ}-bin.zip \
    && mv groovyserv-${vGroovyServ}-bin /usr/local/groovyserv

# Packages
RUN python3 -m pip install tqdm joblib sympy pyyaml

ENTRYPOINT [ "bash" ]

FROM python:3.7

ENV TZ=Asia/Shanghai
ENV ENV=dev

RUN sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list \
    && apt-get -y update \
    && apt-get -y install vim locales \
    && sed -i 's/^# *\(zh_CN.UTF-8\)/\1/' /etc/locale.gen \
    && locale-gen \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo '$TZ' > /etc/timezone \
    && useradd --create-home --shell /bin/bash works \
    && mkdir -p /home/works/program/

ENV LANG=zh_CN.UTF-8
ENV LANGUAGE=zh_CN:zh:en_US:en
ENV LC_ALL=zh_CN.UTF-8

WORKDIR /home/works/program/

COPY ./ /home/works/program/
RUN chown -R works.works /home/works/program/

CMD ["/bin/bash"]

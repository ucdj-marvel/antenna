FROM mysql:8.0.28

RUN apt-get update
RUN apt-get -y install locales-all

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

# タイムゾーンに日本を設定する
RUN ln -sf /usr/share/zoneinfo/Japan /etc/localtime
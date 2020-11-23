# 利用するUbuntuのイメージ
FROM ubuntu:20.04

##############################################
# システム関係
#
# wgetをインストール
RUN apt-get update && apt-get install -y wget
#
RUN apt install -y curl

##############################################
# python 関係
#
# pythonをインストール
RUN apt-get install -y python3 python3-pip
#
# venvをインストール
RUN apt-get install python3-venv -y
#
# numpy, matplotlibをインストール
RUN pip3 install numpy matplotlib
#
# auto-sklearnのインストール
RUN curl https://raw.githubusercontent.com/automl/auto-sklearn/master/requirements.txt | xargs -n 1 -L 1 pip3 install
#
RUN pip3 install auto-sklearn

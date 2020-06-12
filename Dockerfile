FROM centos:8

MAINTAINER "aditi" <amalhotra1104@gmail.com>

RUN yum install python36 -y && pip3 install --upgrade pip && pip3 install tensorflow && pip3 install keras && pip3 install numpy && pip3 install pandas && pip3 install pillow && pip3 install scikit-learn && pip3 install opencv-python && pip3 install matplotlib

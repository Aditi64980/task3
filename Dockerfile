FROM centos
RUN yum install python36 -y
RUN pip3 install --upgrade pip
RUN pip3 install keras
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install pillow
RUN pip3 install scikit-learn
RUN pip3 install opencv-python
RUN pip3 install matplotlib
RUN pip3 install tensorflow

CMD ["python3", "./program1.py"]

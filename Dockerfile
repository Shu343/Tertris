FROM python:latest


RUN git clone https://github.com/Shu343/Tertris /Tertris
WORKDIR /Tertris
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r /Tertris/requirements.txt
CMD python3 __main__.py


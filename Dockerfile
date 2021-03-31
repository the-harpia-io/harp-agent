FROM python:3.9.1-alpine

WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers libressl-dev libffi-dev

# Copy Lib
COPY .circleci/grpcio.tar.gz grpcio.tar.gz
RUN tar -xzf grpcio.tar.gz -C /usr/local/lib/python3.9

# Copy requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN python setup.py install
CMD ["harp-agent"]
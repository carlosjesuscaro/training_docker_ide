FROM ubuntu
WORKDIR /app
COPY . .
RUN apt update && apt upgrade -y
RUN apt install python3 vim curl -y
#ENTRYPOINT ['bash']


EXample
FROM ubuntu
WORKDIR /app
COPY . .
RUN apt update && apt upgrade -y
RUN apt install python3 -y
#ENTRYPOINT ['bash']
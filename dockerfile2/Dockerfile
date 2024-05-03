# syntax=docker/dockerfile:1

FROM ubuntu:latest

ENV TZ=US DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get install -y --no-install-recommends \
	r-base python3.10 python3-pip

WORKDIR /dockerfile2

COPY . .

RUN pip3 install -r requirements.txt

RUN Rscript requirements.R



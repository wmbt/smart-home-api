#!/usr/bin/env bash

cp -f ./gunicorn.service /etc/systemd/system/gunicorn.service
cp -f ./gunicorn.socket /etc/systemd/system/gunicorn.socket
cp -f ./gunicorn.conf /etc/tmpfiles.d/gunicorn.conf
systemctl daemon-reload

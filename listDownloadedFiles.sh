#!/bin/sh
#
# https://github.com/SeleniumHQ/docker-selenium/issues/1813
#
sessionId="81539e3f1260a4f4a795a65df0a561f4"

curl http://localhost:4444/session/${sessionId}/de/files

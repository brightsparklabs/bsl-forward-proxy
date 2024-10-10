##
 # The image used to host the Team BSL CLI.
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

FROM brightsparklabs/appcli:3.0.0

ENTRYPOINT ["./bsl-forward-proxy.py"]
WORKDIR /app

COPY requirements.txt .
RUN pip install --requirement requirements.txt
COPY src .

# TODO: uncomment if using a local appcli during dev
#COPY appcli appcli
#COPY requirements-dev.txt .
#RUN pip install --requirement requirements-dev.txt

ARG APP_VERSION=latest
ARG BUILD_DATE
ARG VCS_REF
LABEL maintainer="enquire@brightsparklabs.com" \
      org.label-schema.name="team-bsl" \
      org.label-schema.description="Image used to run the BSL Forward Proxy CLI" \
      org.label-schema.vendor="brightSPARK Labs" \
      org.label-schema.schema-version="1.0.0-rc1" \
      org.label-schema.vcs-url="https://github.com/brightsparklabs/bsl-forward-proxy" \
      org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.version=${APP_VERSION}
ENV META_BUILD_DATE=${BUILD_DATE} \
    META_VCS_REF=${VCS_REF} \
    APP_VERSION=${APP_VERSION}
RUN echo ${APP_VERSION} > VERSION

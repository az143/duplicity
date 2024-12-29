# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4; encoding:utf-8 -*-
#
# Copyright 2019 Nils Tekampe <nils@tekampe.org>,
# Kenneth Loafman <kenneth@loafman.com>,
# Aaron Whitehouse <code@whitehouse.kiwi.nz>
#
# This file is part of duplicity.
#
# Duplicity is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# Duplicity is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with duplicity; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

FROM ubuntu:20.04

# Set locale to prevent UTF-8 errors
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYENV_ROOT="/root/.pyenv"
ENV PATH="$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH"

# Set to non-interactive so no tzdata prompt
ARG DEBIAN_FRONTEND=noninteractive

# Installing some pre-requisites and some
# packages needed for testing duplicity
RUN apt-get update \
    && apt-get install -y \
        2to3 \
        build-essential \
        git \
        intltool \
        lftp \
        librsync-dev \
        libffi-dev \
        libssl-dev \
        openssl \
        par2 \
        python3-pip \
        python3 \
        rclone \
        rdiff \
        tzdata \
# The following packages are for building python via pyenv
    && apt-get install -y \
        curl \
        libbz2-dev \
        libffi-dev \
        liblzma-dev \
        libncursesw5-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        libxml2-dev \
        libxmlsec1-dev \
        llvm \
        make \
        tk-dev \
        wget \
        xz-utils \
        zlib1g-dev \
# The following packages are not necessary for testing but make life easier or support debugging
    && apt-get install -y \
        ftp \
        iputils-ping \
        mc \
        nano \
        net-tools \
        rsync \
    && rm -rf /var/lib/apt/lists/*

# Install pyenv
RUN git clone -b "v2.4.12" --single-branch https://github.com/pyenv/pyenv.git /root/.pyenv \
    && eval "$(pyenv init --path)" \
    && eval "$(pyenv init -)"
# Install all the Pythons we test
RUN pyenv install 3.8.19
RUN pyenv install 3.9.19
RUN pyenv install 3.10.14
RUN pyenv install 3.11.10
RUN pyenv install 3.12.6
RUN pyenv install 3.13.0

COPY requirements.* /tmp
RUN echo Installing /tmp/requirements for 3.8 \
    && pyenv global 3.8.19 \
    && pip install --upgrade pip setuptools \
    && pip install -r /tmp/requirements.dev \
    && pip install -r /tmp/requirements.txt
RUN echo Installing /tmp/requirements for 3.9 \
    && pyenv global 3.9.19 \
    && pip install --upgrade pip setuptools \
    && pip install -r /tmp/requirements.dev \
    && pip install -r /tmp/requirements.txt
RUN echo Installing /tmp/requirements for 3.10 \
    && pyenv global 3.10.14 \
    && pip install --upgrade pip setuptools \
    && pip install -r /tmp/requirements.dev \
    && pip install -r /tmp/requirements.txt
RUN echo Installing /tmp/requirements for 3.11 \
    && pyenv global 3.11.10 \
    && pip install --upgrade pip setuptools \
    && pip install -r /tmp/requirements.dev \
    && pip install -r /tmp/requirements.txt
RUN echo Installing /tmp/requirements for 3.12 \
    && pyenv global 3.12.6 \
    && pip install --upgrade pip setuptools \
    && pip install -r /tmp/requirements.dev \
    && pip install -r /tmp/requirements.txt
RUN echo Installing /tmp/requirements for 3.13.0 \
    && pyenv global 3.13.0 \
    && pip install --upgrade pip setuptools \
    && pip install -r /tmp/requirements.dev \
    && pip install -r /tmp/requirements.txt

# cleanup the noise left over
RUN rm -rf /root/.cache/pip \
    rm -rf /root/requirements.* \
    rm -rf /root/*

# Set workdir to duplicity
WORKDIR /root/duplicity

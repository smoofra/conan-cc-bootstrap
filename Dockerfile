FROM python:3.12
RUN pip install conan==2.5.0
COPY . /src
RUN conan --version
RUN cp /src/settings.yml ~/.conan2/settings.yml
RUN conan create /src/cc -pr:b /src/Linux-bootstrap -pr:h /src/Linux-x86_64
RUN conan create /src/foo -pr:h /src/Linux-x86_64 -pr:b /src/Linux-x86_64

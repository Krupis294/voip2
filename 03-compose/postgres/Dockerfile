FROM postgres:15
LABEL maintainer='Jan Rozhon <jan@rozhon.eu>'
COPY init/*.sql /docker-entrypoint-initdb.d/
COPY init/*.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/*.sh

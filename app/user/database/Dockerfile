FROM postgres:12
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=usermanagement
COPY create_tables.sql /docker-entrypoint-initdb.d/create_tables.sql
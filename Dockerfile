FROM python:3.12-slim
ARG APP_VERSION=dev
ARG REVISION=desconocida
LABEL org.opencontainers.image.title="reservas-canchas" \
      org.opencontainers.image.version="${APP_VERSION}" \
      org.opencontainers.image.revision="${REVISION}"
ENV APP_VERSION=${APP_VERSION} PORT=8000 DB_PATH=/data/reservas.db PYTHONUNBUFFERED=1
# Usuario sin privilegios; /data es el único lugar donde se escribe (volumen).
RUN useradd --system --uid 10001 app && mkdir /data && chown app /data
WORKDIR /srv
COPY app ./app
USER app
VOLUME /data
EXPOSE 8000
# Tiene que ser comprobable por quien orquesta el contenedor (Compose, Docker, un despliegue).
HEALTHCHECK --interval=5s --timeout=3s --start-period=3s --retries=5 \
  CMD python -c "import os,urllib.request as u; u.urlopen('http://localhost:%s/salud' % os.environ['PORT'], timeout=2)"
CMD ["python", "-m", "app.main"]

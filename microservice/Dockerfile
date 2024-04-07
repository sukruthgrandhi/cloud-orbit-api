FROM python:3.9-bullseye
ARG CLOUD_ORBIT_API
RUN pip install ${CLOUD_ORBIT_API}
# Command to run the FastAPI application
WORKDIR /usr/local/lib/python3.9/site-packages/cloud_orbit_api
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

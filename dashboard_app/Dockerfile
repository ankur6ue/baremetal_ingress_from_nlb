FROM python:3.8
# Install pip
RUN python -m pip install --upgrade pip
RUN pip install flask
RUN mkdir -p /app
WORKDIR /app
COPY server.py /app/
COPY templates/ /app/templates/
CMD ["python", "server.py"]
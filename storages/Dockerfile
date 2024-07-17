FROM python:3.12.4

RUN mkdir app
WORKDIR /app

# ENV PATH="${PATH}:/root/.local/bin"
# ENV PYTHONPATH=.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

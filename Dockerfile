FROM python:3.6.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /vmscope
COPY requirements.txt /vmscope
WORKDIR /vmscope
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]

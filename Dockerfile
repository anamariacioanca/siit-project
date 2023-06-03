FROM python:3.11
RUN pip install Django==4.2.1
COPY sampleproject .
EXPOSE 8000
ENTRYPOINT [ "python", "manage.py", "runserver", "0:8000" ]


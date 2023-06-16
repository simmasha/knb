FROM python:3.10-bookworm
COPY . /python_app
WORKDIR /python_app
RUN pip install --upgrade pip &&  pip install -r requirements.txt && pip install pyinstaller
CMD python main.py

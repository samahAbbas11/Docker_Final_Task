FROM python:3.10.0-alpine3.13

# copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

# install the requiered packages
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8888

CMD [ "python", "./bitcoinApp.py" ]


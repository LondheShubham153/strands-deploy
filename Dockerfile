FROM python:3.13 

WORKDIR /app 

COPY . .

RUN pip install -r requirements.txt

ENV AWS_DEFAULT_REGION="us-west-2"

CMD ["python", "agent.py"]

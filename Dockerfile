# Start from a base image
FROM python:2.7-alpine

# Install empirical library
RUN apk add --update build-base 
# TODO: These should be replaced by pip install empirical
RUN pip install zerorpc 
RUN pip install requests

# Add Evaluator
COPY . /evaluator
WORKDIR /evaluator
ENTRYPOINT ["python", "evaluator.py"]

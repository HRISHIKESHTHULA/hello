ARG python_image_tag=3.9

FROM python:${python_image_tag}

RUN mkdir -p /opt/hello_world
COPY hello_world /opt/hello_world

WORKDIR /opt/hello_world
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
ENTRYPOINT ["python", "./hello_world.py"]

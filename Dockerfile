FROM python:3.11-slim

WORKDIR /app
COPY . /app

# Install pipenv
RUN pip install pipenv

# Install dependencies from Pipfile.lock
RUN pipenv install --deploy --ignore-pipfile

# Run Streamlit app or city_loop.py
CMD ["pipenv", "run", "streamlit", "run", "streamlit_app.py"]

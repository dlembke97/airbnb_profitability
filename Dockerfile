FROM python:3.11-slim
WORKDIR /app
ADD . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install streamlit
CMD ["python", "city_loop.py"]

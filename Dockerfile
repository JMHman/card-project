# 베이스 이미지
FROM python:3.12

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    cargo

# Poetry 설치
RUN pip install --no-cache poetry

# Poetry 설정: 가상환경을 사용하지 않도록 설정
RUN poetry config virtualenvs.create false

# 프로젝트 파일 복사
COPY . .

COPY ./.env app/.env

# poetry를 이용해 의존성 설치
RUN poetry install --no-root

# 환경 변수 설정
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE portfolio.settings

# Collect static files
RUN python manage.py collectstatic --noinput

# 엔트리포인트 설정
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "portfolio.asgi:application"]

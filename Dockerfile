FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

ENV VIRTUAL_ENV=/opt/venv \
    UV_LINK_MODE=copy \
    PATH="/opt/venv/bin:$PATH"


RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=dist,target=/dist \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    uv venv /opt/venv && \
    uv pip install /dist/union_runtime-0.1.0b1-py3-none-any.whl \
    -r requirements.txt

WORKDIR /app

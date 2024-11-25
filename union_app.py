from flytekit import Resources, ImageSpec
from union.app import App

image_spec = ImageSpec(
    name="us-migration",
    requirements="requirements.txt",
    registry="ghcr.io/thomasjpfan",
    copy=["dist/union_runtime-0.1.0b2-py3-none-any.whl"],
    commands=["uv pip install /root/dist/union_runtime-0.1.0b2-py3-none-any.whl"],
)

app = App(
    name="new-us-population-3",
    container_image=image_spec,
    limits=Resources(cpu="2", mem="2Gi"),
    command=[
        "streamlit",
        "run",
        "migration_app.py",
        "--server.port",
        "8080",
    ],
    port=8080,
    include=[
        "migration_app.py",
        "plot_migration.py",
        "data_munging.py",
        "data/*.csv",
    ],
    min_replicas=1,
    max_replicas=1,
)

PACKAGE_NAME=back_fast_api
HOST_PORT=8000
THIS_DIR=$(shell pwd)

clean-pyc:
	rm -Rf tests/__pycache__
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete

clean-build:
	rm -Rf build/
	rm -Rf dist/
	rm -Rf *.egg-info
	rm -Rf .cache/

clean: clean-pyc clean-build

build-dev: clean
	docker build -f Dockerfile.dev -t $(PACKAGE_NAME) .

build: clean
	docker build -t $(PACKAGE_NAME) .

shell: clean-pyc
	docker run -it --rm \
	           -v $(THIS_DIR):/app-run \
	           -w /app-run \
	           -p $(HOST_PORT):8000 \
	           --entrypoint=/bin/ash \
	           $(PACKAGE_NAME)

launch-uvicorn:
	uvicorn main:app --reload --port=8000 --host=0.0.0.0
install:
	python setup.py develop

test:
	python tests/test.py

clear:
	rm -rf build
	rm -rf dist
	find . -type d -name '*.egg-info' -exec rm -rf {} \;

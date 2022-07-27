CWD = $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
DIST = ${CWD}/dist

all: build

.PHONY: build
build:
	npm ci
	npm run build

.PHONY: test
test:
	npm run test

.PHONY: bench
bench:
	echo "STARTING python-lang benchmark suite"
	npx python-lang `pwd`/bench/all.py
	echo "FINISHED python-lang benchmark suite"

clean:
	rm -rf ${DIST} node_modules

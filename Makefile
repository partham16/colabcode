develop:
	pip install -q -U pip
	pip install -q -r requirements_dev.txt
	pre-commit install
	make precommit

install:
	pip install -q -r requirements.txt

full_install: develop install

precommit:
	git add .
	pre-commit run
	git add .

black:
	black colabcode tests

isort:
	isort colabcode tests

pylint:
	pylint colabcode tests --min-public-methods 0

mypy:
	mypy colabcode tests --ignore-missing-imports

flake:
	flake8 colabcode tests --ignore=E501

test:
	#pytest tests/*
	echo "No tests set yet"

check: black flake test precommit

fullcheck: mypy check pylint

make m_pull:
	git pull upstream master

make m_push:
	git push origin master

make m_pull_fup:
	git pull origin for_upstream

make fup_pull:
	git checkout for_upstream
	git pull upstream master

make fup_push:
	git checkout for_upstream
	git push origin for_upstream

make amend:
	git add .
	git commit --amend

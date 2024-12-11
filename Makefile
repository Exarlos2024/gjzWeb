.PHONY: backend frontend install-backend install-frontend

# Windows 环境下的命令
ifeq ($(OS),Windows_NT)
install-backend:
	cd backend && python -m venv .venv && .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt

install-frontend:
	cd frontend && npm install

backend:
	cd backend && powershell -Command ".\\.venv\\Scripts\\Activate.ps1; python manage.py runserver"

# Unix 环境下的命令
else
install-backend:
	cd backend && python -m venv .venv && . .venv/bin/activate; pip install -r requirements.txt

install-frontend:
	cd frontend && npm install

backend:
	cd backend && . .venv/bin/activate; python manage.py runserver
endif

# 通用命令
frontend:
	cd frontend && npm run dev

install: install-backend install-frontend

dev: backend frontend 
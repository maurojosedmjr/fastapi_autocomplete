# Nome do container e imagem
CONTAINER_NAME=autocomplete
IMAGE_NAME=autocomplete

# Definição dos comandos
.PHONY: help build run clean

help: ## Exibe todos os comandos disponíveis
	@echo "Comandos disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

build: ## Builda o container Docker
	@echo "Buildando o container Docker..."
	docker build . -t $(IMAGE_NAME) -f infra/Dockerfile

run: ## Roda o container Docker
	@echo "Rodando o container Docker..."
	docker run --name $(CONTAINER_NAME) -p 8000:8080 -d $(IMAGE_NAME)

clean: ## Remove o container Docker
	@echo "Removendo o container Docker..."
	docker rm -f $(CONTAINER_NAME)

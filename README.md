## 🔄 Fluxo de Trabalho e Comandos Úteis

Este guia resume os comandos essenciais de **Docker** e **Git** utilizados neste projeto para manter o ambiente de desenvolvimento e o versionamento do código.

### 📅 Rotina Diária (Workflow)

Siga este passo a passo para trabalhar no projeto:

1.  **Iniciar o dia (Atualizar e Subir):**
    * Baixe as atualizações do time: `git pull`
    * Suba o ambiente local: `docker compose up -d`
2.  **Desenvolver:**
    * Faça suas alterações no código.
    * Teste no navegador (o ambiente já estará rodando).
3.  **Salvar o progresso:**
    * Verifique o que mudou: `git status`
    * Adicione os arquivos: `git add .`
    * Salve a versão: `git commit -m "Sua mensagem aqui"`
    * Envie para o GitHub: `git push`
4.  **Finalizar o dia:**
    * Derrube o ambiente para limpar a memória: `docker compose down`

---

### 🐳 Resumo dos Comandos Docker
*Gerenciamento da infraestrutura (containers)*

| Comando | Função | Explicação |
| :--- | :--- | :--- |
| `docker compose up -d` | **Subir** | Cria e inicia os containers em segundo plano (libera o terminal). |
| `docker compose down` | **Derrubar** | Para e remove os containers e redes (limpa o ambiente). |
| `docker compose stop` | **Pausar** | Apenas para os containers, mantendo eles criados. |
| `docker compose build` | **Reconstruir** | Recria as imagens (use se instalou novas dependências no sistema). |
| `docker ps` | **Listar** | Mostra quais containers estão rodando no momento. |

### 🐙 Resumo dos Comandos Git
*Versionamento e Histórico*

| Comando | Função | Explicação |
| :--- | :--- | :--- |
| `git status` | **Status** | Mostra arquivos alterados e pendentes. |
| `git add .` | **Preparar** | Adiciona todas as mudanças para serem salvas. |
| `git commit -m "msg"` | **Salvar** | Cria um ponto na história com uma mensagem explicativa. |

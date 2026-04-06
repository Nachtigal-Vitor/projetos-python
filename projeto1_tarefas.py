"""
==============================================
PROJETO 1: Gerenciador de Tarefas (To-Do List)
==============================================
Conceitos Python usados:
  - Funções
  - Listas e dicionários
  - Leitura/escrita de arquivos (JSON)
  - Input do usuário
  - Loops e condicionais
"""

import json
import os

# Nome do arquivo onde as tarefas ficam salvas
ARQUIVO = "tarefas.json"


# --------------------------------------------------
# FUNÇÕES DE ARQUIVO
# --------------------------------------------------

def carregar_tarefas():
    """Lê as tarefas do arquivo JSON. Se não existir, retorna lista vazia."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_tarefas(tarefas):
    """Salva a lista de tarefas no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)


# --------------------------------------------------
# FUNÇÕES DE NEGÓCIO
# --------------------------------------------------

def adicionar_tarefa(tarefas, titulo):
    """Cria uma nova tarefa e adiciona na lista."""
    nova = {
        "id": len(tarefas) + 1,      # ID simples baseado no tamanho da lista
        "titulo": titulo,
        "concluida": False            # Toda tarefa começa como não concluída
    }
    tarefas.append(nova)
    salvar_tarefas(tarefas)
    print(f"✅ Tarefa '{titulo}' adicionada com sucesso!")


def listar_tarefas(tarefas):
    """Mostra todas as tarefas na tela."""
    if not tarefas:
        print("📭 Nenhuma tarefa cadastrada ainda.")
        return

    print("\n" + "=" * 40)
    print(f"{'ID':<5} {'STATUS':<12} {'TÍTULO'}")
    print("=" * 40)

    for t in tarefas:
        status = "✔ Feita" if t["concluida"] else "○ Pendente"
        print(f"{t['id']:<5} {status:<12} {t['titulo']}")

    print("=" * 40 + "\n")


def concluir_tarefa(tarefas, id_tarefa):
    """Marca uma tarefa como concluída pelo ID."""
    for t in tarefas:
        if t["id"] == id_tarefa:
            if t["concluida"]:
                print("⚠️  Essa tarefa já estava concluída.")
            else:
                t["concluida"] = True
                salvar_tarefas(tarefas)
                print(f"🎉 Tarefa '{t['titulo']}' marcada como concluída!")
            return
    print("❌ Tarefa não encontrada.")


def deletar_tarefa(tarefas, id_tarefa):
    """Remove uma tarefa pelo ID."""
    for i, t in enumerate(tarefas):
        if t["id"] == id_tarefa:
            removida = tarefas.pop(i)
            salvar_tarefas(tarefas)
            print(f"🗑️  Tarefa '{removida['titulo']}' removida.")
            return
    print("❌ Tarefa não encontrada.")


# --------------------------------------------------
# MENU PRINCIPAL
# --------------------------------------------------

def menu():
    """Exibe o menu e retorna a opção escolhida."""
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Deletar tarefa")
    print("0 - Sair")
    return input("Escolha uma opção: ").strip()


def main():
    """Função principal: carrega tarefas e roda o loop do menu."""
    tarefas = carregar_tarefas()

    while True:
        opcao = menu()

        if opcao == "1":
            titulo = input("Digite o título da tarefa: ").strip()
            if titulo:
                adicionar_tarefa(tarefas, titulo)
            else:
                print("⚠️  O título não pode ser vazio.")

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            listar_tarefas(tarefas)
            try:
                id_tarefa = int(input("ID da tarefa a concluir: "))
                concluir_tarefa(tarefas, id_tarefa)
            except ValueError:
                print("❌ Digite um número válido.")

        elif opcao == "4":
            listar_tarefas(tarefas)
            try:
                id_tarefa = int(input("ID da tarefa a deletar: "))
                deletar_tarefa(tarefas, id_tarefa)
            except ValueError:
                print("❌ Digite um número válido.")

        elif opcao == "0":
            print("👋 Até logo!")
            break

        else:
            print("⚠️  Opção inválida. Tente novamente.")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()

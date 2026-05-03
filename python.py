aluno = [
  {
    "nome": "márcio",
    "matricula": 230261,
    "curso": "Análise e Desenvolvimento de Sistemas",
    "idade": 21,
    "nota": 10
  },
  {
    "nome": "paulo",
    "matricula": 230262,
    "curso": "gastronomia",
    "idade": 28,
    "nota": 7.0
  },
  {
    "nome": "gabriela",
    "matricula": 230263,
    "curso": "direito",
    "idade": 24,
    "nota": 8.5
  }
]
while True:
  print("1 - Cadastrar aluno")
  print("2 - Listar alunos")
  print("0 - Sair")

  opcao = input("Escolha uma opcao: ")

  if opcao == "1":
    nome_novo_aluno = input("Digite o nome do novo aluno: ")
    matricula_novo_aluno = int(input("Digite a matricula do novo aluno: "))
    curso_novo_aluno = input("Digite o curso do novo aluno: ")
    idade_novo_aluno = int(input("Digite a idade do novo aluno: "))
    nota_novo_aluno = float(input("Digite a nota do novo aluno: "))

    novo_aluno = {
      "nome": nome_novo_aluno,
      "matricula": matricula_novo_aluno,
      "curso": curso_novo_aluno,
      "idade": idade_novo_aluno,
      "nota": nota_novo_aluno
    }

    aluno.append(novo_aluno)
    print("aluno cadastrado com sucesso!")
     elif opcao == "2":
    if not aluno:
      print("Nenhum aluno cadastrado.")
    else:
      print("\n Lista de Alunos")
      for aluno in aluno:
        print(f"Nome: {aluno['nome']}, Matricula: {aluno['matricula']}, Curso: {aluno['curso']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}")
      print()

  elif opcao == "0":
    print("Cadastro encerrado.")
    break

  else:
    print("Opção invalida. Tente novamente.")

print("Programa finalizado.")
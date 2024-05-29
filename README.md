# Sistema Bancário Simples em Python

Este projeto contém dois arquivos que implementam um sistema bancário simples em Python:

1. `sistema_bancario.py`: A versão básica do sistema bancário.
2. `sistema_bancario_otimizado.py`: A versão otimizada do sistema bancário, que inclui funções adicionais e melhorias.

## Funcionalidades

### Versão Básica (`sistema_bancario.py`)

- **Depósito**: Permite ao usuário fazer depósitos em sua conta bancária. O saldo máximo permitido é de R$500. O usuário pode fazer múltiplos depósitos até atingir esse limite.
- **Saque**: Permite ao usuário sacar dinheiro de sua conta bancária. O valor mínimo de saque é R$2 e deve ser um valor múltiplo de 2. O usuário tem um limite de 3 saques por dia.
- **Consultar Saldo**: Permite ao usuário verificar o saldo atual em sua conta bancária.
- **Extrato**: Permite ao usuário visualizar o histórico de transações, incluindo depósitos e saques, bem como o saldo atual.

### Versão Otimizada (`sistema_bancario_otimizado.py`)

Além das funcionalidades da versão básica, a versão otimizada inclui:

- **Cadastrar Cliente**: Permite ao usuário cadastrar novos clientes com informações como CPF, nome, data de nascimento e endereço.
- **Criar Conta**: Permite ao usuário criar novas contas bancárias associadas a clientes já cadastrados.
- **Listar Clientes**: Permite ao usuário visualizar a lista de clientes cadastrados.
- **Listar Contas**: Permite ao usuário visualizar a lista de contas bancárias criadas.

## Como Usar

### Executando a Versão Básica

1. Clone o repositório para sua máquina local:
   ```sh
   git clone https://github.com/ltsilva23/Sistema_bancario_simples.git
   ```

2. Navegue até o diretório do projeto:
   ```sh
   cd sistema-bancario
   ```

3. Execute o arquivo `sistema_bancario.py`:
   ```sh
   python sistema_bancario.py
   ```

4. Siga as instruções no terminal para selecionar as opções desejadas (depósito, saque, consultar saldo, extrato) e fornecer os valores necessários.

### Executando a Versão Otimizada

1. Clone o repositório para sua máquina local:
   ```sh
   git clone https://github.com/ltsilva23/Sistema_bancario_simples.git
   ```

2. Navegue até o diretório do projeto:
   ```sh
   cd sistema-bancario
   ```

3. Execute o arquivo `sistema_bancario_otimizado.py`:
   ```sh
   python sistema_bancario_otimizado.py
   ```

4. Siga as instruções no terminal para selecionar as opções desejadas (depósito, saque, consultar saldo, extrato, cadastrar cliente, criar conta, listar clientes, listar contas) e fornecer os valores necessários.

## Contribuindo

Sinta-se à vontade para contribuir com melhorias ou sugestões para o código! Você pode abrir uma issue para reportar problemas ou propor novas funcionalidades. Pull requests são bem-vindos.

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Comite suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Faça um push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

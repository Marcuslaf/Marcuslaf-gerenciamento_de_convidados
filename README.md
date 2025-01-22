# Sistema de Gerenciamento de Convidados de Casamento
# Wedding Guest Management System

[English version below](#wedding-guest-manager)

## Gerenciador de Convidados de Casamento

Um aplicativo Python para gerenciar listas de convidados de casamento, acompanhar convidados e seus dependentes, e controlar o acesso ao evento através de um sistema baseado em tokens.

### Funcionalidades

- Gerencia listas separadas de convidados para noiva e noivo
- Registra convidados principais com tokens únicos
- Adiciona até 3 dependentes por convidado principal
- Verifica entrada de convidados usando tokens
- Remove convidados ou dependentes da lista
- Lista todos os convidados registrados e seus dependentes

### Limitações do Sistema

- Máximo de 10 convidados principais para cada lado (noiva/noivo)
- Máximo de 3 dependentes por convidado principal
- Cada convidado principal deve ter um CPF único
- Tokens únicos de 6 caracteres gerados automaticamente para convidados principais
- Tokens de dependentes são derivados dos tokens do convidado principal (formato: PRINCIPAL-1, PRINCIPAL-2, etc.)

### Como Usar

#### Opções do Menu Principal

1. Cadastrar convidado principal
2. Cadastrar dependente
3. Listar convidados e dependentes
4. Verificar entrada
5. Remover convidado ou dependente
6. Sair

#### Cadastrando um Convidado Principal

```python
# Exemplo
Tipo (noivo/noiva): noiva
Nome do convidado principal: Maria Silva
CPF do convidado principal: 12345678900
```

#### Cadastrando um Dependente

```python
# Exemplo
Informe o token do convidado principal: ABC123
Nome do dependente: João Silva
```

#### Verificando Entrada

Basta inserir o token do convidado quando solicitado. O sistema verificará se é válido e exibirá as informações do convidado.

### Estrutura de Dados

O sistema utiliza um dicionário para armazenar informações dos convidados:

```python
convidados = {
    "noivo": [  # Convidados do noivo
        {
            "nome": "Nome do Convidado",
            "cpf": "12345678900",
            "token": "ABC123",
            "dependentes": [
                {"nome": "Nome do Dependente", "token": "ABC123-1"}
            ]
        }
    ],
    "noiva": []  # Convidados da noiva (mesma estrutura)
}
```

### Recursos de Segurança

- Tokens únicos para cada convidado principal
- Verificação de token sem distinção entre maiúsculas e minúsculas
- Verificação de CPF duplicado
- Prevenção de colisão de tokens
- Validação de entrada para tipo de convidado (noiva/noivo)

### Tratamento de Erros

O sistema inclui tratamento de erros para:
- Seleção inválida de tipo de convidado
- Tentativas de registro de CPF duplicado
- Limites de convidados excedidos
- Tokens inválidos
- Limite máximo de dependentes atingido

### Instalação

1. Certifique-se de ter Python 3.x instalado
2. Baixe o arquivo do script
3. Execute

Não são necessárias dependências adicionais, pois o script utiliza apenas a biblioteca padrão do Python (módulos random e string).

---

## Wedding Guest Manager

A Python application for managing wedding guest lists, tracking guests and their dependents, and controlling event access through a token-based system.

### Features

- Manage separate guest lists for bride and groom
- Register primary guests with unique tokens
- Add up to 3 dependents per primary guest
- Verify guest entry using tokens
- Remove guests or dependents from the list
- List all registered guests and their dependents

### System Limitations

- Maximum of 10 primary guests for each side (bride/groom)
- Maximum of 3 dependents per primary guest
- Each primary guest must have a unique CPF (Brazilian ID)
- Automatically generated unique 6-character tokens for primary guests
- Dependent tokens are derived from primary guest tokens (format: PRIMARY-1, PRIMARY-2, etc.)

### Usage

#### Main Menu Options

1. Register primary guest
2. Register dependent
3. List guests and dependents
4. Verify entry
5. Remove guest or dependent
6. Exit

#### Registering a Primary Guest

```python
# Example
Type (bride/groom): bride
Primary guest name: Maria Silva
Primary guest CPF: 12345678900
```

#### Registering a Dependent

```python
# Example
Enter primary guest token: ABC123
Dependent name: João Silva
```

#### Verifying Entry

Simply enter the guest's token when prompted. The system will verify if it's valid and display the guest's information.

### Data Structure

The system uses a dictionary to store guest information:

```python
convidados = {
    "noivo": [  # Groom's guests
        {
            "nome": "Guest Name",
            "cpf": "12345678900",
            "token": "ABC123",
            "dependentes": [
                {"nome": "Dependent Name", "token": "ABC123-1"}
            ]
        }
    ],
    "noiva": []  # Bride's guests (same structure)
}
```

### Security Features

- Unique tokens for each primary guest
- Case-insensitive token verification
- CPF duplication check
- Token collision prevention
- Input validation for guest type (bride/groom)

### Error Handling

The system includes error handling for:
- Invalid guest type selection
- Duplicate CPF registration attempts
- Exceeded guest limits
- Invalid tokens
- Maximum dependent limit reached

### Installation

1. Ensure you have Python 3.x installed
2. Download the script file
3. Run

No additional dependencies are required as the script only uses Python's standard library (random and string modules).

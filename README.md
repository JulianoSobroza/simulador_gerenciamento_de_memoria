# 🧠 Simulador de Gerenciamento de Memória com Paginação (FIFO)

## 📘 Descrição Geral

Este projeto implementa uma **simulação do gerenciamento de memória com paginação**, conforme o conteúdo da disciplina **Sistemas Operacionais**.

O simulador representa o funcionamento básico de um sistema operacional que utiliza **memória virtual** e **memória física**, gerenciadas por uma **tabela de páginas** e o algoritmo de substituição **FIFO (First In, First Out)**.

O objetivo é demonstrar como o sistema decide **quais páginas devem permanecer na memória física** e **quais devem ser removidas** quando ocorre uma **falha de página**.

---

## ⚙️ Estrutura do Projeto

```
src/
├── Main.java                   # Ponto de entrada da aplicação
├── modelo/
│   ├── MemoriaFisica.java      # Representa as molduras de memória (RAM)
│   ├── MemoriaVirtual.java     # Representa todas as páginas virtuais
│   ├── Pagina.java             # Estrutura de dados para uma página
│   ├── SimuladorFIFO.java      # Lógica principal da simulação (FIFO)
│   └── TabelaPaginas.java      # (opcional - pode ser expandida)
└── utils/
    └── LeitorArquivo.java      # Lê o arquivo de configuração config.txt
```

---

## 🧩 Arquivo de Configuração (`config.txt`)

O arquivo `config.txt` define os **parâmetros de simulação**.

### 📝 Exemplo:
```txt
# ==============================
# CONFIGURAÇÃO DO SIMULADOR DE MEMÓRIA
# ==============================

# Tamanho da memória física (em número de molduras)
3

# Tamanho da memória virtual (em número de páginas)
8

# Sequência de acessos a endereços virtuais (valores inteiros)
# Cada número representa o índice da página virtual acessada
0 2 1 3 0 4 2 1 5 0 2 3 6
```

### 🔍 Regras:
- Linhas iniciadas com `#` são **comentários** e são ignoradas.
- O arquivo deve conter exatamente **três valores válidos** (em ordem):
  1. **Tamanho da memória física** — número de molduras (ex: `3`).
  2. **Tamanho da memória virtual** — número total de páginas (ex: `8`).
  3. **Sequência de acessos** — lista de endereços virtuais simulados (ex: `0 2 1 3 0 4 2 1 5 0 2 3 6`).

---

## ▶️ Como Executar no IntelliJ IDEA

1. **Abra o projeto no IntelliJ.**
2. Certifique-se de que o arquivo `config.txt` está na **raiz do projeto** (mesmo nível de `Main.java`).
3. Clique com o botão direito em `Main.java` e selecione **Run 'Main.main()'**.
4. Observe no **terminal (CLI)** a simulação passo a passo.

---

## 🧮 Exemplo de Saída

```
=== SIMULADOR DE GERENCIAMENTO DE MEMÓRIA (FIFO) ===
Iniciando simulação FIFO...

Acessando página virtual: 0
⚠ Falha de página! Página 0 não está na memória.
Estado atual das molduras:
Moldura 0 -> Página 0
------------------------------

Acessando página virtual: 2
⚠ Falha de página! Página 2 não está na memória.
Estado atual das molduras:
Moldura 0 -> Página 0
Moldura 1 -> Página 2
------------------------------

Acessando página virtual: 1
⚠ Falha de página! Página 1 não está na memória.
Estado atual das molduras:
Moldura 0 -> Página 0
Moldura 1 -> Página 2
Moldura 2 -> Página 1
------------------------------

...
Total de falhas de página: 9
```

---

## 🔁 Como Testar com Diferentes Parâmetros

Você pode modificar o arquivo `config.txt` para observar comportamentos diferentes do algoritmo FIFO.

| Cenário | Memória Física | Memória Virtual | Acessos Virtuais | O que esperar |
|:--|:--:|:--:|:--|:--|
| **Pequena memória física** | 2 | 8 | `0 1 2 3 0 1 4 0 1 2 3 4` | Muitas falhas (poucas molduras disponíveis) |
| **Grande memória física** | 5 | 8 | `0 1 2 3 0 1 4 0 1 2 3 4` | Menos falhas (mais molduras disponíveis) |
| **Poucos acessos repetidos** | 3 | 6 | `0 1 2 3 4 5` | Alta taxa de falhas (cada acesso é novo) |
| **Acessos frequentes às mesmas páginas** | 3 | 6 | `0 1 2 0 1 2 0 1 2` | Menos falhas (páginas reutilizadas) |

Basta alterar os **números** no `config.txt` e **rodar novamente** o `Main.java`.

---

## 🧰 Requisitos Técnicos

- **Java 17+**
- Compatível com **IntelliJ IDEA** ou qualquer IDE Java
- Não requer interface gráfica (modo texto/CLI)
- Entrada: arquivo `config.txt`
- Saída: terminal padrão (System.out)

---

## 🧠 O que o Simulador Faz

Durante a execução, o sistema:

1. **Lê o arquivo de configuração** (`config.txt`);
2. **Cria as estruturas de memória virtual e física**;
3. **Percorre cada acesso virtual**, verificando se a página está na memória física;
4. Se **não estiver**, ocorre uma **falha de página**, e o sistema:
   - Carrega a página se houver espaço livre;
   - Caso contrário, **remove a página mais antiga (FIFO)**;
5. Exibe o **estado das molduras** a cada passo e, ao final, o **total de falhas de página**.

---

## 🧩 Estrutura Conceitual (Resumo)

| Conceito | Representado por | Explicação |
|:--|:--|:--|
| Página virtual | `Pagina.java` | Unidade lógica da memória virtual |
| Moldura de página | `MemoriaFisica.java` | Espaço físico na RAM |
| Bit de presença | `isPresente()` em `Pagina` | Indica se a página está carregada na RAM |
| Tabela de páginas | Conjunto das instâncias `Pagina` | Mapeia páginas virtuais → molduras físicas |
| Substituição de página | `SimuladorFIFO` | Implementa o algoritmo **First In, First Out** |

---



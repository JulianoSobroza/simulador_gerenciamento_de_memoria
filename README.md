# Simulador de Gerenciamento de Memória com Paginação

Trabalho Prático 2 - Sistemas Operacionais

## Descrição

Este projeto implementa um simulador de gerenciamento de memória com paginação para sistemas operacionais. O simulador demonstra o funcionamento de:

- **Memória Virtual**: Dividida em páginas de tamanho fixo
- **Memória Física**: Dividida em molduras de página (page frames) do mesmo tamanho das páginas
- **Tabela de Páginas**: Mapeia páginas da memória virtual para molduras da memória física
- **Algoritmos de Substituição de Páginas**: FIFO (First-In, First-Out) e LRU (Least Recently Used)

## Estrutura do Projeto

```
.
├── page.py              # Classes Page e PageFrame
├── page_table.py        # Classe PageTable para mapeamento
├── memory.py            # Classes VirtualMemory e PhysicalMemory
├── page_replacement.py  # Algoritmos de substituição (FIFO e LRU)
├── memory_manager.py    # Gerenciador principal de memória
└── main.py              # Programa principal com demonstrações
```

## Requisitos

- Python 3.6 ou superior

## Como Executar

### Modo Interativo

Execute o programa principal para acessar o menu de demonstrações:

```bash
python3 main.py
```

O menu oferece as seguintes opções:
1. Demonstrar algoritmo FIFO
2. Demonstrar algoritmo LRU
3. Demonstrar leitura e escrita
4. Comparar FIFO vs LRU
5. Executar todas as demonstrações

### Uso Programático

Você também pode importar e usar o simulador em seus próprios scripts:

```python
from memory_manager import MemoryManager

# Cria um gerenciador com 8 páginas virtuais, 3 molduras físicas
# Páginas de 4KB, usando algoritmo FIFO
manager = MemoryManager(
    num_virtual_pages=8,
    num_physical_frames=3,
    page_size=4096,
    algorithm='FIFO'  # ou 'LRU'
)

# Acessa páginas
manager.access_page(0)
manager.access_page(1)
manager.access_page(2)

# Escreve dados
manager.write_to_page(3, "Meus dados")

# Lê dados
data = manager.read_from_page(3)

# Exibe estatísticas
manager.print_statistics()
manager.print_status()
```

## Componentes Principais

### Page e PageFrame

- **Page**: Representa uma página na memória virtual com número identificador e dados
- **PageFrame**: Representa uma moldura na memória física que pode conter uma página

### VirtualMemory e PhysicalMemory

- **VirtualMemory**: Gerencia o conjunto de páginas virtuais
- **PhysicalMemory**: Gerencia o conjunto de molduras físicas e encontra molduras livres

### PageTable

Mantém o mapeamento entre páginas virtuais e molduras físicas, incluindo:
- Bit de presença (present bit)
- Bit de referência (referenced bit)
- Bit de modificação (modified bit)

### Algoritmos de Substituição

#### FIFO (First-In, First-Out)
- Substitui a página que está há mais tempo na memória
- Implementação simples usando uma fila

#### LRU (Least Recently Used)
- Substitui a página que não foi usada por mais tempo
- Mantém registro de quando cada página foi acessada

### MemoryManager

Coordena todos os componentes:
- Gerencia page faults e page hits
- Carrega páginas na memória física
- Executa algoritmos de substituição quando necessário
- Mantém estatísticas de acesso

## Conceitos Demonstrados

1. **Page Fault**: Ocorre quando uma página acessada não está na memória física
2. **Page Hit**: Ocorre quando uma página acessada já está na memória física
3. **Substituição de Páginas**: Quando não há molduras livres, uma página existente deve ser removida
4. **Mapeamento Virtual-Físico**: Tabela de páginas traduz endereços virtuais em físicos

## Exemplo de Saída

```
--- Acessando página 0 ---
✗ Page Fault: Página 0 não está na memória física
  → Carregando página 0 na moldura livre 0

--- Acessando página 1 ---
✗ Page Fault: Página 1 não está na memória física
  → Carregando página 1 na moldura livre 1

--- Acessando página 0 ---
✓ Page Hit: Página 0 já está na moldura 0

============================================================
ESTATÍSTICAS DO GERENCIADOR DE MEMÓRIA
============================================================
Total de acessos: 3
Page Hits: 1 (33.33%)
Page Faults: 2 (66.67%)
Algoritmo de substituição: FIFOPageReplacement
============================================================
```

## Autores

Juliano Sobroza

## Licença

Este projeto foi desenvolvido para fins educacionais como parte do Trabalho Prático 2 de Sistemas Operacionais.

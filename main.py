#!/usr/bin/env python3
"""
Programa principal para demonstrar o simulador de gerenciamento de memória.

Este programa cria um simulador de memória com paginação e demonstra seu funcionamento
através de diferentes cenários de acesso à memória.
"""

from memory_manager import MemoryManager


def print_header(title):
    """Imprime um cabeçalho formatado."""
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def demonstrate_fifo():
    """Demonstra o funcionamento do algoritmo FIFO."""
    print_header("DEMONSTRAÇÃO: Algoritmo FIFO")
    
    # Cria um gerenciador com memória virtual de 8 páginas e física de 3 molduras
    manager = MemoryManager(
        num_virtual_pages=8,
        num_physical_frames=3,
        page_size=4096,  # 4KB por página
        algorithm='FIFO'
    )
    
    print("\nConfiguração:")
    print(f"  - Memória Virtual: 8 páginas de 4KB (32 KB total)")
    print(f"  - Memória Física: 3 molduras de 4KB (12 KB total)")
    print(f"  - Algoritmo: FIFO")
    
    # Sequência de acessos que demonstra o FIFO
    access_sequence = [0, 1, 2, 3, 0, 1, 4, 0, 1, 2, 3, 4]
    
    print(f"\nSequência de acessos: {access_sequence}")
    print("\nExecutando acessos...\n")
    
    for page_num in access_sequence:
        print(f"\n--- Acessando página {page_num} ---")
        manager.access_page(page_num)
    
    # Imprime status final
    manager.print_status()


def demonstrate_lru():
    """Demonstra o funcionamento do algoritmo LRU."""
    print_header("DEMONSTRAÇÃO: Algoritmo LRU")
    
    # Cria um gerenciador com memória virtual de 8 páginas e física de 3 molduras
    manager = MemoryManager(
        num_virtual_pages=8,
        num_physical_frames=3,
        page_size=4096,  # 4KB por página
        algorithm='LRU'
    )
    
    print("\nConfiguração:")
    print(f"  - Memória Virtual: 8 páginas de 4KB (32 KB total)")
    print(f"  - Memória Física: 3 molduras de 4KB (12 KB total)")
    print(f"  - Algoritmo: LRU")
    
    # Sequência de acessos que demonstra o LRU
    access_sequence = [0, 1, 2, 3, 0, 1, 4, 0, 1, 2, 3, 4]
    
    print(f"\nSequência de acessos: {access_sequence}")
    print("\nExecutando acessos...\n")
    
    for page_num in access_sequence:
        print(f"\n--- Acessando página {page_num} ---")
        manager.access_page(page_num)
    
    # Imprime status final
    manager.print_status()


def demonstrate_read_write():
    """Demonstra operações de leitura e escrita."""
    print_header("DEMONSTRAÇÃO: Leitura e Escrita")
    
    manager = MemoryManager(
        num_virtual_pages=5,
        num_physical_frames=3,
        page_size=4096,
        algorithm='LRU'
    )
    
    print("\nConfiguração:")
    print(f"  - Memória Virtual: 5 páginas de 4KB")
    print(f"  - Memória Física: 3 molduras de 4KB")
    print(f"  - Algoritmo: LRU")
    
    print("\n--- Operações de Escrita ---")
    
    # Escreve dados em algumas páginas
    manager.write_to_page(0, "Dados da página 0")
    manager.write_to_page(1, "Dados da página 1")
    manager.write_to_page(2, "Dados da página 2")
    
    print("\n--- Operações de Leitura ---")
    
    # Lê dados das páginas
    data0 = manager.read_from_page(0)
    print(f"Dados lidos da página 0: {data0}")
    
    data1 = manager.read_from_page(1)
    print(f"Dados lidos da página 1: {data1}")
    
    # Acessa uma nova página, causando substituição
    print("\n--- Acessando novas páginas ---")
    manager.write_to_page(3, "Dados da página 3")
    manager.write_to_page(4, "Dados da página 4")
    
    # Tenta ler a página 2 novamente
    print("\n--- Relendo página 2 ---")
    data2 = manager.read_from_page(2)
    print(f"Dados lidos da página 2: {data2}")
    
    manager.print_status()


def compare_algorithms():
    """Compara o desempenho dos algoritmos FIFO e LRU."""
    print_header("COMPARAÇÃO: FIFO vs LRU")
    
    # Sequência de acesso comum
    access_sequence = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    
    print(f"\nSequência de acessos: {access_sequence}")
    print("Configuração: 5 páginas virtuais, 3 molduras físicas\n")
    
    # Testa com FIFO
    print("\n--- Executando com FIFO ---")
    fifo_manager = MemoryManager(5, 3, 4096, 'FIFO')
    for page_num in access_sequence:
        fifo_manager.access_page(page_num)
    
    # Testa com LRU
    print("\n--- Executando com LRU ---")
    lru_manager = MemoryManager(5, 3, 4096, 'LRU')
    for page_num in access_sequence:
        lru_manager.access_page(page_num)
    
    # Compara resultados
    print("\n" + "=" * 60)
    print("COMPARAÇÃO DE RESULTADOS")
    print("=" * 60)
    
    print("\nFIFO:")
    print(f"  Page Hits: {fifo_manager.page_hits}")
    print(f"  Page Faults: {fifo_manager.page_faults}")
    
    print("\nLRU:")
    print(f"  Page Hits: {lru_manager.page_hits}")
    print(f"  Page Faults: {lru_manager.page_faults}")
    
    # Determina qual foi melhor
    if lru_manager.page_faults < fifo_manager.page_faults:
        print("\n✓ LRU teve melhor desempenho (menos page faults)")
    elif fifo_manager.page_faults < lru_manager.page_faults:
        print("\n✓ FIFO teve melhor desempenho (menos page faults)")
    else:
        print("\n✓ Ambos tiveram desempenho igual")


def main():
    """Função principal que executa todas as demonstrações."""
    print_header("SIMULADOR DE GERENCIAMENTO DE MEMÓRIA COM PAGINAÇÃO")
    print("\nEste simulador demonstra o funcionamento de um sistema de")
    print("gerenciamento de memória com paginação, incluindo:")
    print("  • Memória virtual dividida em páginas")
    print("  • Memória física dividida em molduras")
    print("  • Tabela de páginas para mapeamento")
    print("  • Algoritmos de substituição (FIFO e LRU)")
    
    while True:
        print("\n" + "=" * 60)
        print("MENU DE DEMONSTRAÇÕES")
        print("=" * 60)
        print("1. Demonstrar algoritmo FIFO")
        print("2. Demonstrar algoritmo LRU")
        print("3. Demonstrar leitura e escrita")
        print("4. Comparar FIFO vs LRU")
        print("5. Executar todas as demonstrações")
        print("0. Sair")
        print("=" * 60)
        
        choice = input("\nEscolha uma opção: ").strip()
        
        if choice == '1':
            demonstrate_fifo()
        elif choice == '2':
            demonstrate_lru()
        elif choice == '3':
            demonstrate_read_write()
        elif choice == '4':
            compare_algorithms()
        elif choice == '5':
            demonstrate_fifo()
            demonstrate_lru()
            demonstrate_read_write()
            compare_algorithms()
        elif choice == '0':
            print("\nEncerrando simulador...")
            break
        else:
            print("\n✗ Opção inválida! Tente novamente.")
        
        input("\nPressione ENTER para continuar...")


if __name__ == '__main__':
    main()

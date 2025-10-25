"""
Simulador de gerenciamento de memória com paginação.

Este módulo implementa um simulador completo de gerenciamento de memória que inclui:
- Memória virtual dividida em páginas de tamanho fixo
- Memória física dividida em molduras de página
- Tabela de páginas para mapeamento
- Algoritmos de substituição de páginas (FIFO e LRU)
"""

from memory import VirtualMemory, PhysicalMemory
from page_table import PageTable
from page_replacement import FIFOPageReplacement, LRUPageReplacement


class MemoryManager:
    """
    Gerenciador de memória que coordena a memória virtual, física e tabela de páginas.
    
    Attributes:
        virtual_memory: Instância da memória virtual
        physical_memory: Instância da memória física
        page_table: Tabela de páginas
        replacement_algorithm: Algoritmo de substituição de páginas
        page_faults: Contador de page faults
        page_hits: Contador de page hits
    """
    
    def __init__(self, num_virtual_pages, num_physical_frames, page_size, algorithm='FIFO'):
        """
        Inicializa o gerenciador de memória.
        
        Args:
            num_virtual_pages: Número de páginas na memória virtual
            num_physical_frames: Número de molduras na memória física
            page_size: Tamanho de cada página/moldura em bytes
            algorithm: Algoritmo de substituição ('FIFO' ou 'LRU')
        """
        self.virtual_memory = VirtualMemory(num_virtual_pages, page_size)
        self.physical_memory = PhysicalMemory(num_physical_frames, page_size)
        self.page_table = PageTable(num_virtual_pages)
        
        # Seleciona o algoritmo de substituição
        if algorithm.upper() == 'FIFO':
            self.replacement_algorithm = FIFOPageReplacement(num_physical_frames)
        elif algorithm.upper() == 'LRU':
            self.replacement_algorithm = LRUPageReplacement(num_physical_frames)
        else:
            raise ValueError(f"Algoritmo desconhecido: {algorithm}")
        
        self.page_faults = 0
        self.page_hits = 0
    
    def access_page(self, page_number, write=False):
        """
        Acessa uma página da memória virtual.
        
        Args:
            page_number: Número da página a ser acessada
            write: Se True, marca a página como modificada
            
        Returns:
            Tuple (page_fault, frame_number) indicando se houve page fault e o número da moldura
        """
        # Verifica se a página está na memória física
        if self.page_table.is_page_present(page_number):
            # Page hit
            self.page_hits += 1
            frame_number = self.page_table.get_frame_number(page_number)
            
            # Marca como referenciada
            self.page_table.set_referenced(page_number, True)
            self.replacement_algorithm.page_referenced(frame_number)
            
            # Marca como modificada se for escrita
            if write:
                self.page_table.set_modified(page_number, True)
            
            print(f"✓ Page Hit: Página {page_number} já está na moldura {frame_number}")
            return (False, frame_number)
        else:
            # Page fault
            self.page_faults += 1
            print(f"✗ Page Fault: Página {page_number} não está na memória física")
            
            # Carrega a página na memória física
            frame_number = self._load_page(page_number)
            
            # Marca como referenciada
            self.page_table.set_referenced(page_number, True)
            
            # Marca como modificada se for escrita
            if write:
                self.page_table.set_modified(page_number, True)
            
            return (True, frame_number)
    
    def _load_page(self, page_number):
        """
        Carrega uma página na memória física.
        
        Args:
            page_number: Número da página a ser carregada
            
        Returns:
            Número da moldura onde a página foi carregada
        """
        # Obtém a página da memória virtual
        page = self.virtual_memory.get_page(page_number)
        
        # Procura uma moldura livre
        frame_number = self.physical_memory.find_free_frame()
        
        if frame_number is not None:
            # Há moldura livre
            print(f"  → Carregando página {page_number} na moldura livre {frame_number}")
        else:
            # Não há moldura livre, precisa substituir
            frame_number = self.replacement_algorithm.select_victim()
            
            if frame_number is None:
                raise RuntimeError("Nenhuma moldura disponível para substituição")
            
            evicted_page = self.physical_memory.get_frame(frame_number).page
            
            if evicted_page:
                print(f"  → Substituindo página {evicted_page.page_number} na moldura {frame_number}")
                
                # Atualiza a tabela de páginas para a página removida
                self.page_table.unmap_page(evicted_page.page_number)
                
                # Notifica o algoritmo sobre a remoção
                if hasattr(self.replacement_algorithm, 'page_evicted'):
                    self.replacement_algorithm.page_evicted(frame_number)
        
        # Carrega a página na moldura
        self.physical_memory.load_page_into_frame(page, frame_number)
        
        # Atualiza a tabela de páginas
        self.page_table.map_page(page_number, frame_number)
        
        # Notifica o algoritmo de substituição
        self.replacement_algorithm.page_loaded(frame_number, page_number)
        
        return frame_number
    
    def write_to_page(self, page_number, data):
        """
        Escreve dados em uma página.
        
        Args:
            page_number: Número da página
            data: Dados a serem escritos
        """
        # Escreve na memória virtual
        self.virtual_memory.write_data(page_number, data)
        
        # Acessa a página (pode causar page fault)
        self.access_page(page_number, write=True)
    
    def read_from_page(self, page_number):
        """
        Lê dados de uma página.
        
        Args:
            page_number: Número da página
            
        Returns:
            Dados da página
        """
        # Acessa a página (pode causar page fault)
        self.access_page(page_number, write=False)
        
        # Lê da memória virtual
        page = self.virtual_memory.get_page(page_number)
        return page.data
    
    def print_statistics(self):
        """Imprime estatísticas do gerenciador de memória."""
        total_accesses = self.page_hits + self.page_faults
        hit_rate = (self.page_hits / total_accesses * 100) if total_accesses > 0 else 0
        fault_rate = (self.page_faults / total_accesses * 100) if total_accesses > 0 else 0
        
        print("\n" + "=" * 60)
        print("ESTATÍSTICAS DO GERENCIADOR DE MEMÓRIA")
        print("=" * 60)
        print(f"Total de acessos: {total_accesses}")
        print(f"Page Hits: {self.page_hits} ({hit_rate:.2f}%)")
        print(f"Page Faults: {self.page_faults} ({fault_rate:.2f}%)")
        print(f"Algoritmo de substituição: {type(self.replacement_algorithm).__name__}")
        print("=" * 60)
    
    def print_status(self):
        """Imprime o status completo do sistema de memória."""
        print("\n" + "=" * 60)
        print("STATUS DO SISTEMA DE MEMÓRIA")
        print("=" * 60)
        print(f"\n{self.virtual_memory}")
        print(f"{self.physical_memory}")
        self.physical_memory.print_memory_status()
        self.page_table.print_table()
        self.print_statistics()

"""
Classe que representa a tabela de páginas para mapeamento entre memória virtual e física.
"""

class PageTableEntry:
    """
    Representa uma entrada na tabela de páginas.
    
    Attributes:
        page_number: Número da página virtual
        frame_number: Número da moldura física (None se não mapeada)
        present_bit: Indica se a página está presente na memória física
        referenced_bit: Indica se a página foi recentemente referenciada
        modified_bit: Indica se a página foi modificada
    """
    
    def __init__(self, page_number):
        """
        Inicializa uma entrada da tabela de páginas.
        
        Args:
            page_number: Número da página virtual
        """
        self.page_number = page_number
        self.frame_number = None
        self.present_bit = False
        self.referenced_bit = False
        self.modified_bit = False
    
    def __repr__(self):
        return (f"PageTableEntry(page={self.page_number}, frame={self.frame_number}, "
                f"present={self.present_bit}, ref={self.referenced_bit}, mod={self.modified_bit})")


class PageTable:
    """
    Tabela de páginas para mapear páginas virtuais para molduras físicas.
    
    Attributes:
        entries: Lista de entradas da tabela de páginas
        num_pages: Número total de páginas virtuais
    """
    
    def __init__(self, num_pages):
        """
        Inicializa a tabela de páginas.
        
        Args:
            num_pages: Número de páginas na memória virtual
        """
        self.num_pages = num_pages
        self.entries = [PageTableEntry(i) for i in range(num_pages)]
    
    def map_page(self, page_number, frame_number):
        """
        Mapeia uma página virtual para uma moldura física.
        
        Args:
            page_number: Número da página virtual
            frame_number: Número da moldura física
        """
        if 0 <= page_number < self.num_pages:
            entry = self.entries[page_number]
            entry.frame_number = frame_number
            entry.present_bit = True
        else:
            raise ValueError(f"Número de página inválido: {page_number}")
    
    def unmap_page(self, page_number):
        """
        Remove o mapeamento de uma página virtual.
        
        Args:
            page_number: Número da página virtual
        """
        if 0 <= page_number < self.num_pages:
            entry = self.entries[page_number]
            entry.frame_number = None
            entry.present_bit = False
            entry.referenced_bit = False
            entry.modified_bit = False
        else:
            raise ValueError(f"Número de página inválido: {page_number}")
    
    def get_frame_number(self, page_number):
        """
        Retorna o número da moldura física para uma página virtual.
        
        Args:
            page_number: Número da página virtual
            
        Returns:
            Número da moldura física ou None se a página não estiver mapeada
        """
        if 0 <= page_number < self.num_pages:
            entry = self.entries[page_number]
            if entry.present_bit:
                return entry.frame_number
            return None
        raise ValueError(f"Número de página inválido: {page_number}")
    
    def is_page_present(self, page_number):
        """
        Verifica se uma página está presente na memória física.
        
        Args:
            page_number: Número da página virtual
            
        Returns:
            True se a página está presente, False caso contrário
        """
        if 0 <= page_number < self.num_pages:
            return self.entries[page_number].present_bit
        raise ValueError(f"Número de página inválido: {page_number}")
    
    def set_referenced(self, page_number, value=True):
        """
        Define o bit de referência de uma página.
        
        Args:
            page_number: Número da página virtual
            value: Valor do bit de referência
        """
        if 0 <= page_number < self.num_pages:
            self.entries[page_number].referenced_bit = value
        else:
            raise ValueError(f"Número de página inválido: {page_number}")
    
    def set_modified(self, page_number, value=True):
        """
        Define o bit de modificação de uma página.
        
        Args:
            page_number: Número da página virtual
            value: Valor do bit de modificação
        """
        if 0 <= page_number < self.num_pages:
            self.entries[page_number].modified_bit = value
        else:
            raise ValueError(f"Número de página inválido: {page_number}")
    
    def print_table(self):
        """Imprime o estado atual da tabela de páginas."""
        print("\n=== Tabela de Páginas ===")
        print(f"{'Página':<8} {'Moldura':<10} {'Presente':<10} {'Ref':<8} {'Mod':<8}")
        print("-" * 52)
        for entry in self.entries:
            frame = entry.frame_number if entry.frame_number is not None else "N/A"
            print(f"{entry.page_number:<8} {str(frame):<10} {entry.present_bit!s:<10} "
                  f"{entry.referenced_bit!s:<8} {entry.modified_bit!s:<8}")

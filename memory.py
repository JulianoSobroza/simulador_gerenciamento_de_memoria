"""
Classes que representam a memória virtual e física.
"""

from page import Page, PageFrame


class VirtualMemory:
    """
    Representa a memória virtual do sistema.
    
    Attributes:
        num_pages: Número total de páginas virtuais
        page_size: Tamanho de cada página em bytes
        pages: Lista de páginas virtuais
    """
    
    def __init__(self, num_pages, page_size):
        """
        Inicializa a memória virtual.
        
        Args:
            num_pages: Número de páginas virtuais
            page_size: Tamanho de cada página em bytes
        """
        self.num_pages = num_pages
        self.page_size = page_size
        self.pages = [Page(i) for i in range(num_pages)]
        self.total_size = num_pages * page_size
    
    def get_page(self, page_number):
        """
        Retorna uma página específica.
        
        Args:
            page_number: Número da página
            
        Returns:
            A página solicitada
        """
        if 0 <= page_number < self.num_pages:
            return self.pages[page_number]
        raise ValueError(f"Número de página inválido: {page_number}")
    
    def write_data(self, page_number, data):
        """
        Escreve dados em uma página.
        
        Args:
            page_number: Número da página
            data: Dados a serem escritos
        """
        if 0 <= page_number < self.num_pages:
            self.pages[page_number].data = data
        else:
            raise ValueError(f"Número de página inválido: {page_number}")
    
    def __repr__(self):
        return f"VirtualMemory(pages={self.num_pages}, page_size={self.page_size}, total={self.total_size} bytes)"


class PhysicalMemory:
    """
    Representa a memória física do sistema.
    
    Attributes:
        num_frames: Número total de molduras de página
        page_size: Tamanho de cada moldura em bytes
        frames: Lista de molduras de página
    """
    
    def __init__(self, num_frames, page_size):
        """
        Inicializa a memória física.
        
        Args:
            num_frames: Número de molduras de página
            page_size: Tamanho de cada moldura em bytes
        """
        self.num_frames = num_frames
        self.page_size = page_size
        self.frames = [PageFrame(i) for i in range(num_frames)]
        self.total_size = num_frames * page_size
    
    def get_frame(self, frame_number):
        """
        Retorna uma moldura específica.
        
        Args:
            frame_number: Número da moldura
            
        Returns:
            A moldura solicitada
        """
        if 0 <= frame_number < self.num_frames:
            return self.frames[frame_number]
        raise ValueError(f"Número de moldura inválido: {frame_number}")
    
    def find_free_frame(self):
        """
        Encontra uma moldura livre.
        
        Returns:
            Número da primeira moldura livre ou None se não houver
        """
        for frame in self.frames:
            if frame.is_free():
                return frame.frame_number
        return None
    
    def load_page_into_frame(self, page, frame_number):
        """
        Carrega uma página em uma moldura específica.
        
        Args:
            page: Página a ser carregada
            frame_number: Número da moldura
        """
        if 0 <= frame_number < self.num_frames:
            self.frames[frame_number].load_page(page)
        else:
            raise ValueError(f"Número de moldura inválido: {frame_number}")
    
    def evict_page_from_frame(self, frame_number):
        """
        Remove uma página de uma moldura.
        
        Args:
            frame_number: Número da moldura
            
        Returns:
            A página removida
        """
        if 0 <= frame_number < self.num_frames:
            return self.frames[frame_number].evict_page()
        raise ValueError(f"Número de moldura inválido: {frame_number}")
    
    def get_num_free_frames(self):
        """
        Retorna o número de molduras livres.
        
        Returns:
            Número de molduras livres
        """
        return sum(1 for frame in self.frames if frame.is_free())
    
    def get_num_used_frames(self):
        """
        Retorna o número de molduras ocupadas.
        
        Returns:
            Número de molduras ocupadas
        """
        return self.num_frames - self.get_num_free_frames()
    
    def print_memory_status(self):
        """Imprime o status atual da memória física."""
        print("\n=== Memória Física ===")
        print(f"Total de molduras: {self.num_frames}")
        print(f"Molduras livres: {self.get_num_free_frames()}")
        print(f"Molduras ocupadas: {self.get_num_used_frames()}")
        print("\nEstado das molduras:")
        for frame in self.frames:
            status = f"Página {frame.page.page_number}" if frame.page else "Livre"
            print(f"  Moldura {frame.frame_number}: {status}")
    
    def __repr__(self):
        return f"PhysicalMemory(frames={self.num_frames}, page_size={self.page_size}, total={self.total_size} bytes)"

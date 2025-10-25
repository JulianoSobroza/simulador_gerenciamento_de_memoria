"""
Classe que representa uma página na memória virtual.
"""

class Page:
    """
    Representa uma página na memória virtual.
    
    Attributes:
        page_number: Número identificador da página
        data: Dados armazenados na página
    """
    
    def __init__(self, page_number, data=None):
        """
        Inicializa uma página.
        
        Args:
            page_number: Número identificador da página
            data: Dados iniciais da página (opcional)
        """
        self.page_number = page_number
        self.data = data if data is not None else []
    
    def __repr__(self):
        return f"Page(number={self.page_number}, data={self.data[:10]}...)" if len(self.data) > 10 else f"Page(number={self.page_number}, data={self.data})"


class PageFrame:
    """
    Representa uma moldura de página (page frame) na memória física.
    
    Attributes:
        frame_number: Número identificador da moldura
        page: Referência à página armazenada nesta moldura (None se vazia)
    """
    
    def __init__(self, frame_number):
        """
        Inicializa uma moldura de página.
        
        Args:
            frame_number: Número identificador da moldura
        """
        self.frame_number = frame_number
        self.page = None
    
    def is_free(self):
        """Verifica se a moldura está livre."""
        return self.page is None
    
    def load_page(self, page):
        """
        Carrega uma página na moldura.
        
        Args:
            page: Página a ser carregada
        """
        self.page = page
    
    def evict_page(self):
        """
        Remove a página da moldura.
        
        Returns:
            A página removida
        """
        evicted_page = self.page
        self.page = None
        return evicted_page
    
    def __repr__(self):
        if self.page:
            return f"Frame(number={self.frame_number}, page={self.page.page_number})"
        return f"Frame(number={self.frame_number}, page=None)"

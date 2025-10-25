"""
Algoritmos de substituição de páginas.
"""

from collections import deque


class PageReplacementAlgorithm:
    """Classe base para algoritmos de substituição de páginas."""
    
    def __init__(self, num_frames):
        """
        Inicializa o algoritmo de substituição.
        
        Args:
            num_frames: Número de molduras na memória física
        """
        self.num_frames = num_frames
    
    def select_victim(self):
        """
        Seleciona uma moldura vítima para substituição.
        
        Returns:
            Número da moldura a ser substituída
        """
        raise NotImplementedError("Subclasses devem implementar este método")
    
    def page_loaded(self, frame_number, page_number):
        """
        Notifica o algoritmo que uma página foi carregada.
        
        Args:
            frame_number: Número da moldura
            page_number: Número da página carregada
        """
        raise NotImplementedError("Subclasses devem implementar este método")
    
    def page_referenced(self, frame_number):
        """
        Notifica o algoritmo que uma página foi referenciada.
        
        Args:
            frame_number: Número da moldura
        """
        pass  # Opcional para alguns algoritmos


class FIFOPageReplacement(PageReplacementAlgorithm):
    """
    Algoritmo de substituição de páginas FIFO (First-In, First-Out).
    
    A primeira página carregada é a primeira a ser substituída.
    """
    
    def __init__(self, num_frames):
        """
        Inicializa o algoritmo FIFO.
        
        Args:
            num_frames: Número de molduras na memória física
        """
        super().__init__(num_frames)
        self.queue = deque()
    
    def select_victim(self):
        """
        Seleciona a moldura mais antiga para substituição.
        
        Returns:
            Número da moldura a ser substituída
        """
        if self.queue:
            return self.queue[0]
        return None
    
    def page_loaded(self, frame_number, page_number):
        """
        Adiciona a moldura ao final da fila.
        
        Args:
            frame_number: Número da moldura
            page_number: Número da página carregada
        """
        if frame_number in self.queue:
            # Remove se já existir (para evitar duplicatas)
            self.queue.remove(frame_number)
        self.queue.append(frame_number)
    
    def page_evicted(self, frame_number):
        """
        Remove a moldura da fila quando uma página é removida.
        
        Args:
            frame_number: Número da moldura
        """
        if frame_number in self.queue:
            self.queue.remove(frame_number)
    
    def __repr__(self):
        return f"FIFO(queue={list(self.queue)})"


class LRUPageReplacement(PageReplacementAlgorithm):
    """
    Algoritmo de substituição de páginas LRU (Least Recently Used).
    
    A página que não foi usada por mais tempo é substituída.
    """
    
    def __init__(self, num_frames):
        """
        Inicializa o algoritmo LRU.
        
        Args:
            num_frames: Número de molduras na memória física
        """
        super().__init__(num_frames)
        self.usage_order = deque()
    
    def select_victim(self):
        """
        Seleciona a moldura menos recentemente usada.
        
        Returns:
            Número da moldura a ser substituída
        """
        if self.usage_order:
            return self.usage_order[0]
        return None
    
    def page_loaded(self, frame_number, page_number):
        """
        Marca a moldura como recentemente usada.
        
        Args:
            frame_number: Número da moldura
            page_number: Número da página carregada
        """
        self._mark_as_used(frame_number)
    
    def page_referenced(self, frame_number):
        """
        Marca a moldura como recentemente usada quando referenciada.
        
        Args:
            frame_number: Número da moldura
        """
        self._mark_as_used(frame_number)
    
    def _mark_as_used(self, frame_number):
        """
        Move a moldura para o final da fila de uso.
        
        Args:
            frame_number: Número da moldura
        """
        if frame_number in self.usage_order:
            self.usage_order.remove(frame_number)
        self.usage_order.append(frame_number)
    
    def page_evicted(self, frame_number):
        """
        Remove a moldura da fila quando uma página é removida.
        
        Args:
            frame_number: Número da moldura
        """
        if frame_number in self.usage_order:
            self.usage_order.remove(frame_number)
    
    def __repr__(self):
        return f"LRU(usage_order={list(self.usage_order)})"

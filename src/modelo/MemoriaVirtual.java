package modelo;

public class MemoriaVirtual {
    private final Pagina[] paginas;

    public MemoriaVirtual(int totalPaginas) {
        this.paginas = new Pagina[totalPaginas];
        for (int i = 0; i < totalPaginas; i++) {
            paginas[i] = new Pagina(i);
        }
    }

    public Pagina getPagina(int numero) {
        return paginas[numero];
    }
}

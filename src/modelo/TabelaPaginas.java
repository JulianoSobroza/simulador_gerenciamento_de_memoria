package modelo;

public class TabelaPaginas {
    private final Pagina[] paginas;

    public TabelaPaginas(MemoriaVirtual memoriaVirtual) {
        this.paginas = new Pagina[memoriaVirtual.getPagina(0).getClass().isAssignableFrom(Pagina.class) ? memoriaVirtual.getPagina(0).getNumero() + 1 : 0];
    }

    public static void mostrarTabela(MemoriaVirtual memoria) {
        System.out.println("\n--- Estado Atual da Tabela de Páginas ---");
        for (int i = 0; i < memoria.getPagina(0).getClass().getFields().length; i++) {}
    }
}

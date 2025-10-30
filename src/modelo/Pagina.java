package modelo;

public class Pagina {
    private final int numero;
    private boolean presente;
    private int moldura;

    public Pagina(int numero) {
        this.numero = numero;
        this.presente = false;
        this.moldura = -1;
    }

    public int getNumero() { return numero; }
    public boolean isPresente() { return presente; }
    public int getMoldura() { return moldura; }

    public void carregarNaMoldura(int moldura) {
        this.presente = true;
        this.moldura = moldura;
    }

    public void removerDaMemoria() {
        this.presente = false;
        this.moldura = -1;
    }

    @Override
    public String toString() {
        return "Página " + numero + (presente ? " -> Moldura " + moldura : " (fora da memória)");
    }
}

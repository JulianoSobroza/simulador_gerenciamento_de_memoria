package modelo;

import java.util.LinkedList;
import java.util.Queue;

public class MemoriaFisica {
    private final int totalMolduras;
    private final Queue<Integer> moldurasOcupadas;

    public MemoriaFisica(int totalMolduras) {
        this.totalMolduras = totalMolduras;
        this.moldurasOcupadas = new LinkedList<>();
    }

    public boolean estaCheia() {
        return moldurasOcupadas.size() >= totalMolduras;
    }

    public int alocarMoldura(int pagina) {
        if (estaCheia()) {
            return -1; // precisa substituir
        }
        moldurasOcupadas.add(pagina);
        return moldurasOcupadas.size() - 1; // índice da moldura
    }

    public int substituirPagina() {
        return moldurasOcupadas.poll(); // remove a mais antiga (FIFO)
    }

    public void adicionarPagina(int pagina) {
        moldurasOcupadas.add(pagina);
    }

    public Queue<Integer> getMoldurasOcupadas() {
        return moldurasOcupadas;
    }
}

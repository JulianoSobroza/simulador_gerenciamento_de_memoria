package modelo;

import java.util.*;

public class SimuladorFIFO {
    private final MemoriaFisica memoriaFisica;
    private final MemoriaVirtual memoriaVirtual;
    private final int[] acessos;
    private int falhasPagina = 0;

    public SimuladorFIFO(int tamFisica, int tamVirtual, int[] acessos) {
        this.memoriaFisica = new MemoriaFisica(tamFisica);
        this.memoriaVirtual = new MemoriaVirtual(tamVirtual);
        this.acessos = acessos;
    }

    public void executar() {
        System.out.println("\nIniciando simulação FIFO...\n");

        for (int endereco : acessos) {
            Pagina pagina = memoriaVirtual.getPagina(endereco);
            System.out.println("Acessando página virtual: " + endereco);

            if (pagina.isPresente()) {
                System.out.println("→ Página já está na memória (moldura " + pagina.getMoldura() + ")");
            } else {
                falhasPagina++;
                System.out.println("⚠ Falha de página! Página " + endereco + " não está na memória.");

                if (!memoriaFisica.estaCheia()) {
                    int moldura = memoriaFisica.alocarMoldura(endereco);
                    pagina.carregarNaMoldura(moldura);
                } else {
                    int paginaRemovida = memoriaFisica.substituirPagina();
                    Pagina antiga = memoriaVirtual.getPagina(paginaRemovida);
                    antiga.removerDaMemoria();

                    int moldura = memoriaFisica.getMoldurasOcupadas().size();
                    memoriaFisica.adicionarPagina(endereco);
                    pagina.carregarNaMoldura(moldura);
                    System.out.println("→ Página " + paginaRemovida + " removida da memória (FIFO).");
                }
            }
            mostrarEstado();
        }

        System.out.println("\nSimulação encerrada.");
        System.out.println("Total de falhas de página: " + falhasPagina);
    }

    private void mostrarEstado() {
        System.out.println("\nEstado atual das molduras:");
        int idx = 0;
        for (int p : memoriaFisica.getMoldurasOcupadas()) {
            System.out.println("Moldura " + idx + " -> Página " + p);
            idx++;
        }
        System.out.println("------------------------------\n");
    }
}

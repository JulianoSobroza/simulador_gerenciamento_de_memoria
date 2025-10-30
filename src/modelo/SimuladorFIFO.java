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

                    int moldura = antiga.getMoldura();
                    antiga.removerDaMemoria();

                    //int moldura = memoriaFisica.getMoldurasOcupadas().size();   errado

                    memoriaFisica.adicionarPagina(endereco);

                    pagina.carregarNaMoldura(moldura);
                    //System.out.println("→ Página " + paginaRemovida + " removida da memória (FIFO).");
                    System.out.println("→ Página " + paginaRemovida + " removida da moldura " + moldura + " (FIFO).");
                }
            }
            mostrarEstado(); // Exibe as molduras
            mostrarTabelaDePaginas();
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

    //NOVO METODO test
    private void mostrarTabelaDePaginas() {
        System.out.println("\n--- Tabela de Páginas ---");
        System.out.println("Página | Presença | Moldura");
        System.out.println("-------------------------");

        // Itera sobre todas as páginas virtuais
        for (int i = 0; i < memoriaVirtual.getTotalPaginas(); i++) {
            Pagina p = memoriaVirtual.getPagina(i);
            String presente = p.isPresente() ? "SIM" : "NÃO";
            String moldura = p.isPresente() ? String.valueOf(p.getMoldura()) : "-";

            // Usa formatação para alinhar as colunas
            System.out.printf("%6d | %8s | %7s\n", i, presente, moldura);
        }
        System.out.println("-------------------------\n");
    }
}

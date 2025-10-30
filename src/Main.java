import modelo.SimuladorFIFO;
import utils.LeitorArquivo;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        System.out.println("=== SIMULADOR DE GERENCIAMENTO DE MEMÓRIA (FIFO) ===");

        try {
            // Lê parâmetros do arquivo de texto
            List<String> linhas = LeitorArquivo.lerArquivo("src/config.txt");

            int tamanhoMemoriaFisica = Integer.parseInt(linhas.get(0).trim());
            int tamanhoMemoriaVirtual = Integer.parseInt(linhas.get(1).trim());
            String[] acessosStr = linhas.get(2).trim().split(" ");
            int[] acessos = new int[acessosStr.length];

            for (int i = 0; i < acessosStr.length; i++) {
                acessos[i] = Integer.parseInt(acessosStr[i]);
            }

            // Executa simulação
            SimuladorFIFO simulador = new SimuladorFIFO(
                    tamanhoMemoriaFisica,
                    tamanhoMemoriaVirtual,
                    acessos
            );

            simulador.executar();

        } catch (Exception e) {
            System.err.println("Erro ao executar simulação: " + e.getMessage());
        }
    }
}

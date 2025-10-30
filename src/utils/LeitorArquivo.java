package utils;

import java.io.*;
import java.util.*;

public class LeitorArquivo {
    public static List<String> lerArquivo(String caminho) throws IOException {
        List<String> linhas = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(caminho))) {
            String linha;
            while ((linha = br.readLine()) != null) {
                linha = linha.trim();
                if (!linha.isEmpty() && !linha.startsWith("#")) {
                    linhas.add(linha);
                }
            }
        }
        return linhas;
    }
}

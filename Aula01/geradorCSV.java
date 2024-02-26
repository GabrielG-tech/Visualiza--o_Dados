import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.text.DecimalFormat;

// Elabore um programa em Java no ambiente replit que gere um arquivo csv para o domínio de -5 a 5 com passo 0,1 para a função ao lado: f(x)=x+2

// Em seguida, envie este arquivo para o drive e plote o gráfico de linha no GLS comital arquivo.

public class geradorCSV {
    public static void main(String[] args) {
        // Configurações
        double minX = -5.0;
        double maxX = 5.0;
        double step = 0.1;
        String csvFileName = "fpg_data.csv";

        // Gera a função e salva os dados no arquivo CSV
        generateAndSaveSigmoideData(minX, maxX, step, csvFileName);
    }

    private static void generateAndSaveSigmoideData(double minX, double maxX, double step, String csvFileName) {
        try {
            // Criar um FileWriter para o arquivo CSV
            FileWriter fileWriter = new FileWriter(csvFileName);
            PrintWriter printWriter = new PrintWriter(fileWriter);

            // Formatar os números com ponto decimal substituído por vírgula
            DecimalFormat decimalFormat = new DecimalFormat("#.00");

            // Escreve o cabeçalho do CSV
            printWriter.println("x;f(x)");

            // Loop para calcular f(x) para cada valor de x e escrever no arquivo CSV
            for (double x = minX; x <= maxX; x += step) {
                // Calcula f(x)
                double fx = x + 2;

                // Escreve no arquivo CSV
                printWriter.printf("%.2f;%.2f%n", x, fx);
                printWriter.printf("%s;%s%n", decimalFormat.format(x).replace('.', ','), decimalFormat.format(fx).replace('.', ','));
            }

            printWriter.close();
            fileWriter.close();

            System.out.println("Arquivo CSV gerado com sucesso: " + csvFileName);
        } catch (IOException e) {
            System.err.println("Erro ao escrever no arquivo CSV: " + e.getMessage()); // ou e.printStackTrace()
        }
    }
}

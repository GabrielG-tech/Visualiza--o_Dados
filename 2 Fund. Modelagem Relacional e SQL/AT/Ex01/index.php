<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dicionário Web</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .custom-image {
            width: 20%;
            height: auto;
        }
    </style>
</head>
<body class="text-center">
    <div class="container">
        <img src="img_dicionario.png" class="img-fluid custom-image" alt="Logo Dicionário Web">
        <h1 class="mt-3">Dicionário Web</h1>
        <a href="inserir_resenha.php" class="btn btn-secondary mb-3">Inserir Nova Resenha</a>

        <!-- Formulário de Pesquisa -->
        <form action="index.php" method="post" class="mt-3">
            <div class="form-group">
                <input name="frase" type="text" id="frase" class="form-control" placeholder="Digite o nome do livro">
            </div>
            <button name="submit" type="submit" class="btn btn-primary">Pesquisar</button>
        </form>

        <?php
            $frase = isset($_POST['frase']) ? strtolower(trim($_POST['frase'])) : '';
            $conexao = mysqli_connect('localhost', 'id21579799_gabriel', 'P#Pato2003');
            mysqli_select_db($conexao, 'id21579799_dados');

            if ($frase) {
                $consulta = "SELECT * FROM registro WHERE LOWER(livro) LIKE '%$frase%'";
                $resultado = mysqli_query($conexao, $consulta);
                $campo = mysqli_fetch_array($resultado);

                if ($campo) {
                    echo "<br>";
                    echo "<table border=0>";
                    echo "<tr><td><strong>Livro:</strong></td><td>{$campo['livro']}</td></tr>";
                    echo "<tr><td><strong>Resenha:</strong></td><td>{$campo['resenha']}</td></tr>";
                    echo "<tr><td><strong>Contribuição:</strong></td><td>{$campo['resenhista']}</td></tr>";
                    echo "<tr><td><strong>E-mail:</strong></td><td>{$campo['email']}</td></tr>";
                    if ($campo['imagem']) {
                        $largura = 400;
                        $altura = 300;
                        echo '<img src="' . $campo['imagem'] . '" alt="' . $campo['livro'] . '" width="' . $largura . '" height="' . $altura . '">';
                    }
                    echo "</table>";
                } else {
                    echo '<p class="mt-3">Livro não encontrado. Adicione uma resenha <a href="inserir_resenha.php">aqui</a>.</p>';
                }
            }
        ?>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

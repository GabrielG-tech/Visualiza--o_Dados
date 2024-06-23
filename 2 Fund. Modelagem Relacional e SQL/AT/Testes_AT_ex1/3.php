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

        <!-- Formulário de Pesquisa -->
        <form action="index.php" method="post" class="mt-3">
            <div class="form-group">
                <input name="frase" type="text" id="frase" class="form-control" placeholder="Digite o nome do livro">
            </div>
            <button name="submit" type="submit" class="btn btn-primary">Pesquisar</button>
        </form>

        <?php
            // ini_set('display_errors', 'Off');
            // error_reporting(E_ALL & ~E_NOTICE & ~E_WARNING);
            $frase = strtolower(trim($_POST['frase']));
            $conexao = mysqli_connect('localhost', 'id21579799_gabriel', 'P#Pato2003');
            mysqli_select_db($conexao, 'id21579799_dados');

            if ($frase) {
                $consulta = "SELECT * FROM registro WHERE LOWER(livro) LIKE '%$frase%'";
                $resultado = mysqli_query($conexao, $consulta);
                $campo = mysqli_fetch_array($resultado);

                if ($campo[0]) {
                    echo "<br>";
                    echo "<table border=0>";
                    echo "<tr><td><strong>Livro:</strong></td><td>$campo[0]</td></tr>";
                    echo "<tr><td><strong>Resenha:</strong></td><td>$campo[1]</td></tr>";
                    echo "<tr><td><strong>Contribuição:</strong></td><td>$campo[2]</td></tr>";
                    echo "<tr><td><strong>E-mail:</strong></td><td>$campo[3]</td></tr>";
                    if ($campo[4]) {
                        $largura = 400;
                        $altura = 300;
                        echo '<img src="' . $campo[4] . '" alt="' . $campo[0] . '" width="' . $largura . '" height="' . $altura . '">';
                    }
                    echo "</table>";
                } else {
                    echo '<p class="mt-3">Livro não encontrado. Adicione uma resenha abaixo.</p>';
                }
            }
        ?>

        <!-- Formulário de Inserção -->
        <form action="index.php" method="post" class="mt-3">
            <h2>Inserir Nova Resenha</h2>
            <div class="form-group">
                <input name="novo_livro" type="text" class="form-control" placeholder="Nome do Livro" required>
            </div>
            <div class="form-group">
                <input name="nova_imagem" type="text" class="form-control" placeholder="URL da Imagem da Capa" required>
            </div>
            <div class="form-group">
                <textarea name="nova_resenha" class="form-control" placeholder="Resenha" required></textarea>
            </div>
            <div class="form-group">
                <input name="novo_resenhista" type="text" class="form-control" placeholder="Nome do Resenhista" required>
            </div>
            <div class="form-group">
                <input name="novo_email" type="email" class="form-control" placeholder="Email do Resenhista" required>
            </div>
            <button name="inserir" type="submit" class="btn btn-primary">Inserir Resenha</button>
        </form>

        <?php
            if (isset($_POST['inserir'])) {
                $novo_livro = trim($_POST['novo_livro']);
                $nova_imagem = trim($_POST['nova_imagem']);
                $nova_resenha = trim($_POST['nova_resenha']);
                $novo_resenhista = trim($_POST['novo_resenhista']);
                $novo_email = trim($_POST['novo_email']);

                if ($novo_livro && $nova_imagem && $nova_resenha && $novo_resenhista && $novo_email) {
                    $verifica = "SELECT * FROM registro WHERE LOWER(livro) = LOWER('$novo_livro')";
                    $resultado_verifica = mysqli_query($conexao, $verifica);

                    if (mysqli_num_rows($resultado_verifica) == 0) {
                        $inserir = "INSERT INTO registro (livro, resenha, resenhista, email, imagem) VALUES ('$novo_livro', '$nova_resenha', '$novo_resenhista', '$novo_email', '$nova_imagem')";
                        if (mysqli_query($conexao, $inserir)) {
                            echo '<p class="mt-3">Nova resenha inserida com sucesso!</p>';
                        } else {
                            echo '<p class="mt-3">Erro ao inserir a resenha: ' . mysqli_error($conexao) . '</p>';
                        }
                    } else {
                        echo '<p class="mt-3">Já existe uma resenha para este livro.</p>';
                    }
                } else {
                    echo '<p class="mt-3">Por favor, preencha todos os campos obrigatórios.</p>';
                }
            }
        ?>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>

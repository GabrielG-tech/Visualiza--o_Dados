<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dicionário Web</title>
        <!-- Bootstrap CSS -->
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <style>
            .custom-image {
                width: 40%;
                height: auto;
            }
        </style>
    </head>
     
    <body class="text-center">
        <div class="container">
            <img src="img_dicionario.png" class="img-fluid custom-image" alt="Logo Dicionário Web">
            
            <!-- Formulário de Pesquisa -->
            <form action="index.php" method="post" class="mt-3">
                <div class="form-group">
                    <input name="frase" type="text" id="frase" class="form-control" placeholder="Digite sua pesquisa">
                </div>
                <button name="submit" type="submit" class="btn btn-primary">Pesquisar</button>
            </form>
            
            <?php
                ini_set('display_errors', 'Off');
                error_reporting(E_ALL & ~E_NOTICE & ~E_WARNING);
                $frase = $_POST['frase'];
                $frase = strtolower($frase);
                $conexao = mysqli_connect('localhost', 'id21579799_gabriel', 'P#Pato2003');
                mysqli_select_db($conexao, 'id21579799_dados');
                $consulta = 'select * from registros where LOWER(livro) LIKE \'%' . strtolower($frase) . '%\';';
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
                    echo '<br> Registro não encontrado';
                }
            ?>
            
            <!-- Formulário de Inserção -->
            <form action="index.php" method="post" class="mt-3">
                <h2>Inserir Novo Livro</h2>
                <div class="form-group">
                    <input name="novo_livro" type="text" class="form-control" placeholder="Novo Livro">
                </div>
                <div class="form-group">
                    <textarea name="nova_resenha" class="form-control" placeholder="Resenha"></textarea>
                </div>
                <div class="form-group">
                    <input name="novo_resenhista" type="text" class="form-control" placeholder="Contribuição">
                </div>
                <div class="form-group">
                    <input name="novo_email" type="email" class="form-control" placeholder="E-mail">
                </div>
                <div class="form-group">
                    <input name="nova_imagem" type="text" class="form-control" placeholder="URL da Imagem (opcional)">
                </div>
                <button name="inserir" type="submit" class="btn btn-primary">Inserir</button>
            </form>

            <?php
                if ($_POST['inserir']) {
                    $novo_livro = $_POST['novo_livro'];
                    $nova_resenha = $_POST['nova_resenha'];
                    $novo_resenhista = $_POST['novo_resenhista'];
                    $novo_email = $_POST['novo_email'];
                    $nova_imagem = $_POST['nova_imagem'];

                    if ($novo_livro && $nova_resenha && $novo_resenhista && $novo_email) {
                        $inserir = "INSERT INTO registros (livro, resenha, resenhista, email, imagem) VALUES ('$novo_livro', '$nova_resenha', '$novo_resenhista', '$novo_email', '$nova_imagem')";
                        // (livro, resenha, resenhista, email, imagem)
                        if (mysqli_query($conexao, $inserir)) {
                            echo '<br> Novo registro inserido com sucesso';
                        } else {
                            echo '<br> Erro ao inserir o registro: ' . mysqli_error($conexao);
                        }
                    } else {
                        echo '<br> Por favor, preencha todos os campos obrigatórios';
                    }
                }
            ?>
            
            <button onclick="window.location.href='index.php'" class="btn btn-primary">Principal</button>
            
        </div>
        <!-- Bootstrap JS, Popper.js, and jQuery -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
</html>

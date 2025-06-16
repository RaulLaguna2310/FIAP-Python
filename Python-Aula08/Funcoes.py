# Funções
# Quebrar um problema complexo em pequenos problemas
# É critíco quebrar um código grande em partes menores, fáceis de serem entendidas e administradas;
# Permite o reaproveitamento de código, evitando a repetição;
# São estruturas que agrupam um conjunto de comandos que são executados quando a função é chamada;

# A estrutura de uma função é:
#     def nome_da_funcao(parametros):
#         bloco_de_codigo
#         return valor_de_retorno
# Parâmetros são variáveis que podem ser passadas para a função durante a chamada da função;
# O comando return retorna um valor da função para o invocador da função;

# Exmeplo:
#   def quadrado(x):
#       return x * x
    # A função quadrado recebe um parâmetro x e retorna o quadrado de x;

# Faz sentido para uma função não retornar nada, nesse caso o return é opcional;

# Função Main:
    # É comum criarmos uma função "main()" que executa os comando iniciais do programa;
    # O programa então conterá várias funções (incluindo a "main()") e um único comando que executa a função "main()";

# Parâmetros Default:
    # É possível definir uma função onde alguns parâmetros possuem valores padrão, e se não forem passados até a invocação da função, esse valor default será utilizado;
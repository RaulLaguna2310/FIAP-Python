# Operadores Lógicos: São utilizados para modificar valores booleanos, craindo expressões lógicas
# "and" ("e" lógico): verifica se os dois operadores possuem valor lógico -> True
# - V and V -> V; V and F -> F; F and V -> F; F and F -> F;

# - "or" ("ou" lógico): verifica se pelo menos um dos dois operadores possuem valor lógico -> True
# - V or V -> V; V or F -> V; F or V -> V; F or F -> F; 

# - "not" ("não" lógico): inverte o valor lógico do operando
# - not V -> F; not F -> V;

# Exercício 1:
# - Considerando -> a = True; b = False; c = True;
# - a and a -> true  |  a and b -> false  |  b or c -> true  |  c or c -> true 
# - a and b -> true  |  b and c -> false  |  c or a -> true  |  b or b -> false
# - not c -> false  |  a or c -> true  |  c = b -> true  |  not b -> true

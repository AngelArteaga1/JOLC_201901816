hola = "Hola Mundo!";
segundaVariable = "Comida";
terceraVaribale = 12;

println(10 ^ 5);
println("Comida" * "Pegamento");
println("PEPE" ^ 2);
println(!(true && false));
println('a');

println(hola * "pPEPE");
println(segundaVariable);
println(terceraVaribale);

popeye = 22.85+10;
println(trunc(popeye));
popeyito = 12+8;
println(float(popeyito+10));

println("Upper: ", uppercase("abcdEfgHijKlmnopQrstUvwxyz1234567890"));
println("Lower: ", lowercase("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"));

println(parse(Int64, "100.4")+100);
println(parse(Float64, "100.4")+0.6);
 
println("String de 1668: ",string(1568+100)*"pepe");
println("String de 1668.546: ",string(1568.546+100)*"pepe");
println(string('a') * " es la primera vocal");
println(string(!(true && false)) * " si soy");
println("'Comida' tiene: ", length("Comida"), " letras");

# Ahora viene la prueba que es algo recursiva
rec = 0;

function sumar(a::Int64, b::Int64)::Int64
    println("Entre a sumar");
    return a+b;
end;

retornable = sumar(sumar(10,10),sumar(20,20));
println(retornable);
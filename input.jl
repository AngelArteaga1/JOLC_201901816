
function factorial(num::Int64)::Int64
    println("num: ",num);
    if num == 1
        return 1;
    else
        numerito = num * factorial(num - 1);
        println("numerito: ", numerito);
        return numerito;
    end;
end;

println(factorial(5));
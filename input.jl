pepe = ["Lavanderia","Persona","3"];
println(pepe);
println(pepe[1]);
println(pepe[2]);
println(pepe[3]);
println("Ahora con un for");
for i in 1:length(pepe)
    println(pepe[i]);
end;

pepe[2] = "Angelito";
println(pepe);

#dimensional = [[1,2,3],[4,5,6],[7,8,9]];
#println(dimensional);

function swap(arreglo::Vector{String})
    temp = arreglo[3];
    arreglo[3] = arreglo[1];
    arreglo[1] = temp;
    println("Primera posicion: ", arreglo[1]);
end;

arreglito = ["uno","dos","tres"];
for i in arreglito
    println(i);
end;

swap(arreglito);
println(arreglito);

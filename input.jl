struct Persona
    nombre;
    edad;
end;

angel = Persona(["Angel", "Oswaldo", "Arteaga", "Garcia"], 20);
println(angel.nombre);
println(angel.edad);
println(string(angel) * "AHHH");

arreglo = [1, angel];
println(arreglo[1]);
println(arreglo[2]);
println(string(arreglo) * "AHHH");
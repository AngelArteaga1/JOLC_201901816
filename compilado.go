/*----HEADER----*/
package main;

import (
	"fmt";
)

var t0, t1, t2, t3, t4, t5, t6, t7 float64;
var P, H float64;
var stack [30101999]float64;
var heap [30101999]float64;



func main(){
	/* Compilacion de valor de variable */
	t0=H;
	heap[int(H)]=1;
	H=H+1;
	heap[int(H)]=2;
	H=H+1;
	heap[int(H)]=3;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t1=H;
	heap[int(H)]=4;
	H=H+1;
	heap[int(H)]=5;
	H=H+1;
	heap[int(H)]=6;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t2=H;
	heap[int(H)]=7;
	H=H+1;
	heap[int(H)]=8;
	H=H+1;
	heap[int(H)]=9;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t3=H;
	heap[int(H)]=t0;
	H=H+1;
	heap[int(H)]=t1;
	H=H+1;
	heap[int(H)]=t2;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	/* Fin de valor de variable */
	stack[int(0)]=t3;
	
	/* Compilacion de Acceso de Arreglo */
	/* Compilacion de Acceso */
	t4=stack[int(0)];
	/* Fin compilacion acceso */
	
	t5=t4;
	t6=1;
	t6=t6-1;
	t5=t5+t6;
	t7=heap[int(t5)];
	/* Fin de Compilacion de Acceso de Arreglo */
	fmt.Printf("%c", int(10));

}
/*----HEADER----*/
package main;

import (
	"fmt";
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25 float64;
var P, H float64;
var stack [30101999]float64;
var heap [30101999]float64;

/*-----NATIVES-----*/
func printString(){
	t1=P+1;
	t2=stack[int(t1)];
	L2:
	t3=heap[int(t2)];
	if t3 == -1 {goto L1;}
	fmt.Printf("%c", int(t3));
	t2=t2+1;
	goto L2;
	L1:
	return;
}

/*-----FUNCS-----*/
func factorial(){
	t0=H;
	heap[int(H)]=110;
	H=H+1;
	heap[int(H)]=117;
	H=H+1;
	heap[int(H)]=109;
	H=H+1;
	heap[int(H)]=58;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t4=P+2;
	t4=t4+1;
	stack[int(t4)]=t0;
	P=P+2;
	printString();
	t5=stack[int(P)];
	P=P-2;
	/* Compilacion de Acceso */
	t7=P+1;
	t6=stack[int(t7)];
	/* Fin compilacion acceso */
	
	fmt.Printf("%d", int(t6));
	fmt.Printf("%c", int(10));
	/* Compilacion de If */
	/* INICIO EXPRESION RELACIONAL */
	/* Compilacion de Acceso */
	t9=P+1;
	t8=stack[int(t9)];
	/* Fin compilacion acceso */
	
	if t8 == 1 {goto L3;}
	goto L4;
	/* FIN DE EXPRESION RELACIONAL */
	
	L3:
	stack[int(P)]=1;
	goto L0;
	goto L5;
	L4:
	/* Compilacion de valor de variable */
	/* Compilacion de Acceso */
	t11=P+1;
	t10=stack[int(t11)];
	/* Fin compilacion acceso */
	
	/* Compilacion de Acceso */
	t13=P+1;
	t12=stack[int(t13)];
	/* Fin compilacion acceso */
	
	t14=t12-1;
	t15=P+3;
	stack[int(t15)]=t14;
	P=P+2;
	factorial();
	t15=stack[int(P)];
	P=P-2;
	t16=t10*t15;
	/* Fin de valor de variable */
	t17=P+2;
	stack[int(t17)]=t16;
	
	t18=H;
	heap[int(H)]=110;
	H=H+1;
	heap[int(H)]=117;
	H=H+1;
	heap[int(H)]=109;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=105;
	H=H+1;
	heap[int(H)]=116;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=58;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t19=P+3;
	t19=t19+1;
	stack[int(t19)]=t18;
	P=P+3;
	printString();
	t20=stack[int(P)];
	P=P-3;
	/* Compilacion de Acceso */
	t22=P+2;
	t21=stack[int(t22)];
	/* Fin compilacion acceso */
	
	fmt.Printf("%d", int(t21));
	fmt.Printf("%c", int(10));
	/* Compilacion de Acceso */
	t24=P+2;
	t23=stack[int(t24)];
	/* Fin compilacion acceso */
	
	stack[int(P)]=t23;
	goto L0;
	L5:
	goto L0;
	L0:
	return;
}

func main(){
	t25=P+1;
	stack[int(t25)]=5;
	P=P+0;
	factorial();
	t25=stack[int(P)];
	P=P-0;
	fmt.Printf("%d", int(t25));
	fmt.Printf("%c", int(10));

}
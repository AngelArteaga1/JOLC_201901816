/*----HEADER----*/
package main;

import (
	"fmt";
	"math";
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39, t40, t41, t42, t43, t44, t45, t46, t47, t48, t49, t50, t51, t52, t53, t54, t55, t56, t57, t58, t59, t60, t61, t62, t63, t64, t65, t66, t67, t68, t69, t70, t71, t72, t73, t74, t75, t76, t77, t78, t79, t80, t81, t82, t83, t84, t85, t86, t87, t88, t89, t90, t91, t92, t93, t94, t95, t96, t97, t98, t99, t100, t101, t102, t103, t104, t105, t106, t107, t108, t109, t110, t111, t112, t113, t114, t115, t116, t117, t118, t119, t120, t121, t122, t123, t124, t125, t126, t127, t128, t129, t130, t131, t132, t133, t134, t135, t136, t137, t138, t139, t140, t141, t142, t143, t144, t145, t146, t147, t148, t149, t150, t151, t152, t153, t154, t155, t156, t157, t158, t159, t160, t161, t162, t163, t164, t165, t166, t167, t168, t169, t170, t171, t172, t173, t174, t175, t176, t177, t178, t179 float64;
var P, H float64;
var stack [30101999]float64;
var heap [30101999]float64;

/*-----NATIVES-----*/
func potencia(){
	t3=P+1;
	t4=stack[int(t3)];
	t3=t3+1;
	t5=stack[int(t3)];
	if t5 <= 0 {goto L1;}
	t3=t4;
	L2:
	if t5 <= 1 {goto L3;}
	t4=t4*t3;
	t5=t5-1;
	goto L2;
	L1:
	stack[int(P)]=1;
	goto L0;
	L3:
	stack[int(P)]=t4;
	L0:
	return;
}
func concatenar(){
	t11=H;
	t12=P+1;
	t13=stack[int(t12)];
	L5:
	t14=heap[int(t13)];
	if t14 == -1 {goto L6;}
	heap[int(H)]=t14;
	H=H+1;
	t13=t13+1;
	goto L5;
	L6:
	t12=P+2;
	t13=stack[int(t12)];
	L7:
	t14=heap[int(t13)];
	if t14 == -1 {goto L4;}
	heap[int(H)]=t14;
	H=H+1;
	t13=t13+1;
	goto L7;
	L4:
	heap[int(H)]=-1;
	H=H+1;
	stack[int(P)]=t11;
	return;
}
func printString(){
	t17=P+1;
	t18=stack[int(t17)];
	L9:
	t19=heap[int(t18)];
	if t19 == -1 {goto L8;}
	fmt.Printf("%c", int(t19));
	t18=t18+1;
	goto L9;
	L8:
	return;
}
func potenciaLeft(){
	t24=H;
	t25=P+1;
	t27=P+2;
	t28=stack[int(t27)];
	L13:
	t26=stack[int(t25)];
	L11:
	t29=heap[int(t26)];
	if t29 == -1 {goto L12;}
	heap[int(H)]=t29;
	H=H+1;
	t26=t26+1;
	goto L11;
	L12:
	if t28 <= 1 {goto L10;}
	t28=t28-1;
	goto L13;
	L10:
	heap[int(H)]=-1;
	H=H+1;
	stack[int(P)]=t24;
	return;
}
func uppercase(){
	t58=H;
	t56=P+1;
	t57=stack[int(t56)];
	L19:
	t59=heap[int(t57)];
	if t59 == -1 {goto L18;}
	if t59 < 97 {goto L20;}
	if t59 > 122 {goto L20;}
	t59=t59-32;
	L20:
	heap[int(H)]=t59;
	H=H+1;
	t57=t57+1;
	goto L19;
	L18:
	heap[int(H)]=-1;
	H=H+1;
	stack[int(P)]=t58;
	return;
}
func lowercase(){
	t70=H;
	t68=P+1;
	t69=stack[int(t68)];
	L22:
	t71=heap[int(t69)];
	if t71 == -1 {goto L21;}
	if t71 < 65 {goto L23;}
	if t71 > 90 {goto L23;}
	t71=t71+32;
	L23:
	heap[int(H)]=t71;
	H=H+1;
	t69=t69+1;
	goto L22;
	L21:
	heap[int(H)]=-1;
	H=H+1;
	stack[int(P)]=t70;
	return;
}
func parseToInt(){
	t79=1;
	t80=0;
	t77=P+1;
	t78=stack[int(t77)];
	L25:
	t81=heap[int(t78)];
	if t81 == 46 {goto L26;}
	if t81 == -1 {goto L26;}
	if t81 < 48 {goto L24;}
	if t81 > 57 {goto L24;}
	t79=t79*10;
	t78=t78+1;
	goto L25;
	L26:
	t79=t79/10;
	t77=P+1;
	t78=stack[int(t77)];
	L27:
	t81=heap[int(t78)];
	if t81 == 46 {goto L24;}
	if t81 == -1 {goto L24;}
	t81=t81-48;
	t82=t81*t79;
	t80=t80+t82;
	t79=t79/10;
	t78=t78+1;
	goto L27;
	L24:
	stack[int(P)]=t80;
	return;
}
func parseToFloat(){
	t89=1;
	t90=1;
	t91=0;
	t87=P+1;
	t88=stack[int(t87)];
	L29:
	t92=heap[int(t88)];
	if t92 == 46 {goto L30;}
	if t92 == -1 {goto L30;}
	if t92 < 48 {goto L28;}
	if t92 > 57 {goto L28;}
	t89=t89*10;
	t88=t88+1;
	goto L29;
	L30:
	t89=t89/10;
	t87=P+1;
	t88=stack[int(t87)];
	L32:
	t92=heap[int(t88)];
	if t92 == 46 {goto L31;}
	if t92 == -1 {goto L28;}
	t92=t92-48;
	t93=t92*t89;
	t91=t91+t93;
	t89=t89/10;
	t88=t88+1;
	goto L32;
	L31:
	t88=t88+1;
	L33:
	t92=heap[int(t88)];
	if t92 == -1 {goto L28;}
	t90=t90/10;
	t92=t92-48;
	t94=t92*t90;
	t91=t91+t94;
	t88=t88+1;
	goto L33;
	L28:
	stack[int(P)]=t91;
	return;
}
func intToString(){
	t102=P+1;
	t103=stack[int(t102)];
	t104=stack[int(t102)];
	t105=stack[int(t102)];
	t106=0;
	t107=1;
	L35:
	if t104 < 1 {goto L37;}
	t107=t107*10;
	t104=t104/10;
	goto L35;
	L37:
	t107=t107/10;
	t108=H;
	L36:
	if t107 < 1 {goto L34;}
	t105=t103/t107;
	t106=t105+48;
	heap[int(H)]=t106;
	H=H+1;
	t103=math.Mod(t103,t107);
	t107=t107/10;
	goto L36;
	L34:
	heap[int(H)]=-1;
	H=H+1;
	stack[int(P)]=t108;
	return;
}
func floatToString(){
	t121=P+1;
	t122=stack[int(t121)];
	t123=stack[int(t121)];
	t124=stack[int(t121)];
	t125=0;
	t126=1;
	L39:
	if t123 < 1 {goto L42;}
	t126=t126*10;
	t123=t123/10;
	goto L39;
	L42:
	t126=t126/10;
	t127=H;
	L40:
	if t126 < 1 {goto L43;}
	t124=t122/t126;
	t125=t124+48;
	heap[int(H)]=t125;
	H=H+1;
	t122=math.Mod(t122,t126);
	t126=t126/10;
	goto L40;
	L43:
	heap[int(H)]=46;
	H=H+1;
	t123=0;
	L41:
	if t123 >= 8 {goto L38;}
	if t122 == 0 {goto L38;}
	t122=t122*10;
	t125=t122+48;
	heap[int(H)]=t125;
	H=H+1;
	t122=math.Mod(t122,1);
	t123=t123+1;
	goto L41;
	L38:
	heap[int(H)]=-1;
	H=H+1;
	stack[int(P)]=t127;
	return;
}
func charToString(){
	t136=P+1;
	t137=stack[int(t136)];
	t138=H;
	t139=H;
	heap[int(t138)]=t137;
	H=H+1;
	t138=t138+1;
	heap[int(t138)]=-1;
	H=H+1;
	stack[int(P)]=t139;
	return;
}
func length(){
	t159=P+1;
	t160=stack[int(t159)];
	t161=0;
	L49:
	t162=heap[int(t160)];
	if t162 == -1 {goto L48;}
	t161=t161+1;
	t160=t160+1;
	goto L49;
	L48:
	stack[int(P)]=t161;
	return;
}

/*-----FUNCS-----*/
func sumar(){
	t168=H;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=110;
	H=H+1;
	heap[int(H)]=116;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=115;
	H=H+1;
	heap[int(H)]=117;
	H=H+1;
	heap[int(H)]=109;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t169=P+3;
	t169=t169+1;
	stack[int(t169)]=t168;
	P=P+3;
	printString();
	t170=stack[int(P)];
	P=P-3;
	fmt.Printf("%c", int(10));
	/* Compilacion de Acceso */
	t172=P+1;
	t171=stack[int(t172)];
	/* Fin compilacion acceso */
	
	/* Compilacion de Acceso */
	t174=P+2;
	t173=stack[int(t174)];
	/* Fin compilacion acceso */
	
	t175=t171+t173;
	stack[int(P)]=t175;
	goto L50;
	goto L50;
	L50:
	return;
}

func main(){
	/* Compilacion de valor de variable */
	t0=H;
	heap[int(H)]=72;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=108;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=77;
	H=H+1;
	heap[int(H)]=117;
	H=H+1;
	heap[int(H)]=110;
	H=H+1;
	heap[int(H)]=100;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=33;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	/* Fin de valor de variable */
	stack[int(0)]=t0;
	
	/* Compilacion de valor de variable */
	t1=H;
	heap[int(H)]=67;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=109;
	H=H+1;
	heap[int(H)]=105;
	H=H+1;
	heap[int(H)]=100;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	/* Fin de valor de variable */
	stack[int(1)]=t1;
	
	/* Compilacion de valor de variable */
	/* Fin de valor de variable */
	stack[int(2)]=12;
	
	t6=P+3;
	t6=t6+1;
	stack[int(t6)]=10;
	t6=t6+1;
	stack[int(t6)]=5;
	P=P+3;
	potencia();
	t7=stack[int(P)];
	P=P-3;
	fmt.Printf("%d", int(t7));
	fmt.Printf("%c", int(10));
	t8=H;
	heap[int(H)]=67;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=109;
	H=H+1;
	heap[int(H)]=105;
	H=H+1;
	heap[int(H)]=100;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t9=H;
	heap[int(H)]=80;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=103;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=109;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=110;
	H=H+1;
	heap[int(H)]=116;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t15=P+3;
	t15=t15+1;
	stack[int(t15)]=t8;
	t15=t15+1;
	stack[int(t15)]=t9;
	P=P+3;
	concatenar();
	t16=stack[int(P)];
	P=P-3;
	t20=P+3;
	t20=t20+1;
	stack[int(t20)]=t16;
	P=P+3;
	printString();
	t21=stack[int(P)];
	P=P-3;
	fmt.Printf("%c", int(10));
	t22=H;
	heap[int(H)]=80;
	H=H+1;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=80;
	H=H+1;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t30=P+3;
	t30=t30+1;
	stack[int(t30)]=t22;
	t30=t30+1;
	stack[int(t30)]=2;
	P=P+3;
	potenciaLeft();
	t31=stack[int(P)];
	P=P-3;
	t32=P+3;
	t32=t32+1;
	stack[int(t32)]=t31;
	P=P+3;
	printString();
	t33=stack[int(P)];
	P=P-3;
	fmt.Printf("%c", int(10));
	/* INICIO EXPRESION LOGICA */
	/* INICIO EXPRESION LOGICA */
	goto L16;
	/* GOTO PARA EVITAR ERROR DE GO */
	goto L14;
	L16:
	goto L14;
	/* GOTO PARA EVITAR ERROR DE GO */
	goto L15;
	/* FINALIZO EXPRESION LOGICA */
	
	/* FINALIZO EXPRESION LOGICA */
	
	L14:
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(101));
	goto L17;
	L15:
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(108));
	fmt.Printf("%c", int(115));
	fmt.Printf("%c", int(101));
	L17:
	fmt.Printf("%c", int(10));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(10));
	/* Compilacion de Acceso */
	t34=stack[int(0)];
	/* Fin compilacion acceso */
	
	t35=H;
	heap[int(H)]=112;
	H=H+1;
	heap[int(H)]=80;
	H=H+1;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=80;
	H=H+1;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t37=P+3;
	t37=t37+1;
	stack[int(t37)]=t34;
	t37=t37+1;
	stack[int(t37)]=t35;
	P=P+3;
	concatenar();
	t38=stack[int(P)];
	P=P-3;
	t39=P+3;
	t39=t39+1;
	stack[int(t39)]=t38;
	P=P+3;
	printString();
	t40=stack[int(P)];
	P=P-3;
	fmt.Printf("%c", int(10));
	/* Compilacion de Acceso */
	t41=stack[int(1)];
	/* Fin compilacion acceso */
	
	t42=P+3;
	t42=t42+1;
	stack[int(t42)]=t41;
	P=P+3;
	printString();
	t43=stack[int(P)];
	P=P-3;
	fmt.Printf("%c", int(10));
	/* Compilacion de Acceso */
	t44=stack[int(2)];
	/* Fin compilacion acceso */
	
	fmt.Printf("%d", int(t44));
	fmt.Printf("%c", int(10));
	/* Compilacion de valor de variable */
	t45=22.85+10;
	/* Fin de valor de variable */
	stack[int(3)]=t45;
	
	/* Compilacion de Acceso */
	t46=stack[int(3)];
	/* Fin compilacion acceso */
	
	t47=t46;
	fmt.Printf("%d", int(t47));
	fmt.Printf("%c", int(10));
	/* Compilacion de valor de variable */
	t48=12+8;
	/* Fin de valor de variable */
	stack[int(4)]=t48;
	
	/* Compilacion de Acceso */
	t49=stack[int(4)];
	/* Fin compilacion acceso */
	
	t50=t49+10;
	t51=t50+0.0;
	fmt.Printf("%f", t51);
	fmt.Printf("%c", int(10));
	t52=H;
	heap[int(H)]=85;
	H=H+1;
	heap[int(H)]=112;
	H=H+1;
	heap[int(H)]=112;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=58;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t53=P+5;
	t53=t53+1;
	stack[int(t53)]=t52;
	P=P+5;
	printString();
	t54=stack[int(P)];
	P=P-5;
	t55=H;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=98;
	H=H+1;
	heap[int(H)]=99;
	H=H+1;
	heap[int(H)]=100;
	H=H+1;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=102;
	H=H+1;
	heap[int(H)]=103;
	H=H+1;
	heap[int(H)]=72;
	H=H+1;
	heap[int(H)]=105;
	H=H+1;
	heap[int(H)]=106;
	H=H+1;
	heap[int(H)]=75;
	H=H+1;
	heap[int(H)]=108;
	H=H+1;
	heap[int(H)]=109;
	H=H+1;
	heap[int(H)]=110;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=112;
	H=H+1;
	heap[int(H)]=81;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=115;
	H=H+1;
	heap[int(H)]=116;
	H=H+1;
	heap[int(H)]=85;
	H=H+1;
	heap[int(H)]=118;
	H=H+1;
	heap[int(H)]=119;
	H=H+1;
	heap[int(H)]=120;
	H=H+1;
	heap[int(H)]=121;
	H=H+1;
	heap[int(H)]=122;
	H=H+1;
	heap[int(H)]=49;
	H=H+1;
	heap[int(H)]=50;
	H=H+1;
	heap[int(H)]=51;
	H=H+1;
	heap[int(H)]=52;
	H=H+1;
	heap[int(H)]=53;
	H=H+1;
	heap[int(H)]=54;
	H=H+1;
	heap[int(H)]=55;
	H=H+1;
	heap[int(H)]=56;
	H=H+1;
	heap[int(H)]=57;
	H=H+1;
	heap[int(H)]=48;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t60=P+5;
	t60=t60+1;
	stack[int(t60)]=t55;
	P=P+5;
	uppercase();
	t61=stack[int(P)];
	P=P-5;
	t62=P+5;
	t62=t62+1;
	stack[int(t62)]=t61;
	P=P+5;
	printString();
	t63=stack[int(P)];
	P=P-5;
	fmt.Printf("%c", int(10));
	t64=H;
	heap[int(H)]=76;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=119;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=58;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t65=P+5;
	t65=t65+1;
	stack[int(t65)]=t64;
	P=P+5;
	printString();
	t66=stack[int(P)];
	P=P-5;
	t67=H;
	heap[int(H)]=65;
	H=H+1;
	heap[int(H)]=66;
	H=H+1;
	heap[int(H)]=67;
	H=H+1;
	heap[int(H)]=68;
	H=H+1;
	heap[int(H)]=69;
	H=H+1;
	heap[int(H)]=70;
	H=H+1;
	heap[int(H)]=71;
	H=H+1;
	heap[int(H)]=72;
	H=H+1;
	heap[int(H)]=73;
	H=H+1;
	heap[int(H)]=74;
	H=H+1;
	heap[int(H)]=75;
	H=H+1;
	heap[int(H)]=76;
	H=H+1;
	heap[int(H)]=77;
	H=H+1;
	heap[int(H)]=78;
	H=H+1;
	heap[int(H)]=79;
	H=H+1;
	heap[int(H)]=80;
	H=H+1;
	heap[int(H)]=81;
	H=H+1;
	heap[int(H)]=82;
	H=H+1;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=84;
	H=H+1;
	heap[int(H)]=85;
	H=H+1;
	heap[int(H)]=86;
	H=H+1;
	heap[int(H)]=87;
	H=H+1;
	heap[int(H)]=88;
	H=H+1;
	heap[int(H)]=89;
	H=H+1;
	heap[int(H)]=90;
	H=H+1;
	heap[int(H)]=49;
	H=H+1;
	heap[int(H)]=50;
	H=H+1;
	heap[int(H)]=51;
	H=H+1;
	heap[int(H)]=52;
	H=H+1;
	heap[int(H)]=53;
	H=H+1;
	heap[int(H)]=54;
	H=H+1;
	heap[int(H)]=55;
	H=H+1;
	heap[int(H)]=56;
	H=H+1;
	heap[int(H)]=57;
	H=H+1;
	heap[int(H)]=48;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t72=P+5;
	t72=t72+1;
	stack[int(t72)]=t67;
	P=P+5;
	lowercase();
	t73=stack[int(P)];
	P=P-5;
	t74=P+5;
	t74=t74+1;
	stack[int(t74)]=t73;
	P=P+5;
	printString();
	t75=stack[int(P)];
	P=P-5;
	fmt.Printf("%c", int(10));
	t76=H;
	heap[int(H)]=49;
	H=H+1;
	heap[int(H)]=48;
	H=H+1;
	heap[int(H)]=48;
	H=H+1;
	heap[int(H)]=46;
	H=H+1;
	heap[int(H)]=52;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t83=P+5;
	t83=t83+1;
	stack[int(t83)]=t76;
	P=P+5;
	parseToInt();
	t84=stack[int(P)];
	P=P-5;
	t85=t84+100;
	fmt.Printf("%d", int(t85));
	fmt.Printf("%c", int(10));
	t86=H;
	heap[int(H)]=49;
	H=H+1;
	heap[int(H)]=48;
	H=H+1;
	heap[int(H)]=48;
	H=H+1;
	heap[int(H)]=46;
	H=H+1;
	heap[int(H)]=52;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t95=P+5;
	t95=t95+1;
	stack[int(t95)]=t86;
	P=P+5;
	parseToFloat();
	t96=stack[int(P)];
	P=P-5;
	t97=t96+0.6;
	fmt.Printf("%f", t97);
	fmt.Printf("%c", int(10));
	t98=H;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=116;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=105;
	H=H+1;
	heap[int(H)]=110;
	H=H+1;
	heap[int(H)]=103;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=100;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=49;
	H=H+1;
	heap[int(H)]=54;
	H=H+1;
	heap[int(H)]=54;
	H=H+1;
	heap[int(H)]=56;
	H=H+1;
	heap[int(H)]=58;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t99=P+5;
	t99=t99+1;
	stack[int(t99)]=t98;
	P=P+5;
	printString();
	t100=stack[int(P)];
	P=P-5;
	t101=1568+100;
	t109=P+5;
	t109=t109+1;
	stack[int(t109)]=t101;
	P=P+5;
	intToString();
	t110=stack[int(P)];
	P=P-5;
	t111=H;
	heap[int(H)]=112;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=112;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t113=P+5;
	t113=t113+1;
	stack[int(t113)]=t110;
	t113=t113+1;
	stack[int(t113)]=t111;
	P=P+5;
	concatenar();
	t114=stack[int(P)];
	P=P-5;
	t115=P+5;
	t115=t115+1;
	stack[int(t115)]=t114;
	P=P+5;
	printString();
	t116=stack[int(P)];
	P=P-5;
	fmt.Printf("%c", int(10));
	t117=H;
	heap[int(H)]=83;
	H=H+1;
	heap[int(H)]=116;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=105;
	H=H+1;
	heap[int(H)]=110;
	H=H+1;
	heap[int(H)]=103;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=100;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=49;
	H=H+1;
	heap[int(H)]=54;
	H=H+1;
	heap[int(H)]=54;
	H=H+1;
	heap[int(H)]=56;
	H=H+1;
	heap[int(H)]=46;
	H=H+1;
	heap[int(H)]=53;
	H=H+1;
	heap[int(H)]=52;
	H=H+1;
	heap[int(H)]=54;
	H=H+1;
	heap[int(H)]=58;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t118=P+5;
	t118=t118+1;
	stack[int(t118)]=t117;
	P=P+5;
	printString();
	t119=stack[int(P)];
	P=P-5;
	t120=1568.546+100;
	t128=P+5;
	t128=t128+1;
	stack[int(t128)]=t120;
	P=P+5;
	floatToString();
	t129=stack[int(P)];
	P=P-5;
	t130=H;
	heap[int(H)]=112;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=112;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t132=P+5;
	t132=t132+1;
	stack[int(t132)]=t129;
	t132=t132+1;
	stack[int(t132)]=t130;
	P=P+5;
	concatenar();
	t133=stack[int(P)];
	P=P-5;
	t134=P+5;
	t134=t134+1;
	stack[int(t134)]=t133;
	P=P+5;
	printString();
	t135=stack[int(P)];
	P=P-5;
	fmt.Printf("%c", int(10));
	t140=P+5;
	t140=t140+1;
	stack[int(t140)]=97;
	P=P+5;
	charToString();
	t141=stack[int(P)];
	P=P-5;
	t142=H;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=115;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=108;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=112;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=105;
	H=H+1;
	heap[int(H)]=109;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=118;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=99;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=108;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t144=P+5;
	t144=t144+1;
	stack[int(t144)]=t141;
	t144=t144+1;
	stack[int(t144)]=t142;
	P=P+5;
	concatenar();
	t145=stack[int(P)];
	P=P-5;
	t146=P+5;
	t146=t146+1;
	stack[int(t146)]=t145;
	P=P+5;
	printString();
	t147=stack[int(P)];
	P=P-5;
	fmt.Printf("%c", int(10));
	/* INICIO EXPRESION LOGICA */
	/* INICIO EXPRESION LOGICA */
	goto L46;
	/* GOTO PARA EVITAR ERROR DE GO */
	goto L44;
	L46:
	goto L44;
	/* GOTO PARA EVITAR ERROR DE GO */
	goto L45;
	/* FINALIZO EXPRESION LOGICA */
	
	/* FINALIZO EXPRESION LOGICA */
	
	L44:
	t148=H;
	heap[int(H)]=116;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=117;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	goto L47;
	L45:
	t148=H;
	heap[int(H)]=102;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=108;
	H=H+1;
	heap[int(H)]=115;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	L47:
	t149=H;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=115;
	H=H+1;
	heap[int(H)]=105;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=115;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=121;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t151=P+5;
	t151=t151+1;
	stack[int(t151)]=t148;
	t151=t151+1;
	stack[int(t151)]=t149;
	P=P+5;
	concatenar();
	t152=stack[int(P)];
	P=P-5;
	t153=P+5;
	t153=t153+1;
	stack[int(t153)]=t152;
	P=P+5;
	printString();
	t154=stack[int(P)];
	P=P-5;
	fmt.Printf("%c", int(10));
	t155=H;
	heap[int(H)]=39;
	H=H+1;
	heap[int(H)]=67;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=109;
	H=H+1;
	heap[int(H)]=105;
	H=H+1;
	heap[int(H)]=100;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=39;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=116;
	H=H+1;
	heap[int(H)]=105;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=110;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=58;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t156=P+5;
	t156=t156+1;
	stack[int(t156)]=t155;
	P=P+5;
	printString();
	t157=stack[int(P)];
	P=P-5;
	t158=H;
	heap[int(H)]=67;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=109;
	H=H+1;
	heap[int(H)]=105;
	H=H+1;
	heap[int(H)]=100;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t163=P+5;
	t163=t163+1;
	stack[int(t163)]=t158;
	P=P+5;
	length();
	t164=stack[int(P)];
	P=P-5;
	fmt.Printf("%d", int(t164));
	t165=H;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=108;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=116;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=115;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t166=P+5;
	t166=t166+1;
	stack[int(t166)]=t165;
	P=P+5;
	printString();
	t167=stack[int(P)];
	P=P-5;
	fmt.Printf("%c", int(10));
	/* Compilacion de valor de variable */
	/* Fin de valor de variable */
	stack[int(5)]=0;
	
	/* Compilacion de valor de variable */
	t176=P+7;
	stack[int(t176)]=10;
	t176=t176+1;
	stack[int(t176)]=10;
	P=P+6;
	sumar();
	t176=stack[int(P)];
	P=P-6;
	t177=P+7;
	stack[int(t177)]=20;
	t177=t177+1;
	stack[int(t177)]=20;
	P=P+6;
	sumar();
	t177=stack[int(P)];
	P=P-6;
	t178=P+7;
	stack[int(t178)]=t176;
	t178=t178+1;
	stack[int(t178)]=t177;
	P=P+6;
	sumar();
	t178=stack[int(P)];
	P=P-6;
	/* Fin de valor de variable */
	stack[int(6)]=t178;
	
	/* Compilacion de Acceso */
	t179=stack[int(6)];
	/* Fin compilacion acceso */
	
	fmt.Printf("%d", int(t179));
	fmt.Printf("%c", int(10));

}
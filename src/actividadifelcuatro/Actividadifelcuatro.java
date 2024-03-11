
package actividadifelcuatro;

import java.util.Scanner;


public class Actividadifelcuatro {

    /*2. Un postulante a un empleo, realiza un test de capacitación, se obtuvo la
siguiente información: cantidad total de preguntas que se le realizaron y
la cantidad de preguntas que contestó correctamente. Se pide
confeccionar un programa que ingrese los dos datos por teclado e informe
el nivel del mismo según el porcentaje de respuestas correctas que ha
obtenido, y sabiendo que: Nivel máximo: Porcentaje>=90%. Nivel
medio: Porcentaje>=75% y <90%. Nivel regular:
Porcentaje>=50% y <75%. Fuera de nivel:
Porcentaje<50%.*/
    
    public static void main(String[] args) {
       
        int a, b, k;
        
         Scanner ca= new Scanner(System.in);
         Scanner cb= new Scanner(System.in);
         
         System.out.print("ingrese la cantidad de preguntas total:");
         a = ca.nextInt();
         
         System.out.print("ingrese la cantidad de respuestas bien respondidas:");
        
         b = cb.nextInt();
        
         k = (b/a)*100;
         
         System.out.println("el porcentaje es:"+ k);
         
         
    }
    
}

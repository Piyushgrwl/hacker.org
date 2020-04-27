/*    */ public class Privy {
/*    */   public void showMeSomethingBoring() {
/*  4 */     System.out.println("this is not interesting. look elsewhere.");
/*    */   }
/*    */   
/*    */   private void showMeSomethingInteresting() {
/*  7 */     char[] c = { 'a', 'x', 'k', 'y', 'u', 'e' };
/*  8 */     int a = 73, b = 391;
/*  9 */     String s = "";
/* 10 */     for (int i = 0; i < 6; i++)
/* 11 */       s = String.valueOf(s) + c[(i * b + (i + 8) * a) % c.length]; 
/* 12 */     System.out.println(s);
/*    */   }
/*    */   
/*    */   public static void main(String[] args) {
/* 15 */     (new Privy()).showMeSomethingBoring();
/*    */   }
/*    */ }


/* Location:              C:\Users\piyuagar\Downloads\!\Privy.class
 * Java compiler version: 5 (49.0)
 * JD-Core Version:       1.1.3
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int son;
int q=0, u=0;
int w=1;
int ar[9][9]={
  {3, 5, 0, 0, 2, 0, 8, 0, 0},
  {0, 0, 0, 5, 0, 6, 0, 0, 7},
  {0, 0, 0, 0, 9, 4, 0, 0, 0},
  {9, 0, 3, 0, 0, 0, 6, 0, 4},
  {0, 0, 0, 0, 0, 0, 7, 9, 0},
  {1, 8, 0, 0, 0, 0, 0, 3, 2},
  {0, 0, 0, 8, 0, 0, 0, 0, 0},
  {0, 7, 0, 0, 0, 5, 0, 0, 0},
  {0, 0, 0, 0, 0, 1, 0, 2, 3},
};

bool gameOver();

void karta();

void qirit();

void hato();

void kiritsh2();




int main()
{
system("cls");
  while(0!=gameOver(w)){
    karta();
    qirit();
    hato();
  }

  return 0;
}





bool gameOver(int w){
  if(w==1)
    return true;
  
  else
    return false;
}


void karta(){
 system("cls");
 system ("color 3");
	printf("    1   2   3   4   5   6   7   8   9\n");
	printf("  \e[31m_____________________________________\e[36m\n1 \e[31m|\e[36m \e[33m%d\e[36m | \e[33m%d\e[36m | \e[32m%d\e[31m | \e[32m%d\e[36m | \e[33m%d\e[36m | \e[32m%d\e[31m | \e[33m%d\e[36m | \e[32m%d\e[36m | \e[32m%d\e[36m \e[31m|\e[36m\n", ar[0][0], ar[0][1], ar[0][2], ar[0][3], ar[0][4], ar[0][5], ar[0][6], ar[0][7], ar[0][8]);
	printf("  \e[31m|\e[36m___|___|___\e[31m|\e[36m___|___|___\e[31m|\e[36m___|___|___\e[31m|\e[36m\n2 \e[31m|\e[36m \e[32m%d\e[36m | \e[32m%d\e[36m | \e[32m%d\e[31m | \e[33m%d\e[36m | \e[32m%d\e[36m | \e[33m%d\e[31m | \e[32m%d\e[36m | \e[32m%d\e[36m | \e[33m%d\e[36m \e[31m|\e[36m\n", ar[1][0], ar[1][1], ar[1][2], ar[1][3], ar[1][4], ar[1][5], ar[1][6], ar[1][7], ar[1][8]);
	printf("  \e[31m|\e[36m___|___|___\e[31m|\e[36m___|___|___\e[31m|\e[36m___|___|___\e[31m|\e[36m\n3 \e[31m|\e[36m \e[32m%d\e[36m | \e[32m%d\e[36m | \e[32m%d\e[31m | \e[32m%d\e[36m | \e[33m%d\e[36m | \e[33m%d\e[31m | \e[32m%d\e[36m | \e[32m%d\e[36m | \e[32m%d\e[36m \e[31m|\e[36m\n", ar[2][0], ar[2][1], ar[2][2], ar[2][3], ar[2][4], ar[2][5], ar[2][6], ar[2][7], ar[2][8]);
	printf("  \e[31m|\e[36m\e[31m___\e[36m|\e[31m___\e[36m|\e[31m___\e[36m\e[31m|\e[36m\e[31m___\e[36m|\e[31m___\e[36m|\e[31m___\e[36m\e[31m|\e[36m\e[31m___\e[36m|\e[31m___\e[36m|\e[31m___\e[36m\e[31m|\e[36m\n4 \e[31m|\e[36m \e[33m%d\e[36m | \e[32m%d\e[36m | \e[33m%d\e[31m | \e[32m%d\e[36m | \e[32m%d\e[36m | \e[32m%d\e[31m | \e[33m%d\e[36m | \e[32m%d\e[36m | \e[33m%d\e[36m \e[31m|\e[36m\n", ar[3][0], ar[3][1], ar[3][2], ar[3][3], ar[3][4], ar[3][5], ar[3][6], ar[3][7], ar[3][8]);
	printf("  \e[31m|\e[36m___|___|___\e[31m|\e[36m___|___|___\e[31m|\e[36m___|___|___\e[31m|\e[36m\n5 \e[31m|\e[36m \e[32m%d\e[36m | \e[32m%d\e[36m | \e[32m%d\e[31m | \e[32m%d\e[36m | \e[32m%d\e[36m | \e[32m%d\e[31m | \e[33m%d\e[36m | \e[33m%d\e[36m | \e[32m%d\e[36m \e[31m|\e[36m\n", ar[4][0], ar[4][1], ar[4][2], ar[4][3], ar[4][4], ar[4][5], ar[4][6], ar[4][7], ar[4][8]);
	printf("  \e[31m|\e[36m___|___|___\e[31m|\e[36m___|___|___\e[31m|\e[36m___|___|___\e[31m|\e[36m\n6 \e[31m|\e[36m \e[33m%d\e[36m | \e[33m%d\e[36m | \e[32m%d\e[31m | \e[32m%d\e[36m | \e[32m%d\e[36m | \e[32m%d\e[31m | \e[32m%d\e[36m | \e[33m%d\e[36m | \e[33m%d\e[36m \e[31m|\e[36m\n", ar[5][0], ar[5][1], ar[5][2], ar[5][3], ar[5][4], ar[5][5], ar[5][6], ar[5][7], ar[5][8]);
	printf("  \e[31m|\e[36m\e[31m___\e[36m|\e[31m___\e[36m|\e[31m___\e[36m\e[31m|\e[36m\e[31m___\e[36m|\e[31m___\e[36m|\e[31m___\e[36m\e[31m|\e[36m\e[31m___\e[36m|\e[31m___\e[36m|\e[31m___\e[36m\e[31m|\e[36m\n7 \e[31m|\e[36m \e[32m%d\e[36m | \e[32m%d\e[36m | \e[32m%d\e[31m | \e[33m%d\e[36m | \e[32m%d\e[36m | \e[32m%d\e[31m | \e[32m%d\e[36m | \e[32m%d\e[36m | \e[32m%d\e[36m \e[31m|\e[36m\n", ar[6][0], ar[6][1], ar[6][2], ar[6][3], ar[6][4], ar[6][5], ar[6][6], ar[6][7], ar[6][8]);
	printf("  \e[31m|\e[36m___|___|___\e[31m|\e[36m___|___|___\e[31m|\e[36m___|___|___\e[31m|\e[36m\n8 \e[31m|\e[36m \e[32m%d\e[36m | \e[33m%d\e[36m | \e[32m%d\e[31m | \e[32m%d\e[36m | \e[32m%d\e[36m | \e[33m%d\e[31m | \e[32m%d\e[36m | \e[32m%d\e[36m | \e[32m%d\e[36m \e[31m|\e[36m\n", ar[7][0], ar[7][1], ar[7][2], ar[7][3], ar[7][4], ar[7][5], ar[7][6], ar[7][7], ar[7][8]);
	printf("  \e[31m|\e[36m___|___|___\e[31m|\e[36m___|___|___\e[31m|\e[36m___|___|___\e[31m|\e[36m\n9 \e[31m|\e[36m \e[32m%d\e[36m | \e[32m%d\e[36m | \e[32m%d\e[31m | \e[32m%d\e[36m | \e[32m%d\e[36m | \e[33m%d\e[31m | \e[32m%d\e[36m | \e[33m%d\e[36m | \e[33m%d\e[36m \e[31m|\e[36m\n", ar[8][0], ar[8][1], ar[8][2], ar[8][3], ar[8][4], ar[8][5], ar[8][6], ar[8][7], ar[8][8]);
  printf("  \e[31m|___\e[36m|\e[31m___\e[36m|\e[31m___|___\e[36m|\e[31m___\e[36m|\e[31m___|___\e[36m|\e[31m___\e[36m|\e[31m___|\e[36m\n");
}


void qirit(){
  printf("Qatorni kiriting: ");
  scanf("%d", &q);
  printf("Ustunni kiriting: ");
  scanf("%d", &u);
  printf("Sonni kiriting: ");
  scanf("%d", &son);

}
    
    
void hato(){
  if(q<1 || q>9 || u<1 || u>9){
    printf("[1] va [9] oraligdagi qatorni yoki ustunni kiriting!!!\n ");
    qirit();
  }
  if(ar[q-1][u-1]==0){
   for(int i=0; i<9; i++){
    if(son==ar[q-1][i] && i!=u-1){
     ar[q-1][u-1]=son;
     karta();
     printf("Bu son bor\n");
     kiritsh2();
    }
   }
   for(int i=0; i<9; i++){
    if(son==ar[i][u-1] && i!=q-1){
     ar[q-1][u-1]=son;
     karta();
     printf("Bu son bor\n");
     kiritsh2();
    }
   }
   ar[q-1][u-1]=son;
 }
 else{
   printf("Buerga qoeb bolmide\n");
   qirit();
 }
  
  if(q-1<3){
    if(u-1<3){
      for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
          if(ar[i][j]==son && i!=q-1 && j!=u-1){
           ar[q-1][u-1]=son;
           karta();
           printf("Bu son bor\n");
           kiritsh2();
          }
        }
      }
    }
    else if(u-1<6 && u-1>2){
      for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
          if(ar[i][j]==son && i!=q-1 && j!=u-1){
           ar[q-1][u-1]=son;
           karta();
           printf("Bu son bor\n");
           kiritsh2();
          }
        }
      }
    }
    else if(u-1>5 && u-1<9){
      for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
         if(ar[i][j]==son && i!=q-1 && j!=u-1){
           ar[q-1][u-1]=son;
           karta();
           printf("Bu son bor\n");
           kiritsh2();
         }
        }
     }
    }
  }
  
  else if(q-1>2 && q-1<6){
    if(u-1<3){
      for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
          if(ar[i][j]==son && i!=q-1 && j!=u-1){
           ar[q-1][u-1]=son;
           karta();
           printf("Bu son bor\n");
           kiritsh2();
          }
        }
      }
    }
    else if(u-1<6 && u-1>2){
      for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
          if(ar[i][j]==son && i!=q-1 && j!=u-1){
           ar[q-1][u-1]=son;
           karta();
           printf("Bu son bor\n");
           kiritsh2();
          }
        }
      }
    }
    else if(u-1>5 && u-1<9){
        for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
         if(ar[i][j]==son && i!=q-1 && j!=u-1){
           ar[q-1][u-1]=son;
           karta();
           printf("Bu son bor\n");
           kiritsh2();
         }
        }
     }
    }
  }
  
  else if(q-1>5 && q-1<9){
    if(u-1<3){
      for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
          if(ar[i][j]==son && i!=q-1 && j!=u-1){
           ar[q-1][u-1]=son;
           karta();
           printf("Bu son bor\n");
           kiritsh2();
          }
        }
      }
    }
    else if(u-1<6 && u-1>2){
      for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
          if(ar[i][j]==son && i!=q-1 && j!=u-1){
           ar[q-1][u-1]=son;
           karta();
           printf("Bu son bor\n");
           kiritsh2();
          }
        }
      }
    }
    else if(u-1>5 && u-1<9){
        for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
         if(ar[i][j]==son && i!=q-1 && j!=u-1){
           ar[q-1][u-1]=son;
           karta();
           printf("Bu son bor\n");
           kiritsh2();
         }
        }
     }
    }
  }


  int s=0;
  for(int i=0; i<9; i++){
    for(int j=0; j<9; j++){
      if(ar[i][j]==0){
        s++;
      }
    }
  }
  if(s==0){
    w--;
  }
  s=0;
}


void kiritsh2(){
  printf("Boshqa sonni kiriting: ");
  scanf("%d", &son);
  ar[q-1][u-1]=0;
  hato();
}





  



// printf("%d \e[31m%d\e[0m  %d", 6, 76, 1);








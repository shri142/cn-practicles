#include<stdio.h>
#include<stdlib.h>
int even_transfer()
{

}
int odd_transfer()
{

}
int even_reciever()
{

}
int odd_reciever()
{

}
int main()
{
    int a,b,c,d;
    int i;
    int choice;
    int store[7];
    begin:
    printf("------------------------Hamming Code-----------------------\n");
    printf("Press 1 for Converting Data word to Code word in Even Parity");
    printf("\n");
    printf("Press 2 for Converting Data word to Code word in Odd Parity");
    printf("\n");
    printf("Press 3 for finding error in Even Parity");
    printf("\n");
    printf("Press 4 for finding error in Odd Parity");
    scanf("%d",&choice);
    printf("\n");
    printf("-------------------------------------------------------------");
    printf("\n");
    if(choice<0&&choice>5)
    {
        printf("\nWrong Choice! Try Again :\n");
        goto begin;
    }
    else
    {

    start:
    printf("\nEnter the data in binary : \n");
   
    printf("Enter 1st bit : ");
    scanf("%d",&a);
    if(a!=0&&a!=1)
    {
        printf("Invalid number! Return to first step");
        goto start;
    }
    printf("Enter 2nd bit : ");
    scanf("%d",&b);
    if(b!=0&&b!=1)
    {
        printf("Invalid number! Return to first step");
        goto start;
    }
    printf("Enter 3rd bit : ");
    scanf("%d",&c);
    if(c!=0&&c!=1)
    {
        printf("Invalid number! Return to first step");
        goto start;
    }
    printf("Enter 4th bit : ");
    scanf("%d",&d);
    if(d!=0&&d!=1)
    {
        printf("Invalid number! Return to first step");
        goto start;
    }
    printf("Entered code : %d %d %d %d ",a,b,c,d);
    
    switch(choice)
    {
        case 1:
        even_transfer();
        break;

        case 2:
        odd_transfer();
        break;

        case 3:
        even_reciever();
        break;

        case 4: 
        odd_transfer();
        break;

        default:
        printf("Wrong choice! Go to start.");
	}
	}
    return 0;
}

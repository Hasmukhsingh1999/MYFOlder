#include <stdio.h>
typedef struct student
{
    int rno;
    char name[20];
    int marks;
}stud;

void main()

{
    FILE *fp;
    stud s;
    char ans ='Y';
    fp = fopen("student_data","a");
    while(ans=='Y' || ans =='y')
    {
        printf("Enter the roll_no , name , and marks");
        scanf("%d",&s.rno);
        gets(s.name);
        scanf("%d",&s.marks);
        // fwrite(&s.sizeof(s),1,fp);
        printf("Want to continue (y/n)");
        scanf("%c",&ans);

    }
    fclose(fp);
}
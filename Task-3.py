#include <stdio.h>
#include <string.h>

#define MAX_EMPLOYEES 100

// Structure to represent an employee
struct employee {
    int emp_number;
    char emp_name[50];
    float emp_salary;
};

int main() {
    struct employee employees[MAX_EMPLOYEES];
    int num_employees, search_emp_num;

    printf("Enter the number of employees: ");
    scanf("%d", &num_employees);

    if (num_employees > MAX_EMPLOYEES || num_employees <= 0) {
        printf("Invalid number of employees. Please enter a value between 1 and 100.\n");
        return 1;
    }

    // Input employee details
    for (int i = 0; i < num_employees; i++) {
        printf("Enter details for employee %d:\n", i + 1);
        printf("Employee Number: ");
        scanf("%d", &employees[i].emp_number);
        printf("Employee Name: ");
        scanf(" %[^\n]s", employees[i].emp_name);
        printf("Employee Salary: ");
        scanf("%f", &employees[i].emp_salary);
    }

    // Searching for an employee by employee number
    printf("\nEnter the employee number to search: ");
    scanf("%d", &search_emp_num);

    int found = 0;
    for (int i = 0; i < num_employees; i++) {
        if (employees[i].emp_number == search_emp_num) {
            printf("\nEmployee Found!\n");
            printf("Employee Number: %d\n", employees[i].emp_number);
            printf("Employee Name: %s\n", employees[i].emp_name);
            printf("Employee Salary: %.2f\n", employees[i].emp_salary);
            found = 1;
            break;
        }
    }

    if (!found) {
        printf("\nEmployee with employee number %d not found.\n", search_emp_num);
    }

    return 0;
}

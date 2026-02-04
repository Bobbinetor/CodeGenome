// calcolatrice.c
#include <stdio.h>
#include <math.h>

double somma(double a, double b) {
    return a + b;
}

double sottrai(double a, double b) {
    return a - b;
}

double moltiplica(double a, double b) {
    return a * b;
}

double dividi(double a, double b) {
    if (b == 0) {
        fprintf(stderr, "Errore: divisione per zero!\n");
        return NAN;
    }
    return a / b;
}

double potenza(double base, double esponente) {
    return pow(base, esponente);
}

// Il main viene compilato solo se NON stai facendo i test
#ifndef TEST_MODE
int main() {
    int scelta;
    double num1, num2;

    printf("=== Calcolatrice ===\n");
    printf("1. Addizione\n2. Sottrazione\n3. Moltiplicazione\n");
    printf("4. Divisione\n5. Potenza\nScelta: ");
    scanf("%d", &scelta);

    printf("Inserisci due numeri: ");
    scanf("%lf %lf", &num1, &num2);

    switch (scelta) {
        case 1: printf("Risultato: %.2lf\n", somma(num1, num2)); break;
        case 2: printf("Risultato: %.2lf\n", sottrai(num1, num2)); break;
        case 3: printf("Risultato: %.2lf\n", moltiplica(num1, num2)); break;
        case 4: printf("Risultato: %.2lf\n", dividi(num1, num2)); break;
        case 5: printf("Risultato: %.2lf\n", potenza(num1, num2)); break;
        default: printf("Scelta non valida!\n");
    }

    return 0;
}
#endif


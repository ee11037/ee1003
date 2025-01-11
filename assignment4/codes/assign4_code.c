#include <stdio.h>
#include <math.h>

#define N 1000  // Number of iterations
#define H 0.001 // Step size

// Function to compute the next points
void solve_diff_eq(double *y_points, double *y_prime_points) {
    // Initial conditions
    double y1 = 2.0;   // y(0) = 2
    double y2 = 1.0;   // y'(0) = 1
    double t = 0.0;    // Starting point (x = 0)

    y_points[0] = y1;
    y_prime_points[0] = y2;

    // Trapezoidal method iteration
    for (int n = 1; n < N; n++) {
        // Calculate y1(n+1) and y2(n+1) using the trapezoidal rule
        double y2_next = y2 + H / 2 * (y2 + y2);  // y2' = y2 (from y' = y)
        double y1_next = y1 + H / 2 * (y2 + y2_next); // y1' = y2

        // Store the points for plotting
        y_points[n] = y1_next;
        y_prime_points[n] = y2_next;

        // Update for the next step
        y1 = y1_next;
        y2 = y2_next;
        t += H;
    }
}



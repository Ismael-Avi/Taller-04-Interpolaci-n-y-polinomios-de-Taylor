import numpy as np
import matplotlib.pyplot as plt

def taylor_ln(x, n):
    """Polinomio de Taylor de grado n de ln(x) alrededor de x0 = 1."""
    suma = 0
    for k in range(1, n + 1):
        suma = suma + (-1)**(k + 1) * (x - 1)**k / k
    return suma
print(taylor_ln(2.5, 10))  

#Grafica 1
x_vals = np.linspace(0.1, 3, 400)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, np.log(x_vals), label=r'$\ln(x)$', color='black', linewidth=2)

for n in [1, 2, 3, 6]:
    plt.plot(x_vals, taylor_ln(x_vals, n), '--', label=f'$P_{n}(x)$')

plt.plot(1, 0, 'ro', label='Punto $(1, 0)$')  # Marcar el punto (1, 0)
plt.ylim(-3, 2)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title(r'Aproximación de $\ln(x)$ con Polinomios de Taylor en $x_0 = 1$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 3. Gráfica 2: Error absoluto y cota del error
n_vals = np.arange(1, 31)
errores_1_5 = [abs(np.log(1.5) - taylor_ln(1.5, n)) for n in n_vals]
errores_2_5 = [abs(np.log(2.5) - taylor_ln(2.5, n)) for n in n_vals]
cota_1_5 = (0.5**(n_vals + 1)) / (n_vals + 1)

plt.figure(figsize=(8, 5))
plt.semilogy(n_vals, errores_1_5, 'o-', label=r'Error en $x = 1.5$')
plt.semilogy(n_vals, cota_1_5, '--', label=r'Cota del error $|R_n(1.5)|$')
plt.semilogy(n_vals, errores_2_5, 's-', label=r'Error en $x = 2.5$')

plt.xlabel('Grado del polinomio ($n$)')
plt.ylabel('Error absoluto (escala logarítmica)')
plt.title('Convergencia y error de los polinomios de Taylor')
plt.legend()
plt.grid(True, which="both", alpha=0.3)
plt.show()
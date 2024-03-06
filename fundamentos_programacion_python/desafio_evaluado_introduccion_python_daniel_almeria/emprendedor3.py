"""
𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 ∗ 𝑈 − 𝐺𝑇
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales
"""

print("Actividad 1 - Rentabilidad (Emprendedor 3)")
print("-" * 100)


p_suscripcion = int(input("Precio de suscripción: "))
n_usuarios = int(input("Número de usuarios: "))
gasto_total = int(input("Gasto total: "))
utilidades_ant = int(input("Utilidades del año anterior: "))

utilidades = p_suscripcion * n_usuarios - gasto_total

print("-" * 100)
print("-" * 100)

print(f"Las utilidades actuales son: {utilidades} CLP")
print(f"Las utilidades del año anterior fueron {utilidades_ant} CLP")
print(f"La razón entre las utilidades actuales y las del año anterior son {round(utilidades/utilidades_ant, 2)}")
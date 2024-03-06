print("Actividad 1 - Rentabilidad (Emprendedor 2)")
print("-" * 100)


p_suscripcion_normal = int(input("Precio de suscripción: "))
n_usuarios_normales = int(input("Número de usuarios normales: "))
n_usuarios_premium = int(input("Número de usuarios premium: "))
gasto_total = int(input("Gasto total: "))

p_suscripcion_premium = p_suscripcion_normal + p_suscripcion_normal * 0.5
print(p_suscripcion_premium)

utilidades = p_suscripcion_normal * n_usuarios_normales + p_suscripcion_premium * n_usuarios_premium - gasto_total

print("-" * 100)
print("-" * 100)

print(f"Las utilidades del proyecto son: {utilidades} CLP")
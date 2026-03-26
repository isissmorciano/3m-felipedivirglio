from coordinate_student import punti_student, linee_student

def main():
    punto_a = punti_student.crea_punto('x', 'y')
    punto_b = punti_student.crea_punto('x', 'y')
    punto_c = punti_student.crea_punto('x', 'y')

    print("=== Coordinate e Linee ===\n")
    print("punti: ")
    print(f"- Punto A: {punti_student.info_punto(punto_a)}")
    print(f"- Punto B: {punti_student.info_punto(punto_b)}")
    print(f"- Punto C: {punti_student.info_punto(punto_c)}")

    linea_ab = linee_student.crea_linea(punto_a, punto_b)
    linea_bc = linee_student.crea_linea(punto_b, punto_c)
    linea_ca = linee_student.crea_linea(punto_a, punto_c)

    print("\nLinee: ")
    for linea in [linea_ab, linea_bc, linea_ca]:
        lunghezza = round(linee_student.lungezza_linea(linea), 2)
        medio = linee_student.punto_medio(linea)
        print(f"- {linee_student.info_linea(linea)}: Lunghezza: {lunghezza}, Punto Medio: {punti_student.info_punto(medio)}")

    print("\ndistanze:")
    print("- Distanza tra A e B: ", round(punti_student.distanza_tra_punti(punto_a, punto_b), 2))
    print("- Distanza tra B e C: ", round(punti_student.distanza_tra_punti(punto_b, punto_c), 2))
    print("- Distanza tra C e A: ", round(punti_student.distanza_tra_punti(punto_c, punto_a), 2))


main()
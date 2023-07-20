
#tiempo(horas) de duración de un curso de python
este_curso = 1.5
max_duración = 7
min_duración = 2.5
en_promedio = 4 
#tiempo(horas) de duración de un curso de python editado
crudo_promedio = 5
crudo_dalto = 3.5

#1)Diferencia de duracion
print("--------------------")
diferencia_en_min = 100 - (este_curso / min_duración) * 100
diferencia_en_max = 100 - (este_curso / max_duración) * 100
duración_en_promedio = 100 - (este_curso / en_promedio) * 100

print(f"El curso de Dalto dura un {diferencia_en_min} % menos que el más rapido")
print(f"El curso de Dalto dura un {round(diferencia_en_max, 1)} % menos que el más largo")
print(f"El curso de Dalto dura un {duración_en_promedio} % en promedio de los otros cursos")
print("--------------------")

#2) Porcentaje del material inservible que se reduce
tiempo_vacio_promedio = 100 - (en_promedio / crudo_promedio) * 100
tiempo_vacio_dalto = 100 - (este_curso / crudo_dalto) * 100

print(f"Un curso promedio elimina {tiempo_vacio_promedio} % de teimpo vacio")
print(f"Este curso elimió el {round(tiempo_vacio_dalto, 1)} % de tiempo perdido")
print("--------------------")

#3) ¿Ver 10h de este curso a cuantos de otros cursos equivale? ¿y al reves?
print(f"Ver 10 horas de este curso equivale a ver {round((en_promedio/este_curso/10)*100, 1 )} horas de otros cursos")
print(f"Ver 10 horas de este curso equivale a ver {round((este_curso/en_promedio/10)*100, 1 )} horas de este cursos")
print("--------------------")
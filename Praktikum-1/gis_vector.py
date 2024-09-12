import numpy as np
import matplotlib.pyplot as plt

#Koordinat
titik_A = np.array([4.5, 2.5])
titik_B = np.array([5.7,2.4])

def hitung_jarak(titik_A, titik_B):
    jarak = np.sqrt(np.sum((titik_A - titik_B) ** 2))
    return jarak

jarak = hitung_jarak(titik_A, titik_B)
print("Jarak antara titik A dan B adalah:", jarak)

plt.scatter(titik_A[0], titik_A[1], color='red', label='Titik A')
plt.scatter(titik_B[0], titik_B[1], color='blue', label='Titik B')
plt.plot([titik_A[0], titik_B[0]], [titik_A[1], titik_B[1]], color='green', linestyle='--')

plt.title('Titik A dan Titik B')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()


with open("hasil_jarak.txt", 'w') as file:
    file.write(f'Jarak antara titik A dan B adalah: {jarak}')





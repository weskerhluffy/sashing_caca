'''
Created on 26/09/2018

@author: ernesto
'''

# XXX: http://codeforces.com/contest/1040/problem/B
if __name__ == '__main__':
    n, k = [int(x) for x in input().strip().split(" ")]
    tam_seccion = min((k << 1) + 1, n)
    num_secciones = n // tam_seccion
    sobrante_secciones = n % tam_seccion
    puntos_de_volteo = list(range(min(k, n - 1), n, tam_seccion))
    ultimo_abarcado = puntos_de_volteo[-1] + k
    if ultimo_abarcado < n - 1:
        punto_extra = ultimo_abarcado + k + 1
        puntos_de_volteo += [punto_extra]
        puntos_de_volteo = list(map(lambda p:p - max(0, punto_extra - n + 1), puntos_de_volteo))
    puntos_de_volteo = list(map(lambda p:p + 1, puntos_de_volteo))
    print("{}".format(len(puntos_de_volteo)))
    print("{}".format(" ".join(map(str, puntos_de_volteo))))

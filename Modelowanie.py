import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

#Generowanie modelu metodą Ball Pivoting
def wyznaczanie_normalnych(chmura_punktow):
    print("Wyznaczanie normalnych dla punktów w chmurze punktów")
    chmura_punktow.normals = o3d.utility.Vector3dVector(np.zeros((1, 3))) 
    # Jeżeli istnieją normalne to są zerowane
    return chmura_punktow.estimate_normals()
    
def ball_pivoting(chmura_punktow, promienie_kul):
    chmura_punktow_z_normalnymi = wyznaczanie_normalnych(chmura_punktow)
    tin = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(chmura_punktow, o3d.utility.DoubleVector(promienie_kul))
    o3d.visualization.draw_geometries([tin])
    
#Generowanie modelu metodą Poissona
def poisson(chmura_punktow):
    print("Przetwarzanie danych algorytmem Poissona")
    wyznaczanie_normalnych(chmura_punktow)
    with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
        tin, gestosc =\
    o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(chmura_punktow, depth=15)
    print(tin)
    o3d.visualization.draw_geometries([tin])
    return tin, gestosc

#Wyświetlanie gęstości chmur punktów
def wyswietlanie_gestosc(gestosc, tin):
    gestosc = np.asarray(gestosc)
    gestosc_colors = plt.get_cmap('plasma')((gestosc - gestosc.min())/(gestosc.max() - gestosc.min()))
    gestosc_colors = gestosc_colors[:, :3]
    gestosc_mesh = o3d.geometry.TriangleMesh()
    gestosc_mesh.vertices = tin.vertices
    gestosc_mesh.triangles = tin.triangles
    gestosc_mesh.triangle_normals = tin.triangle_normals
    gestosc_mesh.vertex_colors = o3d.utility.Vector3dVector(gestosc_colors)
    o3d.visualization.draw_geometries([gestosc_mesh])

#Usunięcie punktów w oparciu o wyliczona gęstość
def filtracja_modelu_w_oparciu_o_gęstość(tin, gestosc, kwantyl = 0.01):
    print("Usuniecie trójkątów powstałych w oparciu o małą liczbę punktów")
    vertices_to_remove = gestosc < np.quantile(gestosc, kwantyl)
    tin.remove_vertices_by_mask(vertices_to_remove)
    print(tin)
    o3d.visualization.draw_geometries([tin])
def poisson_filtracja(chmura_punktów):
    tin, gęstość = poisson(chmura_punktów)
    wyswietlanie_gestosc(gęstość, tin)
    filtracja_modelu_w_oparciu_o_gęstość(tin, gęstość, kwantyl = 0.05)
    o3d.io.write_triangle_mesh("model_3d.ply", tin)